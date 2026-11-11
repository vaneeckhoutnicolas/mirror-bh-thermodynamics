"""
replay_short_article.py

Replays every numbered statement of the short article
"Two horizon Ruppeiner geometry of level homogeneous black hole entropies"
(version 2, November 2026).  Each check prints its tag, the statement it covers, and ok or FAILED.
The tags are those of the replay table at the end of the article.

Conventions: Ruppeiner metric g = - Hess S in the conserved charges (M, J);
scalar curvature with the sign for which the round sphere is positive.

The script imports nothing from the repository.  Dependencies: sympy, mpmath.
Run time: a few seconds.

    python3 replay_short_article.py
    python3 replay_short_article.py coefficients     (also prints the 25 coefficients of Appendix B)
"""
import sys

import sympy as sp
from mpmath import mp, mpf, sqrt as msqrt, pi as mpi, nstr

RESULTS = []


def check(tag, statement, cond):
    cond = bool(cond)
    RESULTS.append((tag, cond))
    print("[%-4s] %-6s %s" % (tag, "ok" if cond else "FAILED", statement))


def zero(e):
    return sp.simplify(sp.cancel(sp.together(e))) == 0


# ----------------------------------------------------------------------------
# jets: W(M) -> w0, w1, ... ; s(j) -> s0, s1, ... ; j = J / W(M)
# ----------------------------------------------------------------------------
w = sp.symbols('w0:6')
s = sp.symbols('s0:6')
j = sp.Symbol('j')


def Dj(e):
    """d/dj acting on j and on the jets of s"""
    return sp.diff(e, j) + sum(sp.diff(e, s[i]) * s[i + 1] for i in range(5))


def dW(e):
    """d/dM at fixed j: acts on the jets of W only"""
    return sum(sp.diff(e, w[i]) * w[i + 1] for i in range(5))


def dM(e):
    """d/dM at fixed J"""
    return sp.cancel(dW(e) - Dj(e) * j * w[1] / w[0])


def dJ(e):
    """d/dJ at fixed M"""
    return sp.cancel(Dj(e) / w[0])


def jets(S, dx, dy):
    p = {(0, 0): S}
    for b in range(4):
        for a in range(4 - b):
            if (a, b) == (0, 0):
                continue
            p[(a, b)] = dy(p[(0, b - 1)]) if a == 0 else dx(p[(a - 1, b)])
    return p


def ruppeiner_R(p):
    """scalar curvature of g = - Hess S from the jets p of S; round sphere positive"""
    q = {key: -val for key, val in p.items()}
    D = q[(2, 0)] * q[(0, 2)] - q[(1, 1)] ** 2
    Mx = sp.Matrix([[q[(2, 0)], q[(1, 1)], q[(0, 2)]],
                    [q[(3, 0)], q[(2, 1)], q[(1, 2)]],
                    [q[(2, 1)], q[(1, 2)], q[(0, 3)]]])
    return sp.cancel(-Mx.det() / (2 * D ** 2))


print("== A. The class S = W(M) s(J/W(M)) ==")
S = w[0] * s[0]
p = jets(S, dM, dJ)
alpha = s[0] - j * s[1]
Sigma = w[1] * w[3] / w[2] ** 2 + w[1] ** 2 / (w[0] * w[2])

check("A0", "the two derivations commute", zero(dM(dJ(S)) - dJ(dM(S))))
check("A1", "first derivatives: dS/dM = W' (s - j s'), dS/dJ = s'",
      zero(p[(1, 0)] - w[1] * alpha) and zero(p[(0, 1)] - s[1]))
gMM, gMJ, gJJ = -p[(2, 0)], -p[(1, 1)], -p[(0, 2)]
check("A2", "Proposition 1: ds^2 = - W'' (s - j s') dM^2 - W s'' dj^2",
      zero(gMM - (-w[2] * alpha - s[2] * j ** 2 * w[1] ** 2 / w[0]))
      and zero(gMJ - s[2] * j * w[1] / w[0]) and zero(gJJ + s[2] / w[0]))
