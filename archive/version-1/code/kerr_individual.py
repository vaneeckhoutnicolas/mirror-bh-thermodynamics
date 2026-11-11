import sympy as sp

M, J = sp.symbols('M J', positive=True)

def brioschi_R(S, x, y, sigma=-1):
    E = sigma*sp.diff(S, x, 2); F = sigma*sp.diff(S, x, 1, y, 1); G = sigma*sp.diff(S, y, 2)
    m1 = sp.Matrix([[-sp.diff(E,y,2)/2 + sp.diff(F,x,1,y,1) - sp.diff(G,x,2)/2,
                     sp.diff(E,x)/2, sp.diff(F,x)-sp.diff(E,y)/2],
                    [sp.diff(F,y)-sp.diff(G,x)/2, E, F],
                    [sp.diff(G,y)/2, F, G]])
    m2 = sp.Matrix([[0, sp.diff(E,y)/2, sp.diff(G,x)/2],
                    [sp.diff(E,y)/2, E, F],
                    [sp.diff(G,x)/2, F, G]])
    return sp.simplify(2*(m1.det()-m2.det())/(E*G-F**2)**2)

res = {}
for sgn in (+1, -1):
    S = 2*sp.pi*(M**2 + sgn*sp.sqrt(M**4 - J**2))
    R = brioschi_R(S, M, J)
    RS = sp.simplify(R*S)
    res[sgn] = RS
    print("R"+("+" if sgn>0 else "-")+" S"+("+" if sgn>0 else "-"), "=", sp.factor(sp.simplify(RS)))

# en termes de nu = sqrt(N_R/N_L) = sqrt(1 - (J/M^2)^2)
nu = sp.Symbol('nu', positive=True)
for sgn in (+1,-1):
    e = res[sgn].subs(J, M**2*sp.sqrt(1-nu**2))
    e = sp.simplify(sp.powsimp(e, force=True))
    print("en nu:", "R±S± (", "+" if sgn>0 else "-", ") =", sp.factor(sp.simplify(e)))
