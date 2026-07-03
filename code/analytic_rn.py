import sympy as sp

x, M, Q = sp.symbols('x M Q', positive=True)  # x = 1/L
Iu = sp.I
NORD = 6  # ordres de la serie pour r

# branche virtuelle r = i/x + sum c_k x^k, resolue ordre par ordre
r = Iu/x
cs = []
for k in range(NORD):
    ck = sp.Symbol(f'c{k}')
    rt = r + ck*x**k + sp.Symbol('junk')*x**(k+1)*0
    P = sp.expand(rt**4*x**2 + rt**2 - 2*M*rt + Q**2)
    # coefficient de x^(k-1) determine c_k
    coef = sp.expand(P).coeff(x, k-1)
    sol = sp.solve(coef, ck)
    ck_val = sp.simplify(sol[0])
    cs.append(ck_val)
    r = r + ck_val*x**k

print("branche virtuelle r = i/x +", " + ".join([f"({sp.simplify(c)}) x^{k}" for k,c in enumerate(cs)]))

S = sp.expand(sp.pi*r**2)
# tronquer au-dela de x^4
S = sum(S.coeff(x, n)*x**n for n in range(-2, 5))

def dd(f, a, b):
    return sp.diff(f, a, b[0]) if False else None

sg = -1
E = sg*sp.diff(S, M, 2); F = sg*sp.diff(S, M, 1, Q, 1); G = sg*sp.diff(S, Q, 2)
Ex, Ey = sp.diff(E, M), sp.diff(E, Q)
Fx, Fy = sp.diff(F, M), sp.diff(F, Q)
Gx, Gy = sp.diff(G, M), sp.diff(G, Q)
m1 = sp.Matrix([[0, Ex/2, Fx-Ey/2],[Fy-Gx/2, E, F],[Gy/2, F, G]])
m2 = sp.Matrix([[0, Ey/2, Gx/2],[Ey/2, E, F],[Gx/2, F, G]])
Knum = sp.expand(m1.det() - m2.det())
Kden = sp.expand((E*G - F**2)**2)
Rc = sp.simplify(2*Knum/Kden)
RS = sp.series(sp.expand(Rc*S), x, 0, 2).removeO()
lim = sp.simplify(RS.subs(x, 0))
print("R*S (une feuille virtuelle), limite plate:", sp.simplify(lim))
print("2*Re =", sp.simplify(lim + sp.conjugate(lim)))