check("A3", "det g = W'' s'' (s - j s') / W in the coordinates (M, J)",
      zero(gMM * gJJ - gMJ ** 2 - w[2] * s[2] * alpha / w[0]))

R = ruppeiner_R(p)
Sg = sp.Symbol('Sigma')
RS_formula = -(s[0] / (2 * alpha)) * (Sg + j * s[3] / s[2] + j ** 2 * s[2] / alpha)
check("A4", "Proposition 2: R S = -(s/(2 alpha)) (Sigma_W + j s'''/s'' + j^2 s''/alpha)",
      zero(R * S - RS_formula.subs(Sg, Sigma)))

E, G = -w[2] * alpha, -w[0] * s[2]
K = (-(Dj(Dj(E)) + dW(dW(G))) / (2 * E * G) + (dW(E) * dW(G) + Dj(E) ** 2) / (4 * E ** 2 * G)
     + (Dj(E) * Dj(G) + dW(G) ** 2) / (4 * E * G ** 2))
check("A5", "same result from the curvature formula of orthogonal coordinates (proof of Proposition 2)",
      zero(2 * K * S - RS_formula.subs(Sg, Sigma)))

# equivalence with the form in (M, sigma = J/S), phi defined by s phi(j/s) = 1
sig = j / s[0]
Phi = 1 / s[0]
phi1 = sp.cancel(Dj(Phi) / Dj(sig))
phi2 = sp.cancel(Dj(phi1) / Dj(sig))
check("A6", "phi - sigma phi' = 1/(s - j s') and W (phi''/phi) dsigma^2/(phi - sigma phi') = - W s'' dj^2",
      zero(Phi - sig * phi1 - 1 / alpha) and zero((phi2 / Phi) * Dj(sig) ** 2 * alpha + s[2]))

print("\n== B. The combination Sigma_W ==")
M, M0, Q, lam, cst = sp.symbols('M M_0 Q lambda c', positive=True)
pw = sp.Symbol('p', positive=True)


def Sigma_of(W):
    W1, W2, W3 = sp.diff(W, M), sp.diff(W, M, 2), sp.diff(W, M, 3)
    return sp.simplify(W1 * W3 / W2 ** 2 + W1 ** 2 / (W * W2))


check("B1", "Sigma_W = 2 for W = c (M - M_0)^p and for W = c exp(lambda M)",
      zero(Sigma_of(cst * (M - M0) ** pw) - 2) and zero(Sigma_of(cst * sp.exp(lam * M)) - 2))
h, l = w[1] / w[2], w[0] / w[1]
w3_on_shell = sp.solve(sp.Eq(Sigma, 2), w[3])[0]
check("B2", "converse: if Sigma_W = 2 then (W'/W'') / (W/W') is constant",
      zero(dW(h / l).subs(w[3], w3_on_shell)))
check("B3", "Kerr Sen at fixed charge, W = M^2 - Q^2/2: Sigma_W = 2/(1 - Q^2/(2M^2))",
      zero(Sigma_of(M ** 2 - Q ** 2 / 2) - 2 / (1 - Q ** 2 / (2 * M ** 2))))

print("\n== C. The two branch family s = 2 pi (1 +- nu), nu^2 = 1 - j^2 ==")
nu = sp.Symbol('nu', positive=True)
branch = {}
for e in (1, -1):
    sv = 2 * sp.pi * (1 + e * sp.sqrt(1 - j ** 2))
    d = [sv, sp.diff(sv, j), sp.diff(sv, j, 2), sp.diff(sv, j, 3)]
    val = RS_formula.subs({s[0]: d[0], s[1]: d[1], s[2]: d[2], s[3]: d[3]})
    val = sp.simplify(val.subs(j, sp.sqrt(1 - nu ** 2)))
    branch[e] = val
    if e == 1:
        dd = [sp.simplify(t.subs(j, sp.sqrt(1 - nu ** 2))) for t in d]
        jn = sp.sqrt(1 - nu ** 2)
        check("C0", "s' = -2 pi j/nu, s'' = -2 pi/nu^3, s''' = -6 pi j/nu^5, alpha = 2 pi (1 + nu)/nu (outer branch)",
              zero(dd[1] + 2 * sp.pi * jn / nu) and zero(dd[2] + 2 * sp.pi / nu ** 3)
              and zero(dd[3] + 6 * sp.pi * jn / nu ** 5) and zero(dd[0] - jn * dd[1] - 2 * sp.pi * (1 + nu) / nu))
