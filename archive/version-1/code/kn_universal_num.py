from mpmath import mp, mpf, sqrt, pi, diff, nstr
mp.dps = 40

def S_branch(sign, Q):
    def S(M, J):
        a = J/M
        D = sqrt(M**2 - a**2 - Q**2)
        return pi*((M + sign*D)**2 + a**2)
    return S

def RS(Sf, M0, J0):
    d = {}
    for i in range(4):
        for j in range(4-i):
            if 2 <= i+j <= 3:
                d[(i,j)] = diff(Sf, (M0, J0), (i, j))
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
    return 2*K*Sf(M0,J0)

print("KN plat, frame (M,J) a Q fixe: test RS(+/-) = -1/2 +/- (nu^2-2)/(2nu)")
for (M0,J0,Q0) in [(1,0.3,0.4),(1,0.5,0.2),(2,1.0,0.7),(1,0.2,0.8)]:
    M0,J0,Q0 = mpf(M0),mpf(J0),mpf(Q0)
    Sp, Sm = S_branch(1,Q0), S_branch(-1,Q0)
    vp, vm = RS(Sp,M0,J0), RS(Sm,M0,J0)
    nu = (Sp(M0,J0)-Sm(M0,J0))/(Sp(M0,J0)+Sm(M0,J0))
    pp = -mpf(1)/2 + (nu**2-2)/(2*nu)
    pm = -mpf(1)/2 - (nu**2-2)/(2*nu)
    print(f"M={M0} J={J0} Q={Q0}: somme={nstr(vp+vm,10)}  ecart+={nstr(vp-pp,6)}  ecart-={nstr(vm-pm,6)}")

print()
print("Frame electrique (M,Q) a J=0 (RN): RS=0, nu quelconque -> la fonction ne s'applique pas (famille plate)")
