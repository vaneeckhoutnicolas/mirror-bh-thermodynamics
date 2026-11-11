from mpmath import mp, mpf, mpc, polyroots, diff, pi, nstr
mp.dps = 50

def roots_kn(a, m, q, L):
    return polyroots([1/L**2, 0, 1 + a**2/L**2, -2*m, a**2 + q**2],
                     maxsteps=300, extraprec=150)

def make_S_MJ(Q, L):
    # fluctuations (M,J) a Q fixe
    def branchfun(M, J, r0):
        a = J/M; Xi = 1 - a**2/L**2; m = M*Xi**2; q = Q*Xi
        rs = roots_kn(a, m, q, L)
        r = min(rs, key=lambda z: abs(z - r0))
        return pi*(r**2 + a**2)/Xi
    return branchfun

def make_S_MQ(J, L):
    def branchfun(M, Q, r0):
        a = J/M; Xi = 1 - a**2/L**2; m = M*Xi**2; q = Q*Xi
        rs = roots_kn(a, m, q, L)
        r = min(rs, key=lambda z: abs(z - r0))
        return pi*(r**2 + a**2)/Xi
    return branchfun

def RS(branchfun, x0, y0, r0, S0):
    f = lambda x, y: branchfun(x, y, r0)
    d = {}
    for i in range(4):
        for j in range(4 - i):
            if 2 <= i + j <= 3:
                d[(i,j)] = diff(f, (x0, y0), (i, j))
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
    return 2*K*S0

def run_MJ(M, J, Q, L):
    a = J/M; Xi = 1 - a**2/L**2; m = M*Xi**2; q = Q*Xi
    rs = roots_kn(mpf(a), mpf(m), mpf(q), mpf(L))
    bf = make_S_MJ(mpf(Q), mpf(L))
    tv = mpc(0)
    for r0 in rs:
        if abs(r0.imag) > mpf('1e-30'):
            S0 = pi*(r0**2 + a**2)/Xi
            tv += RS(bf, mpf(M), mpf(J), r0, S0)
    return tv.real

def run_MQ_phys(M, Q, J, L):
    a = J/M; Xi = 1 - a**2/L**2; m = M*Xi**2; q = Q*Xi
    rs = roots_kn(mpf(a), mpf(m), mpf(q), mpf(L))
    bf = make_S_MQ(mpf(J), mpf(L))
    tp = mpc(0)
    for r0 in rs:
        if abs(r0.imag) < mpf('1e-30') and r0.real > 0:
            S0 = pi*(r0**2 + a**2)/Xi
            tp += RS(bf, mpf(M), mpf(Q), r0, S0)
    return tp.real

print("A) KN-AdS, fluctuations (M,J) a Q=0.4 fixe (attendu -25/8):")
vals=[]
for L in [300, 1000, 3000]:
    v = run_MJ(1, 0.3, 0.4, L)
    vals.append((L,v)); print(f"  L={L}: virt={nstr(v,14)}")
(L1,v1),(L2,v2) = vals[-2], vals[-1]
print("  extrapolation:", nstr((v2*L2**2 - v1*L1**2)/(L2**2 - L1**2), 15))

print("B) paire physique en frame (M,Q), J=0.3 fixe, L=3000 (constance?):")
for (M,Q) in [(1, 0.4), (1.5, 0.6), (1, 0.7)]:
    p = run_MQ_phys(M, Q, 0.3, 3000)
    print(f"  M={M} Q={Q}: phys={nstr(p,14)}")

print()
print("C) scan de la deformation, frame (M,J), M=1, J=0.3, L: extrapolation 1000/3000")
def extrap(f):
    v1, v2 = f(1000), f(3000)
    return (v2*mpf(3000)**2 - v1*mpf(1000)**2)/(mpf(3000)**2 - mpf(1000)**2)
base = mpf(-25)/8
for Q in [0.2, 0.3, 0.4, 0.5]:
    v = extrap(lambda L: run_MJ(1, 0.3, Q, L))
    dev = v - base
    print(f"  Q={Q}: charge={nstr(v,13)}  dev={nstr(dev,10)}  dev/Q^4={nstr(dev/mpf(Q)**4,10)}  dev/Q^2={nstr(dev/mpf(Q)**2,10)}")
print("D) meme frame, Q=0.4, J varie:")
for J in [0.15, 0.6]:
    v = extrap(lambda L: run_MJ(1, J, 0.4, L))
    print(f"  J={J}: charge={nstr(v,13)}")
print("E) invariance d'echelle: (M,Q,J)=(2,0.8,1.2) vs (1,0.4,0.3):")
v = extrap(lambda L: run_MJ(2, 1.2, 0.8, L))
print(f"  charge={nstr(v,13)}")
print("F) frame (M,Q), J de fond varie (attendu -27/8):")
def run_MQ_virt(M, Q, J, L):
    a = J/M; Xi = 1 - a**2/L**2; m = M*Xi**2; q = Q*Xi
    rs = roots_kn(mpf(a), mpf(m), mpf(q), mpf(L))
    bf = make_S_MQ(mpf(J), mpf(L))
    tv = mpc(0)
    for r0 in rs:
        if abs(r0.imag) > mpf('1e-30'):
            S0 = pi*(r0**2 + a**2)/Xi
            tv += RS(bf, mpf(M), mpf(Q), r0, S0)
    return tv.real
for J in [0.6, 0.9]:
    v = extrap(lambda L: run_MQ_virt(1, 0.4, J, L))
    print(f"  J={J}: charge={nstr(v,13)}")

print()
print("G) test predictif hors grille: Q=0.7, prediction = -25/8 + (0.49/16)(5.49) = -2.95686875")
v = extrap(lambda L: run_MJ(1, 0.3, 0.7, L))
print(f"  mesure: {nstr(v,13)}")