Dsplit = (3 - Sg) * nu / 2 - 1 / nu
check("C1", "Theorem 1: R_pm S_pm = -1/2 pm [(3 - Sigma_W) nu/2 - 1/nu]",
      zero(branch[1] - (-sp.Rational(1, 2) + Dsplit)) and zero(branch[-1] - (-sp.Rational(1, 2) - Dsplit)))
check("C2", "Theorem 1: R_+ S_+ + R_- S_- = -1 for every level function", zero(branch[1] + branch[-1] + 1))
cross = branch[1] * (1 - nu) / (1 + nu) + branch[-1] * (1 + nu) / (1 - nu)
check("C3", "cross sum R_+ S_- + R_- S_+ = 3 + 2 (Sigma_W - 2) nu^2/(1 - nu^2); equal to 3 iff Sigma_W = 2",
      zero(cross - 3 - 2 * (Sg - 2) * nu ** 2 / (1 - nu ** 2)))
Jk = sp.Symbol('J', positive=True)
nuK = sp.sqrt(1 - Jk ** 2 / M ** 4)
for e in (1, -1):
    Rk = branch[e].subs(Sg, 2) / (2 * sp.pi * M ** 2 * (1 + e * nu))
    target = 1 / (4 * sp.pi * M ** 2) - e / (2 * sp.pi * M ** 2 * nu)
    if e == 1:
        okK = zero(Rk - target)
    else:
        okK = okK and zero(Rk - target)
check("C4", "Kerr: R_pm = 1/(4 pi M^2) -+ 1/(2 pi sqrt(M^4 - J^2))", okK)
sK = {1: (2 * sp.pi * (1 + nu), -2 * sp.pi / nu ** 3, 2 * sp.pi * (1 + nu) / nu),
      -1: (2 * sp.pi * (1 - nu), 2 * sp.pi / nu ** 3, 2 * sp.pi * (nu - 1) / nu)}
qq = sp.Symbol('q', positive=True)
Sig_ks = 2 / (1 - qq ** 2 / 2)
check("C6", "Kerr Sen: (3 - Sigma_W)/2 = (2 - 3 q^2)/(2 (2 - q^2)) and cross sum = 3 + 4 q^2 nu^2/((2 - q^2)(1 - nu^2))",
      zero((3 - Sig_ks) / 2 - (2 - 3 * qq ** 2) / (2 * (2 - qq ** 2)))
      and zero(cross.subs(Sg, Sig_ks) - 3 - 4 * qq ** 2 * nu ** 2 / ((2 - qq ** 2) * (1 - nu ** 2))))
check("C5", "the metric is indefinite on both branches when W W'' > 0: s'' alpha < 0",
      all(sp.simplify(sK[e][1] * sK[e][2]).subs(nu, sp.Rational(1, 3)) < 0 for e in (1, -1))
      and zero(sK[1][1] * sK[1][2] + (2 * sp.pi) ** 2 * (1 + nu) / nu ** 4)
      and zero(sK[-1][1] * sK[-1][2] + (2 * sp.pi) ** 2 * (1 - nu) / nu ** 4))

print("\n== D. Independent route: direct computation with S = 2 pi (W +- rho), rho^2 = W^2 - k(J) ==")
kj = sp.symbols('k0:6')
rho = sp.Symbol('rho')


def dM2(e):
    return sp.cancel(dW(e) + sp.diff(e, rho) * w[0] * w[1] / rho)


def dJ2(e):
    return sp.cancel(sum(sp.diff(e, kj[i]) * kj[i + 1] for i in range(5)) - sp.diff(e, rho) * kj[1] / (2 * rho))


