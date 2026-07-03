from mpmath import mp, mpf, mpc, polyroots, diff, pi, nstr
mp.dps = 50

# KN-AdS: a = J/M, Xi = 1 - a^2/L^2, m = M Xi^2, q = Q Xi
# P(r) = r^4/L^2 + (1+a^2/L^2) r^2 - 2 m r + (a^2 + q^2)
# S = pi (r^2 + a^2)/Xi

def setup(M, Q, J, L):
    a = J/M
    Xi = 1 - a**2/L**2
    m = M*Xi**2
    q = Q*Xi
    return a, Xi, m, q

def roots_kn(M, Q, J, L):
    a, Xi, m, q = setup(M, Q, J, L)
    return polyroots([1/L**2, 0, 1 + a**2/L**2, -2*m, a**2 + q**2],
                     maxsteps=300, extraprec=150), a, Xi

def curvature_RS(M0, Q0, J, L, r0):
    def S(M, Q):
        rs, a, Xi = roots_kn(M, Q, J, L)
        r = min(rs, key=lambda z: abs(z - r0))
        return pi*(r**2 + a**2)/Xi
    d = {}
    for i in range(4):
        for j in range(4 - i):
            if 2 <= i + j <= 3:
                d[(i,j)] = diff(S, (M0, Q0), (i, j))
    sg = -1
    E, F, G = sg*d[(2,0)], sg*d[(1,1)], sg*d[(0,2)]
    Ex, Ey, Fx, Fy = sg*d[(3,0)], sg*d[(2,1)], sg*d[(2,1)], sg*d[(1,2)]
    Gx, Gy = sg*d[(1,2)], sg*d[(0,3)]
    def det3(a3):
        return (a3[0][0]*(a3[1][1]*a3[2][2]-a3[1][2]*a3[2][1])
               -a3[0][1]*(a3[1][0]*a3[2][2]-a3[1][2]*a3[2][0])
               +a3[0][2]*(a3[1][0]*a3[2][1]-a3[1][1]*a3[2][0]))
    m1 = [[0, Ex/2, Fx-Ey/2],[Fy-Gx/2, E, F],[Gy/2, F, G]]
    m2 = [[0, Ey/2, Gx/2],[Ey/2, E, F],[Gx/2, F, G]]
    K = (det3(m1)-det3(m2))/(E*G-F**2)**2
    rs, a, Xi = roots_kn(M0, Q0, J, L)
    return 2*K*pi*(r0**2 + a**2)/Xi

def sums(M, Q, J, L):
    rs, a, Xi = roots_kn(mpf(M), mpf(Q), mpf(J), mpf(L))
    tphys, tvirt = mpc(0), mpc(0)
    for r0 in rs:
        v = curvature_RS(mpf(M), mpf(Q), mpf(J), mpf(L), r0)
        if abs(r0.imag) < mpf('1e-30') and r0.real > 0:
            tphys += v
        else:
            tvirt += v
    return tphys.real, tvirt.real

print("KN-AdS, fluctuations (M,Q) a J=0.3 fixe, M=1 Q=0.4:")
vals=[]
for L in [300, 1000, 3000]:
    p, v = sums(1, 0.4, 0.3, L)
    vals.append((L,v))
    print(f"  L={L}: phys={nstr(p,14)}  virt={nstr(v,14)}")
(L1,v1),(L2,v2) = vals[-2], vals[-1]
vinf = (v2*L2**2 - v1*L1**2)/(L2**2 - L1**2)
print("extrapolation virt:", nstr(vinf, 15))
print("reperes: -27/8 =", nstr(mpf(-27)/8,10), " -25/8 =", nstr(mpf(-25)/8,10))
