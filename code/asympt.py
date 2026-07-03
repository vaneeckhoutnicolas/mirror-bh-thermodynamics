from mpmath import mp, mpf, mpc, polyroots, diff, pi, nstr
mp.dps = 50

def roots_rnads(M, Q, L):
    return polyroots([1/L**2, 0, 1, -2*M, Q**2], maxsteps=300, extraprec=150)

def curvature_RS(M0, Q0, L, r0):
    def S(M, Q):
        rs = roots_rnads(M, Q, L)
        r = min(rs, key=lambda z: abs(z - r0))
        return pi*r**2
    d = {}
    for i in range(4):
        for j in range(4 - i):
            if 2 <= i + j <= 3:
                d[(i,j)] = diff(S, (M0, Q0), (i, j))
    sg = -1
    E, F, G = sg*d[(2,0)], sg*d[(1,1)], sg*d[(0,2)]
    Ex, Ey, Fx, Fy = sg*d[(3,0)], sg*d[(2,1)], sg*d[(2,1)], sg*d[(1,2)]
    Gx, Gy = sg*d[(1,2)], sg*d[(0,3)]
    def det3(a):
        return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
               -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
               +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))
    m1 = [[0, Ex/2, Fx-Ey/2],[Fy-Gx/2, E, F],[Gy/2, F, G]]
    m2 = [[0, Ey/2, Gx/2],[Ey/2, E, F],[Gx/2, F, G]]
    K = (det3(m1)-det3(m2))/(E*G-F**2)**2
    return 2*K*pi*r0**2

def virt_sum(M, Q, L):
    rs = roots_rnads(mpf(M), mpf(Q), mpf(L))
    tot = mpc(0)
    for r0 in rs:
        if abs(r0.imag) > mpf('1e-30'):
            tot += curvature_RS(mpf(M), mpf(Q), mpf(L), r0)
    return tot.real

print("Paire virtuelle, limite plate L -> inf :")
for (M,Q) in [(1, 0.5), (3, 1.2), (0.5, 0.4)]:
    vals = []
    for L in [100, 300, 1000, 3000]:
        v = virt_sum(M, Q, L)
        vals.append((L, v))
        print(f"  M={M} Q={Q} L={L}: {nstr(v, 15)}")
    # extrapolation Richardson en 1/L^2 : v = v_inf + c/L^2
    (L1,v1),(L2,v2) = vals[-2], vals[-1]
    vinf = (v2*L2**2 - v1*L1**2)/(L2**2 - L1**2)
    print(f"  -> extrapolation: {nstr(vinf, 15)}   (-27/8 = {nstr(mpf(-27)/8, 15)})")