Sp = 2 * sp.pi * (w[0] + rho)
Tp = sp.cancel(ruppeiner_R(jets(Sp, dM2, dJ2)) * Sp)
Tm = Tp.subs(rho, -rho)
Jq = sp.Symbol('Jq', positive=True)
mirror = {kj[0]: Jq ** 2, kj[1]: 2 * Jq, kj[2]: 2, kj[3]: 0, kj[4]: 0}


def on_mirror(e):
    e = e.subs(mirror).subs(Jq, sp.sqrt(w[0] ** 2 - rho ** 2))
    return sp.simplify(e.subs(rho, nu * w[0]))


check("D1", "Theorem 1 again, without Propositions 1 and 2",
      zero(on_mirror(Tp) - (-sp.Rational(1, 2) + Dsplit.subs(Sg, Sigma)))
      and zero(on_mirror(Tp + Tm) + 1))

diag = sp.cancel(Tp + Tm)
k1, k2, k3 = kj[1], kj[2], kj[3]
kk = sp.Symbol('k')
# sum + 1 = N / (A_+^2 A_-^2), with A_pm written without the relation rho^2 = W^2 - k
A_p = (k1 ** 2 + 2 * k2 * rho ** 2) * (w[0] + rho) * w[2] + (k1 ** 2 + 2 * k2 * rho ** 2 - 2 * k2 * w[0] ** 2) * w[1] ** 2
A_m = A_p.subs(rho, -rho)
Delta = A_p ** 2 * A_m ** 2
N_rho = sp.cancel((diag + 1) * Delta)
is_poly = sp.fraction(sp.together(N_rho))[1] == 1
N_rho = sp.expand(N_rho)
even = sp.expand(N_rho - N_rho.subs(rho, -rho)) == 0


def on_shell(e):
    """impose rho^2 = W^2 - k on an expression that is even in rho"""
    return sp.expand(sp.expand(e).subs(rho, sp.sqrt(w[0] ** 2 - kj[0]))).subs(kj[0], kk)


N_k = on_shell(N_rho)
P = sp.Poly(N_k, w[0], w[1], w[2], w[3])
coeffs = [c for c in P.coeffs()]
X = 2 * kk * k2 - k1 ** 2                      # the obstruction 2 k k'' - k'^2
check("D2", "Theorem 2 (only if): (sum + 1) A_+^2 A_-^2 is a polynomial N, even in rho, with %d terms in the jets of W; "
            "its coefficient of W''^4 alone is k^2 (2 k k'' - k'^2)^4" % len(coeffs),
      is_poly and even and len(coeffs) == 25 and zero(P.coeff_monomial(w[2] ** 4) - kk ** 2 * X ** 4))
check("D3", "Theorem 2 (if): all coefficients vanish when k''' = 0 and 2 k k'' = k'^2",
      all(zero(c.subs({k3: 0, k2: k1 ** 2 / (2 * kk)})) for c in coeffs))
Kf = sp.Function('K')(Jk)                    # K = sqrt(k)
check("D4", "2 k k'' - k'^2 = 4 k^(3/2) (sqrt k)''",
      zero(2 * Kf ** 2 * sp.diff(Kf ** 2, Jk, 2) - sp.diff(Kf ** 2, Jk) ** 2 - 4 * Kf ** 3 * sp.diff(Kf, Jk, 2)))
if "coefficients" in sys.argv[1:]:
    print("       the 25 coefficients of N; exponents are those of (W, W', W'', W'''):")
    for mono, c in sorted(P.terms()):
        print("      ", mono, sp.factor(c))
Gb = sp.groebner(coeffs, k3, k2, k1, kk, order='lex')
gens = [sp.factor(g) for g in Gb.exprs]
has_a = any(sp.simplify(g / (k1 ** 5 * k3)).is_number for g in gens)
has_b = any(sp.simplify(g / (k1 ** 6 * X)).is_number for g in gens)
check("D5", "cross check: a Groebner basis of the ideal of the 25 coefficients, in Q[k''', k'', k', k] with the "
            "lexicographic order k''' > k'' > k' > k, has %d elements and contains k'^5 k''' and k'^6 (2 k k'' - k'^2)" % len(gens),
      has_a and has_b)
