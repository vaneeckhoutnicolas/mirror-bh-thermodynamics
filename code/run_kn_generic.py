import sympy as sp, sys, time
sys.path.insert(0, '/home/claude/galois')
import series_lib
series_lib.NMAX = 8
from series_lib import Ser, evaluate, newton_root, brioschi_RS
from impl2 import implicit_partials, S_partials_expr

x, r, M, J, Q = sp.symbols('x r M J Q', positive=True)
a = J/M
Xi = 1 - a**2*x**2
m = M*Xi**2
q = Q*Xi
P = sp.expand(r**4*x**2 + (1 + a**2*x**2)*r**2 - 2*m*r + a**2 + q**2)
S = sp.pi*(r**2 + a**2)/Xi

t0 = time.time()
sols, rf = implicit_partials(P, r, M, J)          # frame angulaire (M,J), Q parametre
Sp_expr = S_partials_expr(S, r, M, J, sols, rf)
print(f"derivation implicite: {time.time()-t0:.0f}s")

sub = {M: sp.Integer(1), J: sp.Rational(1,3)}   # WLOG et J-independance prouvee, Q symbolique
Pn = sp.expand(P.subs(sub))
r0 = Ser({-1: sp.I, 0: sp.Integer(-1)})
rser = newton_root(Pn, r, x, r0, {x: Ser.x(1)}, steps=4)
env = {x: Ser.x(1), r: rser}
Spser = {ij: evaluate(sp.together(e.subs(sub)), env) for ij, e in Sp_expr.items()}
Sser = evaluate(S.subs(sub), env)
RS = brioschi_RS(Spser, Sser)
print(f"total: {time.time()-t0:.0f}s")
for k in range(-2, 1):
    c = sp.simplify(RS.coeff(k))
    print(f"coeff x^{k} (une feuille):", c)
c0 = sp.simplify(RS.coeff(0))
pair = sp.simplify(sp.expand(c0 + sp.conjugate(c0.subs(sp.I, -sp.I))))
print("paire virtuelle:", sp.factor(pair))
