import sympy as sp

M, J, Q = sp.symbols('M J Q', positive=True)

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

# KN plat, coordonnees (M,J) a Q fixe
a = J/M
D = sp.sqrt(M**2 - a**2 - Q**2)
Sp = sp.pi*((M + D)**2 + a**2)
Sm = sp.pi*((M - D)**2 + a**2)
nu_expr = sp.simplify((Sp - Sm)/(Sp + Sm))

RSp = sp.simplify(brioschi_R(Sp, M, J)*Sp)
RSm = sp.simplify(brioschi_R(Sm, M, J)*Sm)
print("somme:", sp.simplify(RSp + RSm))

# conjecture: RSpm = -1/2 +- (nu^2-2)/(2 nu) avec nu = (S+-S-)/(S++S-)
pred_p = sp.simplify(-sp.Rational(1,2) + (nu_expr**2 - 2)/(2*nu_expr))
pred_m = sp.simplify(-sp.Rational(1,2) - (nu_expr**2 - 2)/(2*nu_expr))
print("ecart branche +:", sp.simplify(RSp - pred_p))
print("ecart branche -:", sp.simplify(RSm - pred_m))