top = [(m, c) for m, c in P.terms() if m[2] == 4]
N4 = sum(c * w[0] ** m[0] for m, c in top)
D4c = sp.Poly(on_shell(Delta), w[2]).coeff_monomial(w[2] ** 4)
check("D6", "terms of degree four in W'': N_4 = k X (X - 2 k'' W^2)^3 (k - W^2), so that "
            "sum + 1 -> X (W^2 - k) / (k (k'^2 + 2 k'' (W^2 - k))) when W'' -> infinity, X = 2 k k'' - k'^2",
      max(m[2] for m, c in P.terms()) == 4 and all(m[1] == 0 and m[3] == 0 for m, c in top)
      and zero(N4 - kk * X * (X - 2 * k2 * w[0] ** 2) ** 3 * (kk - w[0] ** 2))
      and zero(D4c - kk ** 2 * (2 * k2 * w[0] ** 2 - X) ** 4)
      and zero(N4 / D4c - X * (w[0] ** 2 - kk) / (kk * (k1 ** 2 + 2 * k2 * (w[0] ** 2 - kk))))
      and zero((N4 / D4c).subs({k1: 2 * Jq, k2: 2}).subs(kk, Jq ** 2 + sp.Symbol('C'))
               - sp.Symbol('C') * (w[0] ** 2 - Jq ** 2 - sp.Symbol('C')) / ((Jq ** 2 + sp.Symbol('C')) * (w[0] ** 2 - sp.Symbol('C')))))

print("\n== E. Kerr Newman at fixed charge: k = J^2 + C, C = Q^4/4, W = M^2 - Q^2/2 ==")
Cc = sp.Symbol('C', positive=True)
dev = (diag + 1).subs({kj[0]: Jq ** 2 + Cc, kj[1]: 2 * Jq, kj[2]: 2, kj[3]: 0, kj[4]: 0})
dev = sp.factor(sp.simplify(dev.subs(Jq, sp.sqrt(w[0] ** 2 - rho ** 2 - Cc))))
first = sp.simplify((dev / Cc).subs(Cc, 0).subs(rho, nu * w[0]))
A_, B_ = w[1] ** 2 / (w[0] * w[2]), w[1] * w[3] / w[2] ** 2
first_claim = (nu ** 2 * (1 + 2 * A_ * B_ + 4 * A_ ** 2) + A_ * (1 - 8 * nu ** 2)) / (w[0] ** 2 * (1 - nu ** 2))
check("E1", "sum + 1 = C [nu^2 (1 + 2AB + 4A^2) + A (1 - 8 nu^2)]/J^2 + O(C^2), A = W'^2/(W W''), B = W'W'''/W''^2",
      zero(first - first_claim))
kerr_first = first_claim.subs({w[0]: M ** 2, w[1]: 2 * M, w[2]: 2, w[3]: 0}).subs(nu, nuK) * Q ** 4 / 4
check("E2", "Kerr Newman: sum = -1 + Q^4 (3 M^4 - J^2)/(4 M^4 J^2) + O(Q^6)",
      zero(kerr_first - Q ** 4 * (3 * M ** 4 - Jk ** 2) / (4 * M ** 4 * Jk ** 2)))

mp.dps = 50
dev_f = sp.lambdify((w[0], w[1], w[2], w[3], kj[0], kj[1], kj[2], kj[3], rho), diag, 'mpmath')


def kn_sum(Mv, Jv, Qv):
    W0 = Mv ** 2 - Qv ** 2 / 2
    k0 = Jv ** 2 + Qv ** 4 / 4
    return dev_f(W0, 2 * Mv, mpf(2), mpf(0), k0, 2 * Jv, mpf(2), mpf(0), msqrt(W0 ** 2 - k0))


