import sympy as sp
M, Q = sp.symbols('M Q', positive=True)

def brioschi_R(S, x, y, sigma=-1):
    E = sigma*sp.diff(S, x, 2); F = sigma*sp.diff(S, x, 1, y, 1); G = sigma*sp.diff(S, y, 2)
    Ex, Ey = sp.diff(E,x), sp.diff(E,y)
    Fx, Fy = sp.diff(F,x), sp.diff(F,y)
    Gx, Gy = sp.diff(G,x), sp.diff(G,y)
    Eyy, Fxy, Gxx = sp.diff(E,y,2), sp.diff(F,x,1,y,1), sp.diff(G,x,2)
    m1 = sp.Matrix([[-Eyy/2 + Fxy - Gxx/2, Ex/2, Fx - Ey/2],
                    [Fy - Gx/2, E, F],[Gy/2, F, G]])
    m2 = sp.Matrix([[0, Ey/2, Gx/2],[Ey/2, E, F],[Gx/2, F, G]])
    K = (m1.det() - m2.det())/(E*G - F**2)**2
    return sp.simplify(2*K)

tot = 0
for sgn in (+1, -1):
    r = M + sgn*sp.sqrt(M**2 - Q**2)
    S = sp.pi*r**2
    R = brioschi_R(S, M, Q)
    RS = sp.simplify(R*S)
    print("branche", "+" if sgn>0 else "-", ": R =", R, "  R*S =", RS)
    tot += RS
print("somme diagonale RN plat:", sp.simplify(tot))
