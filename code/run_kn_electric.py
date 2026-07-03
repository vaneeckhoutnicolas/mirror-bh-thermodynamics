import sympy as sp, sys
sys.path.insert(0, '/home/claude/galois')
from series_lib import Ser, evaluate, newton_root, brioschi_RS
from impl2 import implicit_partials, S_partials_expr

x, r, M, Q = sp.symbols('x r M Q')

def charge_MQ(J0, M0, Q0):
    J0 = sp.Rational(*J0)
    a = J0/M
    Xi = 1 - a**2*x**2
    m = M*Xi**2
    q = Q*Xi
    P = sp.expand(r**4*x**2 + (1 + a**2*x**2)*r**2 - 2*m*r + a**2 + q**2)
    S = sp.pi*(r**2 + a**2)/Xi
    sols, rf = implicit_partials(P, r, M, Q)
    Sp_expr = S_partials_expr(S, r, M, Q, sols, rf)
    sub = {M: sp.Rational(*M0), Q: sp.Rational(*Q0)}
    Pn = P.subs(sub)
    r0 = Ser({-1: sp.I, 0: -sub[M]})
    rser = newton_root(Pn, r, x, r0, {x: Ser.x(1)}, steps=5)
    env = {x: Ser.x(1), r: rser}
    Spser = {ij: evaluate(sp.together(e.subs(sub)), env) for ij, e in Sp_expr.items()}
    Sser = evaluate(S.subs(sub), env)
    RS = brioschi_RS(Spser, Sser)
    c0 = sp.simplify(RS.coeff(0))
    return sp.simplify(c0 + sp.conjugate(c0))

for (J0, M0, Q0) in [((1,2),(1,1),(2,5)), ((1,3),(2,1),(1,2))]:
    v = charge_MQ(J0, M0, Q0)
    print(f"J={sp.Rational(*J0)}, M={sp.Rational(*M0)}, Q={sp.Rational(*Q0)}: charge = {v}")