val = kn_sum(mpf(1), mpf(1) / 2, mpf(1) / 5)
print("       exact sum at (M, J, Q) = (1, 1/2, 1/5):", nstr(val, 30))
check("E3", "value at (1, 1/2, 1/5) is -0.9950920929 to ten digits", abs(val + mpf('0.9950920929')) < mpf(10) ** -10)
small = [(kn_sum(mpf(1), mpf(1) / 2, mpf(10) ** -n) + 1) / mpf(10) ** (-4 * n) for n in (1, 2, 3)]
print("       (sum + 1)/Q^4 at Q = 0.1, 0.01, 0.001:", ", ".join(nstr(t, 12) for t in small), " (limit 11/4)")
check("E4", "numerical confirmation of the Q^4 coefficient at M = 1, J = 1/2: limit 11/4",
      abs(small[2] - mpf(11) / 4) < mpf(10) ** -4 and abs(small[1] - mpf(11) / 4) < mpf(10) ** -2)
Mv, Jv, Qv = mpf(1), mpf(1) / 2, mpf(1) / 5
av = Jv / Mv
okS = True
for e in (1, -1):
    r = Mv + e * msqrt(Mv ** 2 - av ** 2 - Qv ** 2)
    S_area = mpi * (r ** 2 + av ** 2)
    W0 = Mv ** 2 - Qv ** 2 / 2
    S_class = 2 * mpi * (W0 + e * msqrt(W0 ** 2 - Jv ** 2 - Qv ** 4 / 4))
    okS = okS and abs(S_area - S_class) < mpf(10) ** -40
check("E5", "Kerr Newman entropies pi (r_pm^2 + a^2) are 2 pi (W pm sqrt(W^2 - J^2 - Q^4/4))", okS)

print("\n== F. Published closed forms ==")
# F1: Aman, Bengtsson, Pidokrajt, arXiv:1507.06097, eqs. (25), (26), (29): Kerr, both horizons, S = 2 M^2 (1 +- nu)
okF1 = True
for e in (1, -1):
    s0v, s1v, s2v = 2 * (1 + e * nu), -2 * e * j / nu, -2 * e / nu ** 3
    Ev = (-2 * (s0v - j * s1v)).subs(j, sp.sqrt(1 - nu ** 2))
    Gv = -M ** 2 * s2v
    T = e * nu / (4 * M * (1 + e * nu))
    E29 = -1 / (M * T)
    G29 = (M / 2) / (nu ** 2 * (1 + e * nu)) / T
    okF1 = okF1 and zero(Ev - E29) and zero(Gv - G29)
check("F1", "Proposition 1 on Kerr is eq. (29) of Aman, Bengtsson and Pidokrajt (2015), on both horizons", okF1)
# F2: same paper, eqs. (30), (31), (35), (37) with c = cos(2 beta)
c = sp.Symbol('c')
t2px2 = 4 * M * sp.sqrt(2 / (1 + c))       # t^2 + x^2 = 4 M cosh(2 alpha), cosh(2 alpha) = 1/cos(beta)
t2mx2 = 4 * M                               # t^2 - x^2
t2x2 = 4 * M ** 2 * (1 - c) / (1 + c)       # t^2 x^2 = 4 M^2 sinh^2(2 alpha)
t4px4 = t2px2 ** 2 - 2 * t2x2
S35 = t2mx2 ** 4 / (4 * t2px2 ** 2)
R37 = -4 * (t4px4 + 10 * t2x2) / (t2mx2 ** 2 * (t4px4 - 6 * t2x2))
fbranch = lambda x: -sp.Rational(1, 2) - 1 / x + x / 2
check("F2", "their unified curvature gives R S = f(cos 2 beta), f(x) = -1/2 - 1/x + x/2, and f(x) + f(-x) = -1",
      zero(S35 - 2 * M ** 2 * (1 + c)) and zero(R37 * S35 - fbranch(c)) and zero(fbranch(c) + fbranch(-c) + 1))
