from mpmath import mp, mpf, mpc, polyroots, nstr
mp.dps = 40

# RN-AdS: Delta(r) = r^4/L^2 + r^2 - 2Mr + Q^2
# exposant de monodromie (scalaire neutre sans masse): alpha_i = omega * r_i^2 / Delta'(r_i)
# (= omega/(4 pi T_i) a normalisation pres)

def rnads(M, Q, L, omega=1):
    rs = polyroots([1/L**2, 0, 1, -2*M, Q**2], maxsteps=300, extraprec=100)
    def Dp(r): return 4*r**3/L**2 + 2*r - 2*M
    alphas = [omega*r**2/Dp(r) for r in rs]
    phys = [a for r, a in zip(rs, alphas) if abs(r.imag) < mpf('1e-25') and r.real > 0]
    virt = [a for r, a in zip(rs, alphas) if abs(r.imag) >= mpf('1e-25')]
    return sum(alphas), sum(phys), sum(virt)

print("RN-AdS, somme des exposants (omega=1):")
for (M,Q,L) in [(1, 0.4, 10), (1, 0.4, 100), (1, 0.4, 1000), (2, 0.7, 500)]:
    tot, ph, vi = rnads(mpf(M), mpf(Q), mpf(L))
    print(f"  M={M} Q={Q} L={L}: total={nstr(tot,8)}  phys={nstr(ph,10)}  virt={nstr(vi,10)}")
print("  (plat: alpha+ + alpha- = 2M omega, verif: 2M =", 2*1, ")")

# Kerr-AdS: alpha_i = [omega(r^2+a^2) - m a(1+r^2/L^2)] / Delta'(r)
def kerrads(M, J, L, omega=1, mm=1):
    a = J/M; Xi = 1 - a**2/L**2; mpar = M*Xi**2
    rs = polyroots([1/L**2, 0, 1 + a**2/L**2, -2*mpar, a**2], maxsteps=300, extraprec=100)
    def Dp(r): return 4*r**3/L**2 + 2*(1 + a**2/L**2)*r - 2*mpar
    alphas = [(omega*(r**2 + a**2) - mm*a*(1 + r**2/L**2))/Dp(r) for r in rs]
    return sum(alphas)

print("Kerr-AdS, somme totale (omega=1, m=1):")
for (M,J,L) in [(1, 0.5, 10), (2, 1.2, 50)]:
    print(f"  M={M} J={J} L={L}: total={nstr(kerrads(mpf(M), mpf(J), mpf(L)),8)}")

# asymptotique des exposants virtuels
print("Asymptotique paire virtuelle RN-AdS (M=1, Q=0.4):")
for L in [100, 1000, 10000]:
    tot, ph, vi = rnads(mpf(1), mpf(0.4), mpf(L))
    print(f"  L={L}: somme virt = {nstr(vi,10)}   somme phys = {nstr(ph,10)}")
