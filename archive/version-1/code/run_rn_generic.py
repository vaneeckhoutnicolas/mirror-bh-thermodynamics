import sympy as sp, sys, time
sys.path.insert(0, '/home/claude/galois')
import series_lib
series_lib.NMAX = 8
from series_lib import Ser, evaluate, newton_root, brioschi_RS
from impl2 import implicit_partials, S_partials_expr

x, r, M, Q = sp.symbols('x r M Q', positive=True)
P = r**4*x**2 + r**2 - 2*M*r + Q**2
S = sp.pi*r**2

t0 = time.time()
sols, rf = implicit_partials(P, r, M, Q)
Sp_expr = S_partials_expr(S, r, M, Q, sols, rf)

sub = {M: sp.Integer(1)}  # WLOG par invariance d'echelle, Q reste symbolique
Pn = sp.expand(P.subs(sub))
r0 = Ser({-1: sp.I, 0: sp.Integer(-1)})
rser = newton_root(Pn, r, x, r0, {x: Ser.x(1)}, steps=4)
env = {x: Ser.x(1), r: rser}
Spser = {ij: evaluate(sp.together(e.subs(sub)), env) for ij, e in Sp_expr.items()}
Sser = evaluate(S.subs(sub), env)
RS = brioschi_RS(Spser, Sser)
print(f"[{time.time()-t0:.0f}s]")
for k in range(-3, 1):
    print(f"coeff x^{k}:", sp.simplify(RS.coeff(k)))