# F3: Bravetti, Momeni, Myrzakulov, Altaibayeva, arXiv:1303.2077, eq. (14) and the Ruppeiner curvature below eq. (23)
Sb, Jb = sp.symbols('S J', positive=True)
M14 = sp.Rational(3, 4) * Sb ** sp.Rational(2, 3) * (1 + 4 * Jb ** 2 / Sb ** 2) ** sp.Rational(2, 3)
lvl = sp.powsimp(sp.expand_power_base((sp.Rational(4, 3) * M14) ** sp.Rational(3, 2), force=True), force=True)
nub = (Sb ** 2 - 4 * Jb ** 2) / (Sb ** 2 + 4 * Jb ** 2)
R_bmma = -Sb * (Sb ** 2 + 12 * Jb ** 2) / (Sb ** 4 - 16 * Jb ** 4)
check("F3", "five dimensions, equal spins: (4M/3)^(3/2) = S + 4 J^2/S, and their Ruppeiner curvature is the outer branch of Theorem 1",
      zero(lvl - (Sb + 4 * Jb ** 2 / Sb)) and zero(R_bmma * Sb - fbranch(nub)))
# F3b: same family in units G = 1 from the horizon data (their eqs. 8 and 9 with S = A/4)
mu_v, a_v = mpf(1), mpf(3) / 10
okMP = True
for e in (1, -1):
    b_ = mu_v - 2 * a_v ** 2
    r2 = (b_ + e * msqrt(b_ ** 2 - 4 * a_v ** 4)) / 2
    S_h = (mpi ** 2 / 2) * (r2 + a_v ** 2) ** 2 / msqrt(r2)
    Wv = (mpi / 8) * mu_v ** mpf('1.5')
    Jv2 = (mpi / 4) * mu_v * a_v
    okMP = okMP and abs(S_h - 2 * mpi * (Wv + e * msqrt(Wv ** 2 - Jv2 ** 2))) < mpf(10) ** -40
check("F4", "five dimensions, equal spins, G = 1: S_pm = 2 pi (W pm sqrt(W^2 - J^2)), W = (pi/8) mu^(3/2), mu = 8M/(3 pi)", okMP)
# F5: Aman and Pidokrajt, arXiv:hep-th/0510139, eqs. (36), (50), (51): single spin Kerr in d dimensions
u, dd_ = sp.symbols('u d', positive=True)
n_ = 1 / (dd_ - 3)
Lg = 8 * n_ * u / (1 + 4 * u ** 2)
Pp = sp.Symbol('P', positive=True)
Du = lambda e: sp.diff(e, u) + sp.diff(e, Pp) * Lg * Pp
sA, jA = 1 / Pp, u / Pp
s1A = sp.cancel(Du(sA) / Du(jA))
s2A = sp.cancel(Du(s1A) / Du(jA))
s3A = sp.cancel(Du(s2A) / Du(jA))
RS_A = sp.cancel(RS_formula.subs({Sg: 2, s[0]: sA, s[1]: s1A, s[2]: s2A, s[3]: s3A, j: jA}))
kap = (dd_ - 5) / (dd_ - 3)
RS_50 = -(1 - 12 * kap * u ** 2) / ((1 - 4 * kap * u ** 2) * (1 + 4 * kap * u ** 2))
check("F5", "Proposition 2 reproduces eq. (50) of Aman and Pidokrajt for every d, and R S = -1 at d = 5 (their eq. 51)",
      zero(RS_A - RS_50) and zero(RS_A.subs(dd_, 5) + 1))
# F6: single branch companion s = c nu
cs = sp.Symbol('c_s', positive=True)
svv = cs * sp.sqrt(1 - j ** 2)
dv_ = [svv, sp.diff(svv, j), sp.diff(svv, j, 2), sp.diff(svv, j, 3)]
RS_odd = sp.simplify(RS_formula.subs({s[0]: dv_[0], s[1]: dv_[1], s[2]: dv_[2], s[3]: dv_[3]}))
check("F6", "Proposition 3: for S = c sqrt(W^2 - J^2), R S = -Sigma_W/2 - (1 - Sigma_W/2) j^2",
      zero(RS_odd - (-Sg / 2 - (1 - Sg / 2) * j ** 2)) and zero(RS_odd.subs(Sg, 2) + 1))
