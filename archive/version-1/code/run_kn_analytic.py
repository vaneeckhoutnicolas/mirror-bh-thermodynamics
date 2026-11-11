import sympy as sp, sys
sys.path.insert(0, '/home/claude/galois')
from series_lib import Ser, evaluate, newton_root, brioschi_RS
from impl2 import implicit_partials, S_partials_expr

x, r, M, J = sp.symbols('x r M J')

def charge_MJ(Q0, M0, J0):
    Q0 = sp.Rational(*Q0)
    a = J/M
    Xi = 1 - a**2*x**2
    m = M*Xi**2
    q = Q0*Xi
    P = sp.expand(r**4*x**2 + (1 + a**2*x**2)*r**2 - 2*m*r + a**2 + q**2)
    S = sp.pi*(r**2 + a**2)/Xi
    sols, rf = implicit_partials(P, r, M, J)
    Sp_expr = S_partials_expr(S, r, M, J, sols, rf)
    sub = {M: sp.Rational(*M0), J: sp.Rational(*J0)}
    Pn = P.subs(sub)
    r0 = Ser({-1: sp.I, 0: -sub[M]})
    rser = newton_root(Pn, r, x, r0, {x: Ser.x(1)}, steps=5)
    env = {x: Ser.x(1), r: rser}
    Spser = {ij: evaluate(sp.together(e.subs(sub)), env) for ij, e in Sp_expr.items()}
    Sser = evaluate(S.subs(sub), env)
    RS = brioschi_RS(Spser, Sser)
    c0 = sp.nsimplify(sp.simplify(RS.coeff(0)))
    return sp.simplify(c0 + sp.conjugate(c0))

import time
pts = []
for Qn in [(0,1), (1,4), (1,2), (3,4), (1,1)]:
    t0 = time.time()
    v = charge_MJ(Qn, (1,1), (1,3))
    q = sp.Rational(*Qn)
    pts.append((q, v))
    print(f"Q={q}: charge paire = {v}   ({time.time()-t0:.0f}s)")

Qs = sp.Symbol('Q')
poly = sp.interpolate([(float(q), v) for q, v in pts], Qs)
print("polynome interpole:", sp.nsimplify(sp.expand(poly)))
print("conjecture: -25/8 + 5Q^2/16 + Q^4/16 =", sp.expand(sp.Rational(-25,8) + 5*Qs**2/16 + Qs**4/16))
