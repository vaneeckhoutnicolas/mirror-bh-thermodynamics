from mpmath import mp, mpf, sqrt, pi, diff, nstr
mp.dps = 40

# MP5D spins egaux a=b: r+-^2 = [(mu-2a^2) +- sqrt((mu-2a^2)^2-4a^4)]/2
# S_std = (pi^2/2)(r^2+a^2)^2/r ; M prop mu ; J = (pi/4) mu a
# coordonnees lineaires (m, j) = (mu, mu*a)

def S_branch(sign):
    def S(m, j):
        a = j/m
        b = m - 2*a**2
        r2 = (b + sign*sqrt(b**2 - 4*a**4))/2
        r = sqrt(r2)
        return (pi**2/2)*(r2 + a**2)**2/r
    return S

def RS(Sf, m0, j0):
    d = {}
    for i in range(4):
        for k in range(4-i):
            if 2 <= i+k <= 3:
                d[(i,k)] = diff(Sf, (m0, j0), (i, k))
    sg = -1
    E,F,G = sg*d[(2,0)], sg*d[(1,1)], sg*d[(0,2)]
    Ex,Ey,Fx,Fy = sg*d[(3,0)], sg*d[(2,1)], sg*d[(2,1)], sg*d[(1,2)]
    Gx,Gy = sg*d[(1,2)], sg*d[(0,3)]
    def det3(A):
        return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
               -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
               +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
    m1=[[0,Ex/2,Fx-Ey/2],[Fy-Gx/2,E,F],[Gy/2,F,G]]
    m2=[[0,Ey/2,Gx/2],[Ey/2,E,F],[Gx/2,F,G]]
    K=(det3(m1)-det3(m2))/(E*G-F*F)**2
    return 2*K*Sf(m0,j0)

print("MP5D spins egaux, branche externe vs Bravetti et al.")
print("Bravetti: RS = -u^2(u^2+12)/(u^4-16), u = s/J, s = S_std/pi, J_phys = (pi/4) mu a")
for (mu, a) in [(1, 0.3), (1, 0.42), (2, 0.5)]:
    mu, a = mpf(mu), mpf(a)
    m0, j0 = mu, mu*a
    Sp, Sm = S_branch(1), S_branch(-1)
    vplus = RS(Sp, m0, j0)
    vminus = RS(Sm, m0, j0)
    Sstd = Sp(m0, j0)
    Jphys = pi*mu*a/4
    u = (Sstd/pi)/Jphys
    bra = -u**2*(u**2 + 12)/(u**4 - 16)
    print(f"mu={mu} a={a}: RS+ (nous) = {nstr(vplus,12)}  Bravetti = {nstr(bra,12)}  ecart = {nstr(vplus-bra,6)}")
    print(f"          RS- = {nstr(vminus,12)}   somme = {nstr(vplus+vminus,12)}")
