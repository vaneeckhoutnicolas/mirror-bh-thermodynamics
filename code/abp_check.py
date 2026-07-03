import sympy as sp

# ABP 2015: a = sin 2beta, cosh 2alpha = 1/cos beta, t = 2 sqrt(M) cosh a, x = 2 sqrt(M) sinh a
# S = (t^2-x^2)^4 / (4 (t^2+x^2)^2),  R = -4(t^4+10 t^2 x^2+x^4)/[(t^2-x^2)^2 (t^4-6 t^2 x^2+x^4)]
# Notre carte: R+S+ = (nu-2)(nu+1)/(2nu), R-S- = -(nu-1)(nu+2)/(2nu), nu = sqrt(1-a^2)

beta, Ms = sp.symbols('beta M', positive=True)
al = sp.acosh(1/sp.cos(beta))/2
t = 2*sp.sqrt(Ms)*sp.cosh(al)
x = 2*sp.sqrt(Ms)*sp.sinh(al)
S = (t**2 - x**2)**4/(4*(t**2 + x**2)**2)
R = -4*(t**4 + 10*t**2*x**2 + x**4)/((t**2 - x**2)**2*(t**4 - 6*t**2*x**2 + x**4))
RS_abp = sp.simplify(R*S)

a = sp.sin(2*beta)
nu = sp.sqrt(1 - a**2)   # = cos 2beta, valable |beta|<pi/4 (branche externe)
ours_plus = (nu - 2)*(nu + 1)/(2*nu)
print("branche externe (|beta|<pi/4):")
print("  difference RS_ABP - RS_nous:", sp.simplify(sp.trigsimp(RS_abp - ours_plus)))

# branche interne: pi/4 < beta < pi/2, cos 2beta < 0, nu = -cos 2beta
nu_in = -sp.cos(2*beta)
ours_minus = -(nu_in - 1)*(nu_in + 2)/(2*nu_in)
diff_in = sp.simplify(sp.trigsimp(RS_abp - ours_minus))
b0 = sp.Rational(2,5)*sp.pi  # point test dans (pi/4, pi/2)
print("branche interne (pi/4<beta<pi/2):")
print("  difference symbolique:", diff_in)
print("  valeur au point test beta=2pi/5:", sp.simplify(diff_in.subs(beta, b0)))
# somme des deux branches au meme a
print("somme R+S+ + R-S- (via ABP, deux valeurs de beta a meme a):")
b_out = sp.Rational(1,10)*sp.pi
b_in = sp.pi/2 - b_out
tot = sp.simplify(RS_abp.subs(beta, b_out) + RS_abp.subs(beta, b_in))
print("  =", tot)