# F7: Aman, Bengtsson, Pidokrajt, arXiv:gr-qc/0601119, eq. (17) at a + b = 0 (full comparison: script 08)
R17_red = -(2 * s[0] * s[2] + j * s[0] * s[3] - 2 * j * s[1] * s[2] - j ** 2 * s[1] * s[3] + j ** 2 * s[2] ** 2) \
          / (2 * s[2] * w[0] * (s[0] - j * s[1]) ** 2)
check("F7", "for a power law level, Proposition 2 is eq. (17) of Aman, Bengtsson and Pidokrajt (2006) at a + b = 0",
      zero(RS_formula.subs(Sg, 2) / S - R17_red))

# F8: the same paper, eqs. (17) and (18) for general exponents a, b and an arbitrary function f,
#     against a direct computation of the Hessian curvature of psi = x^a f(x^b y)
xx, yy, ea, eb = sp.symbols('x y a b', positive=True)
sgm = sp.Symbol('sigma')
f0, f1, f2, f3 = sp.symbols('f0 f1 f2 f3')
Ff = sp.Function('f')


def to_f_symbols(e):
    e = e.doit()
    for n, sym in ((3, f3), (2, f2), (1, f1)):
        e = e.replace(lambda t: isinstance(t, sp.Subs) and isinstance(t.expr, sp.Derivative)
                      and sum(c for _, c in t.expr.variable_count) == n, lambda t, sym=sym: sym)
    return sp.simplify(e.subs(Ff(xx ** eb * yy), f0).subs(yy, sgm / xx ** eb))


psi = xx ** ea * Ff(xx ** eb * yy)
dpsi = {(i, k): sp.diff(psi, xx, i, yy, k) for i in range(4) for k in range(4) if 2 <= i + k <= 3}
Dh = dpsi[(2, 0)] * dpsi[(0, 2)] - dpsi[(1, 1)] ** 2
Mh = sp.Matrix([[dpsi[(2, 0)], dpsi[(1, 1)], dpsi[(0, 2)]],
                [dpsi[(3, 0)], dpsi[(2, 1)], dpsi[(1, 2)]],
                [dpsi[(2, 1)], dpsi[(1, 2)], dpsi[(0, 3)]]])
Dh, Rh = to_f_symbols(Dh), to_f_symbols(-Mh.det() / (2 * Dh ** 2))     # curvature of Hess psi, sphere positive
g18 = xx ** (2 * (ea + eb - 1)) * (ea * (ea - 1) * f0 * f2 - (ea + eb) ** 2 * f1 ** 2 - eb * (eb + 1) * sgm * f1 * f2)
br17 = (ea * (ea - 1) * (ea + eb) * f0 * f1 * f3 - 2 * ea * (ea - 1) * (ea + 2 * eb) * f0 * f2 ** 2
        - ea * eb * (ea - 1) * sgm * f0 * f2 * f3 + (ea + eb) ** 2 * (ea + eb - 1) * f1 ** 2 * f2
        + eb * (ea + eb) * (2 * ea + eb - 1) * sgm * f1 ** 2 * f3 + eb * (2 * eb - ea ** 2 - 3 * ea * eb) * sgm * f1 * f2 ** 2
        + eb ** 2 * (eb + 1) * sgm ** 2 * (f1 * f2 * f3 - f2 ** 3))
R17 = (eb + 1) * xx ** (3 * ea + 4 * eb - 4) / (2 * g18 ** 2) * br17
check("F8", "their eqs. (17) and (18) as transcribed, for general a, b, f: (17) is the curvature of - Hess psi (so of the Ruppeiner metric for psi = S)",
      zero(Dh - g18) and zero(Rh + R17))

print()
bad = [t for t, ok in RESULTS if not ok]
print("%d checks, %d failed%s" % (len(RESULTS), len(bad), (": " + ", ".join(bad)) if bad else ""))
raise SystemExit(1 if bad else 0)
