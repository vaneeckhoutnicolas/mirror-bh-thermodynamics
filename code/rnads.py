from mpmath import mp, mpf, mpc, polyroots, diff, pi, nstr
mp.dps = 40

def roots_rnads(M, Q, L):
    # r^4/L^2 + r^2 - 2 M r + Q^2 = 0
    return polyroots([1/L**2, 0, 1, -2*M, Q**2], maxsteps=200, extraprec=100)

def branch_S(M0, Q0, L, r0):
    def S(M, Q):
        rs = roots_rnads(M, Q, L)
        r = min(rs, key=lambda z: abs(z - r0))
        return pi*r**2
    return S

def curvature_RS(M0, Q0, L, r0):
    S = branch_S(M0, Q0, L, r0)
    d = {}
    for i in range(4):
        for j in range(4 - i):
            if 2 <= i + j <= 3:
                d[(i,j)] = diff(S, (M0, Q0), (i, j))
    sg = -1  # g = -Hess(S), calibre sur Kerr
    E, F, G = sg*d[(2,0)], sg*d[(1,1)], sg*d[(0,2)]
    Ex, Ey = sg*d[(3,0)], sg*d[(2,1)]
    Fx, Fy = sg*d[(2,1)], sg*d[(1,2)]
    Gx, Gy = sg*d[(1,2)], sg*d[(0,3)]
    def det3(a):
        return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
               -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
               +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))
    m1 = [[0, Ex/2, Fx-Ey/2],[Fy-Gx/2, E, F],[Gy/2, F, G]]
    m2 = [[0, Ey/2, Gx/2],[Ey/2, E, F],[Gx/2, F, G]]
    K = (det3(m1)-det3(m2))/(E*G-F**2)**2
    R = 2*K
    return R*pi*r0**2

def test(M, Q, L):
    rs = roots_rnads(mpf(M), mpf(Q), mpf(L))
    phys = sorted([r for r in rs if abs(r.imag) < mpf('1e-25') and r.real > 0], key=lambda z: -z.real)
    tot_all = mpc(0)
    tot_phys = mpc(0)
    for r0 in rs:
        rspr = curvature_RS(mpf(M), mpf(Q), mpf(L), r0)
        tot_all += rspr
        if abs(r0.imag) < mpf('1e-25') and r0.real > 0:
            tot_phys += rspr
    print(f"M={M} Q={Q} L={L}  n_phys={len(phys)}")
    print("  somme 2 horizons :", nstr(tot_phys, 12))
    print("  somme 4 racines  :", nstr(tot_all, 12))

for (M,Q,L) in [(1, 0.5, 10), (1, 0.5, 5), (1, 0.8, 10), (2, 0.7, 8), (1, 0.5, 100)]:
    test(M, Q, L)
