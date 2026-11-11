import sympy as sp, sys
sys.path.insert(0, '/home/claude/galois')
from series_lib import Ser, evaluate, newton_root, brioschi_RS
from impl2 import implicit_partials, S_partials_expr

x, r, M, Q = sp.symbols('x r M Q')
P = r**4*x**2 + r**2 - 2*M*r + Q**2
S = sp.pi*r**2

sols, rf = implicit_partials(P, r, M, Q)
Sp_expr = S_partials_expr(S, r, M, Q, sols, rf)

def charge(M0, Q0):
    sub = {M: sp.Rational(M0[0], M0[1]), Q: sp.Rational(Q0[0], Q0[1])}
    Pn = P.subs(sub)
    env0 = {x: Ser.x(1)}
    r0 = Ser({-1: sp.I, 0: -sub[M]})
    rser = newton_root(Pn, r, x, r0, env0, steps=5)
    env = {x: Ser.x(1), r: rser}
    Spser = {ij: evaluate(e.subs(sub), env) for ij, e in Sp_expr.items()}
    Sser = evaluate(S.subs(sub), env)
    RS = brioschi_RS(Spser, Sser)
    negs = {k: RS.coeff(k) for k in range(-4, 0) if RS.coeff(k) != 0}
    c0 = sp.simplify(RS.coeff(0))
    return c0, negs

for pt in [((1,1),(1,2)), ((2,1),(1,3))]:
    c0, negs = charge(*pt)
    pair = sp.simplify(c0 + sp.conjugate(c0))
    print(f"(M,Q)={pt}: RS par feuille = {c0}, termes negatifs residuels = {negs}")
    print(f"   somme paire virtuelle = {pair}  =? -27/8 = {sp.Rational(-27,8)}")
