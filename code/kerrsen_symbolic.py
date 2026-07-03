import sympy as sp

M, J, W = sp.symbols('M J W', positive=True)
Q = sp.Symbol('Q', positive=True)

def brioschi_RS(S, x, y):
    E = -sp.diff(S,x,2); F = -sp.diff(S,x,1,y,1); G = -sp.diff(S,y,2)
    m1 = sp.Matrix([[0, sp.diff(E,x)/2, sp.diff(F,x)-sp.diff(E,y)/2],
                    [sp.diff(F,y)-sp.diff(G,x)/2, E, F],
                    [sp.diff(G,y)/2, F, G]])
    m2 = sp.Matrix([[0, sp.diff(E,y)/2, sp.diff(G,x)/2],
                    [sp.diff(E,y)/2, E, F],
                    [sp.diff(G,x)/2, F, G]])
    K = (m1.det()-m2.det())/(E*G-F**2)**2
    return sp.simplify(2*K*S)

Wex = M**2 - Q**2/2
res = {}
for sgn in (+1,-1):
    S = 2*sp.pi*(Wex + sgn*sp.sqrt(Wex**2 - J**2))
    res[sgn] = brioschi_RS(S, M, J)

# variables: nu = sqrt(1 - J^2/W^2), w = Q^2/(2M^2)
nu, w = sp.symbols('nu w', positive=True)
subsmap = {J: (M**2*(1-w))*sp.sqrt(1-nu**2), Q: sp.sqrt(2*w)*M}
for sgn in (+1,-1):
    e = res[sgn].subs(subsmap)
    e = sp.simplify(sp.powsimp(sp.radsimp(e), force=True))
    D = sp.simplify(e - (-sp.Rational(1,2)))
    print("RS", "+" if sgn>0 else "-", "= -1/2 +", sp.factor(sp.simplify(D)))
