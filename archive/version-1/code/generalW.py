import sympy as sp

M, J = sp.symbols('M J', positive=True)
w = sp.Function('w')(M)

def RS_branch(sgn):
    S = 2*sp.pi*(w + sgn*sp.sqrt(w**2 - J**2))
    E = -sp.diff(S, M, 2); F = -sp.diff(S, M, 1, J, 1); G = -sp.diff(S, J, 2)
    Ex, Ey = sp.diff(E, M), sp.diff(E, J)
    Fx, Fy = sp.diff(F, M), sp.diff(F, J)
    Gx, Gy = sp.diff(G, M), sp.diff(G, J)
    m1 = sp.Matrix([[0, Ex/2, Fx-Ey/2],[Fy-Gx/2, E, F],[Gy/2, F, G]])
    m2 = sp.Matrix([[0, Ey/2, Gx/2],[Ey/2, E, F],[Gx/2, F, G]])
    K = (m1.det() - m2.det())/(E*G - F**2)**2
    return 2*K*S

W, a, b = sp.symbols('W a b', positive=True)   # W, W', W''
nu = sp.Symbol('nu', positive=True)

reps = {sp.Derivative(w, (M, 3)): 0, sp.Derivative(w, (M, 2)): b,
        sp.Derivative(w, M): a, w: W}

out = {}
for sgn in (+1, -1):
    e = RS_branch(sgn)
    # substituer les derivees (ordre decroissant)
    e = e.subs(sp.Derivative(w, (M, 3)), 0).subs(sp.Derivative(w, (M, 2)), b)\
         .subs(sp.Derivative(w, M), a).subs(w, W)
    e = e.subs(J, W*sp.sqrt(1 - nu**2))
    e = sp.simplify(sp.radsimp(sp.cancel(sp.together(e))))
    out[sgn] = e
    print("RS", "+" if sgn > 0 else "-", "=", sp.factor(e))

tot = sp.simplify(out[1] + out[-1])
print("somme:", sp.factor(tot))
D = sp.simplify((out[1] - out[-1])/2)
print("D = (RS+ - RS-)/2 =", sp.factor(D))
# cas Kerr: W = M^2, a = 2M, b = 2 -> a^2 = 4W
print("check Kerr (a^2=4W, b=2):", sp.simplify(D.subs(a, 2*sp.sqrt(W)).subs(b, 2)))
