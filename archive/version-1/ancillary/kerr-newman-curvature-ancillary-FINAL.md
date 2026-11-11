# Ancillary file — explicit Kerr-Newman expressions

Companion to *Mirror-Constrained Black Hole Thermodynamics*, Section 7.

All expressions exact. Conventions: Ruppeiner metric g = -Hess(S), coordinates (M,J,Q),

entropies S_pm = pi(2M^2 - Q^2 +/- 2W),  W = sqrt(P),  P = M^4 - M^2 Q^2 - J^2.

Verified against independent exact-assembly numerics to 16 digits at multiple interior points.

## 1. Kerr (closed form, both sheets)

R_pm = 1/(4*pi*M^2) -/+ 1/(2*pi*sqrt(M^4 - J^2))

R_+ + R_- = 1/(2*pi*M^2)

R_+ - R_- = -1/(pi*sqrt(M^4 - J^2))

R_+ * R_- = (3*M^4 + J^2)/(16*pi^2*M^4*(J^2 - M^4))

## 2. Kerr-Newman discriminant and degeneracy polynomials

P = M**4 - M**2*Q**2 - J**2          # extremal branch locus P = 0

D = 4*J**4*M**4 - 8*J**4*M**2*Q**2 + 4*J**4*Q**4 + 12*J**2*M**6*Q**2 - 15*J**2*M**4*Q**4 + 4*J**2*M**2*Q**6 - M**6*Q**6 + M**4*Q**8

## 3. Determinant identity

det(g^+) * det(g^-) = -64*pi**6*M**4*D / P**5

=> curvature singular set:  {M=0}  U  {P=0}  U  {D=0}

D=0 is exactly det(g^+)det(g^-)=0, the metric-degeneracy locus.

## 4. Kerr-Newman mirror-even curvature (closed form)

R_+ + R_-  =  NUM / ( 2*pi*M**2 * D**2 )

NUM =
64*J**8*M**8 - 152*J**8*M**6*Q**2 + 104*J**8*M**4*Q**4 - 8*J**8*M**2*Q**6 - 8*J**8*Q**8 + 168*J**6*M**10*Q**2 - 456*J**6*M**8*Q**4 + 354*J**6*M**6*Q**6 - 54*J**6*M**4*Q**8 - 20*J**6*M**2*Q**10 + 96*J**4*M**14*Q**2 + 176*J**4*M**12*Q**4 - 582*J**4*M**10*Q**6 + 388*J**4*M**8*Q**8 - 45*J**4*M**6*Q**10 - 18*J**4*M**4*Q**12 - 96*J**2*M**16*Q**4 + 232*J**2*M**14*Q**6 - 206*J**2*M**12*Q**8 + 75*J**2*M**10*Q**10 + 2*J**2*M**8*Q**12 - 7*J**2*M**6*Q**14 + 4*M**14*Q**10 - 9*M**12*Q**12 + 6*M**10*Q**14 - M**8*Q**16

## 5. Kerr-Newman mirror-odd sector

(R_+ - R_-)**2  =  ODDNUM / ODDDEN

ODDNUM =
-6400*J**16*M**16 + 24320*J**16*M**14*Q**2 - 47424*J**16*M**12*Q**4 + 67968*J**16*M**10*Q**6 - 73408*J**16*M**8*Q**8 + 58368*J**16*M**6*Q**10 - 35520*J**16*M**4*Q**12 + 15232*J**16*M**2*Q**14 - 3136*J**16*Q**16 - 34560*J**14*M**18*Q**2 + 171904*J**14*M**16*Q**4 - 402880*J**14*M**14*Q**6 + 592672*J**14*M**12*Q**8 - 617696*J**14*M**10*Q**10 + 472288*J**14*M**8*Q**12 - 247584*J**14*M**6*Q**14 + 75264*J**14*M**4*Q**16 - 9408*J**14*M**2*Q**18 - 15360*J**12*M**22*Q**2 - 68672*J**12*M**20*Q**4 + 537664*J**12*M**18*Q**6 - 1389344*J**12*M**16*Q**8 + 2115536*J**12*M**14*Q**10 - 2140068*J**12*M**12*Q**12 + 1423376*J**12*M**10*Q**14 - 577856*J**12*M**8*Q**16 + 125392*J**12*M**6*Q**18 - 10864*J**12*M**4*Q**20 - 26112*J**10*M**24*Q**4 - 84736*J**10*M**22*Q**6 + 923616*J**10*M**20*Q**8 - 2658576*J**10*M**18*Q**10 + 3987224*J**10*M**16*Q**12 - 3525308*J**10*M**14*Q**14 + 1877404*J**10*M**12*Q**16 - 582072*J**10*M**10*Q**18 + 94104*J**10*M**8*Q**20 - 5600*J**10*M**6*Q**22 - 9216*J**8*M**28*Q**4 - 19968*J**8*M**26*Q**6 - 131584*J**8*M**24*Q**8 + 1211232*J**8*M**22*Q**10 - 2992180*J**8*M**20*Q**12 + 3694996*J**8*M**18*Q**14 - 2622705*J**8*M**16*Q**16 + 1104166*J**8*M**14*Q**18 - 263793*J**8*M**12*Q**20 + 29812*J**8*M**10*Q**22 - 764*J**8*M**8*Q**24 + 18432*J**6*M**30*Q**6 + 7680*J**6*M**28*Q**8 - 334336*J**6*M**26*Q**10 + 1009376*J**6*M**24*Q**12 - 1515512*J**6*M**22*Q**14 + 1366816*J**6*M**20*Q**16 - 763938*J**6*M**18*Q**18 + 248142*J**6*M**16*Q**20 - 36986*J**6*M**14*Q**22 - 78*J**6*M**12*Q**24 + 404*J**6*M**10*Q**26 - 9216*J**4*M**32*Q**8 + 53760*J**4*M**30*Q**10 - 143296*J**4*M**28*Q**12 + 226144*J**4*M**26*Q**14 - 224228*J**4*M**24*Q**16 + 133636*J**4*M**22*Q**18 - 36885*J**4*M**20*Q**20 - 5488*J**4*M**18*Q**22 + 7434*J**4*M**16*Q**24 - 1996*J**4*M**14*Q**26 + 135*J**4*M**12*Q**28 + 768*J**2*M**30*Q**14 - 4160*J**2*M**28*Q**16 + 9808*J**2*M**26*Q**18 - 13200*J**2*M**24*Q**20 + 11052*J**2*M**22*Q**22 - 5760*J**2*M**20*Q**24 + 1704*J**2*M**18*Q**26 - 208*J**2*M**16*Q**28 - 4*J**2*M**14*Q**30 - 16*M**28*Q**20 + 80*M**26*Q**22 - 164*M**24*Q**24 + 176*M**22*Q**26 - 104*M**20*Q**28 + 32*M**18*Q**30 - 4*M**16*Q**32

ODDDEN =
4*pi**2*(J**2 - M**4 + M**2*Q**2)*(4*J**4*M**4 - 8*J**4*M**2*Q**2 + 4*J**4*Q**4 + 12*J**2*M**6*Q**2 - 15*J**2*M**4*Q**4 + 4*J**2*M**2*Q**6 - M**6*Q**6 + M**4*Q**8)**4

## 6. LaTeX (numerator and D)

D_LaTeX:
4 J^{4} M^{4} - 8 J^{4} M^{2} Q^{2} + 4 J^{4} Q^{4} + 12 J^{2} M^{6} Q^{2} - 15 J^{2} M^{4} Q^{4} + 4 J^{2} M^{2} Q^{6} - M^{6} Q^{6} + M^{4} Q^{8}

NUM_LaTeX:
64 J^{8} M^{8} - 152 J^{8} M^{6} Q^{2} + 104 J^{8} M^{4} Q^{4} - 8 J^{8} M^{2} Q^{6} - 8 J^{8} Q^{8} + 168 J^{6} M^{10} Q^{2} - 456 J^{6} M^{8} Q^{4} + 354 J^{6} M^{6} Q^{6} - 54 J^{6} M^{4} Q^{8} - 20 J^{6} M^{2} Q^{10} + 96 J^{4} M^{14} Q^{2} + 176 J^{4} M^{12} Q^{4} - 582 J^{4} M^{10} Q^{6} + 388 J^{4} M^{8} Q^{8} - 45 J^{4} M^{6} Q^{10} - 18 J^{4} M^{4} Q^{12} - 96 J^{2} M^{16} Q^{4} + 232 J^{2} M^{14} Q^{6} - 206 J^{2} M^{12} Q^{8} + 75 J^{2} M^{10} Q^{10} + 2 J^{2} M^{8} Q^{12} - 7 J^{2} M^{6} Q^{14} + 4 M^{14} Q^{10} - 9 M^{12} Q^{12} + 6 M^{10} Q^{14} - M^{8} Q^{16}

## 7. Dimensionless two-horizon invariants (Section 7.8)

Dimensionless curvature Rbar = R*S. Define the diagonal and cross combinations
trace = R_+ S_+ + R_- S_-
cross = R_+ S_- + R_- S_+
Computed in the quadratic extension Q(M,J,Q)[W]/(W^2 - P), where R_pm = p +/- q W with
p, q rational; then trace = 2*pi*p*(2M^2 - Q^2) + 4*pi*q*P and cross = 2*pi*p*(2M^2 - Q^2) - 4*pi*q*P.
Both reduce to N/(2*M^2*D^2) with the same D as in Section 2.
Verified against independent high-precision Ricci evaluation (mpmath, dps=50) at five interior
points to 48 digits.

### Closed forms (exact)

trace = N_trace / (2*M^2*D^2),  N_trace =
-32*J**8*M**10 - 64*J**8*M**8*Q**2 + 56*J**8*M**6*Q**4 + 152*J**8*M**4*Q**6 - 120*J**8*M**2*Q**8 + 8*J**8*Q**10 - 96*J**6*M**12*Q**2 + 248*J**6*M**10*Q**4 - 528*J**6*M**8*Q**6 + 474*J**6*M**6*Q**8 - 154*J**6*M**4*Q**10 + 20*J**6*M**2*Q**12 - 384*J**4*M**14*Q**4 + 944*J**4*M**12*Q**6 - 700*J**4*M**10*Q**8 + 192*J**4*M**8*Q**10 - 59*J**4*M**6*Q**12 + 18*J**4*M**4*Q**14 + 24*J**2*M**14*Q**8 - 58*J**2*M**12*Q**10 + 41*J**2*M**10*Q**12 - 14*J**2*M**8*Q**14 + 7*J**2*M**6*Q**16 - 2*M**14*Q**12 + 5*M**12*Q**14 - 4*M**10*Q**16 + M**8*Q**18

cross = N_cross / (2*M^2*D^2),  N_cross =
288*J**8*M**10 - 672*J**8*M**8*Q**2 + 664*J**8*M**6*Q**4 - 392*J**8*M**4*Q**6 + 104*J**8*M**2*Q**8 + 8*J**8*Q**10 + 768*J**6*M**12*Q**2 - 2408*J**6*M**10*Q**4 + 2856*J**6*M**8*Q**6 - 1398*J**6*M**6*Q**8 + 182*J**6*M**4*Q**10 + 20*J**6*M**2*Q**12 + 384*J**4*M**16*Q**2 + 896*J**4*M**14*Q**4 - 3624*J**4*M**12*Q**6 + 3416*J**4*M**10*Q**8 - 1148*J**4*M**8*Q**10 + 77*J**4*M**6*Q**12 + 18*J**4*M**4*Q**14 - 384*J**2*M**18*Q**4 + 1120*J**2*M**16*Q**6 - 1312*J**2*M**14*Q**8 + 770*J**2*M**12*Q**10 - 183*J**2*M**10*Q**12 - 18*J**2*M**8*Q**14 + 7*J**2*M**6*Q**16 + 16*M**16*Q**10 - 42*M**14*Q**12 + 37*M**12*Q**14 - 12*M**10*Q**16 + M**8*Q**18

### Special values and limits

Kerr (2D, M,J):                 trace = -1,  cross = 3
Reissner-Nordstrom (M,Q, flat): trace =  0,  cross = 0
Kerr-Newman at Q=0 (3D):        trace = -1,  cross = 9
(At Q=0: N_trace -> -32 J^8 M^10, 2 M^2 D^2 -> 32 J^8 M^10, ratio -1;
N_cross -> 288 J^8 M^10, ratio 9.)

The diagonal value -1 is robust to the dimension of the parameter manifold; the cross is not
(3 in two dimensions, 9 in three). RN is flat, so both vanish there.

### Charge breaking of the diagonal integer

trace = -1 + c(M,J) Q^2 + O(Q^4),   c(M,J) = 3 (M^4 - 2 J^2) / (M^2 J^2)

- diverges as J -> 0 (non-uniform double limit with the flat RN value 0)
- vanishes / changes sign at J = M^2/sqrt(2), i.e. where sqrt(M^4 - J^2) = J (a/M = 1/sqrt2)
- verified to 28 digits at independent (M,J) points.

## 8. Spin-angle parametrization (Kerr) and complex continuation (Section 7.9)

Set sin(theta) = a/M = J/M^2,  theta in [0, pi/2] physical, extremal at theta = pi/2.
Then W = sqrt(M^4 - J^2) = M^2 cos(theta), and:

S+ = 4 pi M^2 cos^2(theta/2),   S- = 4 pi M^2 sin^2(theta/2)
R+- = (1/(4 pi M^2)) (1 -/+ 2 sec theta)
R+ S+ = -1/2 + (1/2) cos theta - sec theta
R- S- = -1/2 - (1/2) cos theta + sec theta
=> R+S+ + R-S- = -1   (twice the deck-even constant -1/2),  R+S- + R-S+ = 3

Deck involution = reflection theta -> pi - theta about the extremal angle.

Past extremality (J > M^2): theta = pi/2 + i psi, and the two entropies become complex conjugates,
S+- = 2 pi M^2 (1 -/+ i sinh psi),
the two real horizons merging at theta=pi/2 and continuing as a conjugate pair. The diagonal
invariant stays real and equal to -1 across the branch point (it is a deck-symmetric analytic
invariant). Charge coefficient in angle: c = 3 cos(2 theta) / (M^2 sin^2 theta), sign change at
theta = pi/4.

## 9. Cosmological-constant breaking of the diagonal integer (Section 6)

Kerr-AdS (Gibbons-Perry-Pope): eps = 1/l^2 = -Lambda/3, Xi = 1 - a^2 eps,
m = (r^2+a^2)(1+eps r^2)/(2r),  E = m/Xi^2,  J = a m/Xi^2 = a E  (so a = J/M),
S = pi (r^2 + a^2)/Xi.
Building S+-(M,J;eps) to first order in eps (perturbing the horizon radii r+- about their Kerr
values, a = J/M fixed) and recomputing the 2D Ruppeiner curvature trace gives

R+S+ + R-S-  =  -1  +  c_eps * eps  +  O(eps^2),     c_eps = 4 J^2 (J^2 - 6 M^4) / M^6

Verified against high-precision Richardson-extrapolated numerics to ~40 digits at independent
(M,J) points. Features:

- c_eps -> 0 as J -> 0 (vanishes; the Schwarzschild-AdS limit is smooth),
  in contrast with the charge coefficient 3(M^4-2J^2)/(M^2J^2) which DIVERGES as J->0.
- sub-extremal J <= M^2 => J^2 - 6M^4 < 0 => c_eps < 0 throughout: no sign change.
  AdS (eps>0, Lambda<0) pushes the invariant uniformly below -1; dS pushes it above.
- construction keeps M as energy at fixed Lambda (non-extended). The fully extended
  (enthalpy, varying Lambda, with V-P pair) version is left open.

## 10. Kerr-AdS thermodynamic volume and the degeneracy of the extended state space (Section 6)

Derived self-consistently as V = dM/dP|_{S,J} from the GPP thermodynamics (no external formula used):

V = 2 pi l^2 (a^2+r^2)(a^2 l^2 - a^2 r^2 + 2 l^2 r^2) / (3 r (a-l)^2 (a+l)^2)

Schwarzschild-AdS check (a->0):  V = 4 pi r^3 / 3   (exact)
Flat limit (l->oo):              V -> 2 pi (a^2+r^2)(a^2+2 r^2) / (3 r)

The flat-limit volume is a function of (M,J) alone (r^2+a^2 = 2 M r, a = J/M), so the
pressure-conjugate volume is NOT independent at zero pressure. Concretely, the Jacobian of the
extended coordinates collapses:

det d(M,J,V)/d(r,a,l)  =  [ 2 pi (a^2+r^2)^4 / r^2 ] * (1/l^3)  +  O(1/l^5)   as l -> oo

i.e. it vanishes as l^{-3}. The 3D extended state space pinches onto the 2D (M,J) surface in the
flat limit. Consequence: the integer R+S+ + R-S- = -1 is a property of that boundary slice; charge
and Lambda deform it WITHIN the flat (M,J) geometry (sections 7.8 / 6), while the enthalpic
direction leaves that geometry entirely. Whether the non-degenerate 3D extended curvature (fixed
nonzero P) has a clean invariant of its own is left open.

## 11. The integer as the shadow of product universality (Section 7.11)

Test family (degree-2 homogeneous, deck-symmetric):  S_pm = A M^2 +/- B sqrt(M^4 - J^2).
Kerr is A = B = 2 pi.

Diagonal R+S+ + R-S- is constant (= -1) IFF A = B.  For A != B it is a genuine function of
(M,J); e.g. A=1,B=2 gives  -(7J^4+3J^2M^4+18M^8)/(J^2+3M^4)^2 , and no linear combination of
diagonal and cross is constant. (Checked A=B=1 -> diagonal -1, cross 3, confirming the machinery.)

Entropy product of the family:
S+ S-  =  (A^2 - B^2) M^4  +  B^2 J^2
-> mass-independent IFF A = B, where S+ S- = A^2 J^2  (Ansorg-Hennig form).

CONCLUSION: the diagonal integer appears exactly when the entropy product is mass-independent.
The integer is the differential-geometric encoding of Ansorg-Hennig universality.

Kerr-AdS confirmation (eps = -Lambda/3), product to O(eps):
S+ S-  =  4 pi^2 J^2 ( 1 - 8 eps M^2 )  +  O(eps^2)
The O(eps) term is mass-dependent (d/dM = -64 pi^2 J^2 M != 0): AdS breaks product universality
at the SAME order at which the diagonal integer breaks (coeff c_eps = 4 J^2 (J^2 - 6 M^4)/M^6).
Product universality and the integer break together, by the same deformation.

Charge is different: KN product pi^2(Q^4 + 4 J^2) stays mass-independent, yet the 3D integer
still moves (coeff c_Q) through curvature couplings to the charge direction. So Lambda breaks the
integer via product-universality failure in the (M,J) plane; charge breaks it via the extra
dimension. This is the geometric face of the divergent (c_Q, J->0) vs vanishing (c_eps, J->0)
static-limit contrast.

## 12. The product as CFT level-matching; what “conserved” means (thread on causal structure)

Established (Larsen 1997; Cvetic et al; Chen-Liu-Zhang JHEP 11 (2012) 017):
S_pm = 2 pi ( sqrt(N_L) +/- sqrt(N_R) ),   product  S+ S- = 4 pi^2 (N_L - N_R),
with N_L, N_R the left/right levels of a dual 2D CFT; N_L - N_R is fixed by the charges (level matching).

Verified for our cases:
Kerr:          N_L = M^4,               N_R = M^4 - J^2,          N_L-N_R = J^2,        product 4 pi^2 J^2
Kerr-Newman:   N_L = M^4-M^2Q^2+Q^4/4,  N_R = M^4-M^2Q^2-J^2,     N_L-N_R = J^2+Q^4/4,  product pi^2(4J^2+Q^4)

Surface-gravity matching (computed): for RN, Kerr, KN,
T+ S+ = T- S- = (r+ - r-)/4   (magnitudes; with kappa_- < 0 the signed sum vanishes).
This is the Chen-Liu-Zhang condition  T+S+ = T-S-  <=>  product mass-independent  <=>  c_L = c_R.

So the diagonal curvature integer sits in ONE family, four faces:
product mass-independence  <=>  T+S+ = T-S-  <=>  c_L = c_R  <=>  N_L - N_R quantized.
The integer is its Hessian-geometry face.

Honest scope on the causal question: the “conserved” quantity is the microscopic level difference
N_L - N_R (level matching in the dual CFT), fixed by the charges. It is NOT a flux across the Cauchy
horizon. The thermodynamic two-sheet cover and the causal two-sheet structure of the maximal extension
share the inner horizon but are distinct objects; the integer carries no claim about the interior universe.

## 13. Arithmetic structure of the state space (CM elliptic curve) – verified facts

State curve  W^2 = M^4 - J^2  <->  Weierstrass  eta^2 = X^3 + 4 J^2 X   (j = 1728, CM by Z[i]).
Maps:  X = 2(W+M^2),  eta = 4 M (M^2+W) ;   inverse  M = eta/(2X),  W = X/2 - M^2.

Exact arithmetic identity of each physical operation (all verified):

- mirror  (inner<->outer, W->-W)   =  P |-> T - P ,  reflection through the 2-torsion T=(0,0)
  (T is the J=0 / Schwarzschild reference half-period).  = tau_T o [-1].
- mass conjugation  M -> -M          =  [-1]  (inversion  P -> -P).
- Gaussian multiplication [i]:(X,eta)->(-X, i eta), order 4,  [i]^2 = [-1].
  On physical variables:  [i]:(M,W) -> (-i M, -W).  Quarter-turn of the mass + sheet swap.
  Sends real states to complex states -> this IS the past-extremal complex continuation (Sec 7.9).
- group law closes on states of fixed J (M1,M2 -> M3 on the curve) but no physical meaning found.

## 14. Gamma(1/4) bridge: Ruppeiner distance to extremality = CM period

Outer-sheet induced metric on the fixed-M line:  g_JJ = -d^2 S+/dJ^2 = 2 pi M^4 / (M^4 - J^2)^{3/2}.
Proper (Ruppeiner) length, Schwarzschild (J=0) to extremal (J=M^2):

```
    L  =  integral_0^{M^2} sqrt(g_JJ) dJ  =  M * Gamma(1/4)^2 / 2       (verified 15 digits)
```

This is the lemniscate constant.  The real period of the CM curve is Omega = Gamma(1/4)^2 / sqrt(2 pi),
so L = M * Omega * sqrt(2 pi)/2 : the SAME Gamma(1/4)^2 constant. Not a coincidence – both are period
integrals of the same algebraic function W = sqrt(M^4 - J^2), whose curve is the j=1728 CM curve.

Inner sheet:  g_JJ = -2 pi M^4/(M^4-J^2)^{3/2}  (opposite sign) -> inner-horizon distance = i x outer.
The two horizons’ proper distances differ by exactly i, the Gaussian unit of the CM ring Z[i].

Status: verified structure and a verified physical fingerprint (Gamma(1/4) in the distance; distance to
extremality is FINITE). It does NOT explain the curvature integers (-1,3), which live at a different order
(j-invariant deviates at O(Q^4), integer at O(Q^2)). Modular-forms / BPS connection remains conjectural.
Novelty search still required.

## 15. Prove-or-kill test on a new family: Reissner-Nordstrom-de Sitter (THREE horizons)

Horizon quartic (l^2 = 3/Lambda):  r^4 - l^2 r^2 + 2 M l^2 r - Q^2 l^2 = 0.
Four roots: r_- (Cauchy), r_+ (event), r_c (cosmological), r_o (virtual, negative). Vieta:
e1 = 0,  e2 = -l^2,  e3 = -2 M l^2 (carries MASS = quantity),  e4 = -Q^2 l^2 (mass-free = QUALITY).

PROVEN: the sorting principle generalizes to three horizons.
Product over ALL FOUR entropies  Prod pi r_i^2 = pi^4 (e4)^2 = pi^4 Q^4 l^4  -> MASS-INDEPENDENT.
Product over the 3 PHYSICAL horizons alone is mass-DEPENDENT (needs the virtual root r_o).
This reproduces the Visser/Cvetic de Sitter result -> strong consistency check.

TESTED (novel, never computed): multi-horizon Ruppeiner curvature sum Sum_i R_i S_i (fixed l, (M,Q) space).
Exact local implicit-Taylor computation of each horizon’s curvature:
(M,Q)=(0.15,0.10): sum over 4 roots = -3.648 ; over 3 physical = -2.137
(M,Q)=(0.17,0.08): sum over 4 roots = -3.651 ; over 3 physical = -2.149
NOT constant -> NO clean multi-horizon curvature integer.

Interpretation (careful, not a falsification): RN-dS has Lambda != 0 by construction, and Lambda is already
known to break the two-horizon integer; 4D cannot host three horizons at Lambda=0. So the “3-horizon” and
“Lambda” effects are confounded. The result CONFIRMS the framework’s layered structure: the algebraic
sorting (quantity/quality) is robust and survives; the geometric curvature integer requires Lambda=0 and
does not survive the de Sitter setting. Robust layer stays, fragile layer breaks, as predicted.

LEDGER UPDATE:
PROVEN this step: quantity/quality sorting holds beyond Kerr-Newman (3-horizon de Sitter).
CONSTRAINED this step: the curvature-integer layer is specific to the clean Lambda=0 rotating case;
it does not extend to the multi-horizon de Sitter setting.
Cleanly isolating “multi-horizon” from “Lambda” would need a Lambda=0 multi-horizon family,
which 4D Einstein-Maxwell does not provide (would require higher-D or higher-derivative gravity).

## 16. Cross-family proof of (i)<=>(vi): integer = -1  IFF  entropy product universal

New computations (never done before): the two-horizon diagonal invariant R+S+ + R-S- across families.
High-precision numerics (dps 22-30), exact per the digits shown.

Kerr (4D)                : -1        [product 4 pi^2 J^2, universal]
Kerr-Newman, Q=0         : -1        [universal]
KERR-SEN, all Q (Q=0,1,2): -1        [product 4 pi^2 J^2, charge-INDEPENDENT] <- decisive: charge does
NOT break it, opposite to Kerr-Newman, and the only difference is
that the Kerr-Sen product has no charge dependence.
Kerr-Newman, Q!=0        : broken (-1 + c_Q Q^2 + …) [product 4J^2+Q^4, charge-dependent]
MYERS-PERRY 5D           : -1        [product ~ Ja Jb, universal]
MYERS-PERRY 6D           : NOT -1, non-constant (-3.87, -3.08, -3.07 at sample points)
[product NON-universal for d>=6, per Chen-Liu-Zhang]

CONCLUSION: R+S+ + R-S- = -1 (mass-independent constant)  <=>  entropy product is mass-independent.
Verified across TWO theories (Einstein-Maxwell, heterotic-string Kerr-Sen) and THREE dimensions (4,5,6),
in BOTH directions (universal->integer; non-universal->broken). Kerr-Sen (charge-robust) vs Kerr-Newman
(charge-broken) is the sharpest single test: same charge parameter, opposite fate, decided entirely by
product universality.

LEDGER:
PROVEN (strong, cross-family): the diagonal integer <=> entropy-product universality. Face (i)<=>(vi)
of the framework now holds far beyond its original Kerr-Newman domain.
Kerr-Sen integer and Myers-Perry (5D,6D) two-horizon integers are, to our knowledge, new.
(Novelty search still a precondition before any publication claim.)

## 17. Context beta: local vs context-complete invariants (new lens, proven core)

Reframes the breaking of universality in a cosmological background as an artefact of
incomplete (local-only) accounting. The known all-horizons universality (Visser;
Cvetic-Gibbons-Kubiznak-Pope) is decomposed into a “local invariant = universal / context-factor”.

RN-de Sitter (quartic r^4 - l^2 r^2 + 2M l^2 r - Q^2 l^2 = 0; roots r_-,r_+,r_c physical, r_o virtual<0):
S_all  = pi^4 (r_- r_+ r_c r_o)^2 = pi^4 Q^4 l^4                 [MASS-FREE, context-complete]
S_phys = pi^3 (r_- r_+ r_c)^2     = pi^3 Q^4 l^4 / (Sigma_phys)^2 [MASS-DEPENDENT, local]
Sigma_phys = r_-+r_++r_c = -r_o  is the CONTEXT BETA (carries the mass).
Numerically verified (Q=1,l=10): S_all/pi^4 = 10000 exactly for all M; S_phys/pi^3 moves
(80.55, 79.51, 78.51, 77.55, 76.61) as M runs 1.3..1.7; identity Q^4 l^4/Sigma^2=(r-r+rc)^2 exact.
Interpretation: the universal invariant Q^4 l^4 is present but “divided by the box”. Including the
cosmological/virtual horizon (the boundary of the universe) restores mass-independence.

BOUNDARY (proven): rotation is NOT context-completable.
Kerr-dS all-horizons product of (r_i^2+a^2) = 4 M^2 L^4 a^2  (mass-dependent, prop. M^2).
The frame-dragging factor keeps an irreducible beta; only the CHARGE sector is hedgeable.

TWO LAYERS respond oppositely to context:

- algebraic quality (entropy product): context-completable (charge sector). PROVEN.
- geometric curvature integer: intrinsically flat-space (breaks under Lambda of either sign, cf. Kerr-AdS
  -1 + c_eps eps). Whether cosmological horizons restore it is OPEN; RN-dS Sum R_i S_i (a Ruppeiner-flat
  case, non-decisive) did not show restoration. Honest status: local object, not yet context-restored.

NOVELTY: all-horizons universality is established literature. New here is (a) the beta-decomposition lens
local=universal/context, (b) the charge/rotation asymmetry in context-completability, (c) the contrast
between the completable product and the intrinsically-local integer. Companion-note framing; not a claim.

## 18. Is the breaking noise or structure? Regression / dispersion test (answer: structure)

Tested whether the FRAGILE layer (curvature integer, when broken) carries irreducible dispersion.

Kerr-AdS breaking vs eps (fixed M=2,J=1.3):
small-eps linear fit: slope -> derived beta c_eps = 4 J^2 (J^2-6M^4)/M^6, R^2=0.9993.
wider range, polynomial order vs R^2: 0.816, 0.99999, 0.9999998, 0.99999999, 1.0000000000 (order 5).
=> residual -> machine zero. Breaking is an EXACT ANALYTIC function of eps. No noise floor.

Myers-Perry 6D scaling collapse:
trace invariant under (M,Ja,Jb)->(lam M, lam^2 Ja, lam^2 Jb): at fixed (ja,jb)=(Ja/M^2,Jb/M^2)
trace = -3.86964579 to 10 digits for lam=1.0,1.3,0.75. Scattered raw values (-3.87,-3.08,-3.07)
are F(ja,jb) sampled at different dimensionless points. Deterministic 2D surface, zero noise.

UNIFIED FINDING: no invariant studied contains irreducible randomness. Apparent volatility is always
deterministic structure viewed through too few variables:

- RN-dS product: dispersion = omitted context (Q,l); full context -> R^2=1 (betas 4,4,-2).
- Kerr-AdS integer: residual = higher-order in eps; polynomial -> R^2=1.
- MP-6D integer: dispersion = wrong scaling; dimensionless ratios -> exact collapse.
  The beta is exact; dispersion = missing context; complete context -> machine-zero residual.
  Genuine probability lives only in the Ruppeiner substrate (metric = covariance of thermodynamic
  fluctuations). “Volatility” here is signal to decompose, not noise to hedge; the perfect hedge = zero residual.

## 19. General context beta: Vieta carrier identity across dimensions (proven)

Generalized the RN-dS “context beta” to d-dim RN-de Sitter (charged static). Monic horizon polynomial:
r^(2(d-3)+2) - l^2 r^(2(d-3)) + mu l^2 r^(d-3) - q^2 l^2 = 0.  Entropy S ~ r^(d-2).

CARRIER IDENTITY (exact, all d): Prod_phys r  x  Prod_virt r  =  Prod_all r  =  mass-free (= q^2 l^2 for q=.5,l=10 -> 25.0).
Verified d=4,5,6,7 at mu=1.0,1.1,1.2: product = 25.0 exactly, physical and virtual products move inversely.
=> the product of the VIRTUAL (unphysical) roots is ALWAYS the carrier of any mass-dependence.

DIMENSIONAL PATTERN (whether Prod_phys itself carries mass):
d=4: varies (2.386->2.367)  -> context beta present
d=5: EXACTLY 5.0 (=q l), variation ~1e-31 -> MASS-FREE, self-completing
d=6: varies -> beta present
d=7: varies -> beta present
Unique d=5: reduced polynomial in x=r^2 is cubic (degree 3) = number of physical horizons, so NO virtual
x-root; the r-virtual roots are just mirrors -sqrt(x) with mass-free product. All other d retain genuine
virtual roots carrying mass.

TWO REFINEMENTS:
(a) The 4D beta is a PURE Lambda effect: flat RN has r+ r- = Q^2 (mass-free, 2 horizons); the cosmological
horizon introduces the virtual root that carries the mass. The box CREATES the local imbalance it then
completes.
(b) Resonance with Myers-Perry (d=5 universal, d=6 breaks): charge and rotation are distinct mechanisms, but
d=5 emerges favorable to universality by both independent routes. Noted, not over-interpreted.

All-horizons invariant (context-complete quality) exists whenever there is a charge (constant term = charge),
robust across all d. Boundary (rotation, no-charge) unchanged from section 17.

-----

## 20. Virtual sheet curvature charges: protocol and exact results (Section 10)

Companion to Section 10 of the main paper. All conventions as in Sections 1 through 7: Ruppeiner metric g = −Hess S(coordinates), sign calibrated so that the Kerr two-horizon diagonal sum equals −1 exactly (verified symbolically with the Brioschi formula, both sign choices tested, σ = −1 selected).

### 20.1 Families and branch functions

RN-AdS: P(r) = r⁴/ℓ² + r² − 2Mr + Q², S = πr², coordinates (M,Q).

Kerr-AdS and KN-AdS: with a = J/M (exact, since J = Ma follows from M = m/Ξ², J = ma/Ξ²), Ξ = 1 − a²/ℓ², m = MΞ², electric parameter q = QΞ:

P(r) = r⁴/ℓ² + (1 + a²/ℓ²) r² − 2mr + (a² + q²), S = π(r² + a²)/Ξ.

Frames: electric (M,Q) at fixed J, angular (M,J) at fixed Q.

At fixed ℓ each root r_i of the quartic defines a branch entropy S_i over the fluctuation plane. Two roots are the physical horizons; the complex conjugate pair are the virtual sheets. Branch tracking by nearest-root continuation.

### 20.2 Numerical protocol

mpmath, 40 to 50 decimal digits. Partial derivatives of the branch entropy through third order by mp.diff on the tracked branch. Curvature by the Brioschi formula; for a Hessian metric the second-derivative entry of the first Brioschi determinant vanishes identically, so third-order partials of S suffice. Flat limit by Richardson extrapolation in 1/ℓ² using ℓ = 1000 and 3000 (checked against ℓ = 100, 300).

Pipeline validation: physical pair in the flat limit gives 0 for RN (both branches Ruppeiner-flat, verified symbolically) and −1.0000006 at ℓ = 3000 for Kerr, converging to −1.

### 20.3 Refutation of the four-root trace conjecture

RN-AdS, sum of R_i S_i over all four roots (real to working precision at every point):

| (M, Q, ℓ) | physical pair | four-root trace |
|---|---|---|
| (1, 0.5, 10) | +0.0655 | −3.2110 |
| (1, 0.5, 5) | +0.8155 | −2.2787 |
| (1, 0.8, 10) | +0.1537 | −3.1353 |
| (2, 0.7, 8) | +2.2733 | −0.7285 |
| (1, 0.5, 100) | +0.000267 | −3.3736 |

Not constant. Conjecture 10.2 refuted.

### 20.4 Virtual pair, numerical flat limits

RN-AdS, virtual pair, Richardson extrapolation:

| (M, Q) | extrapolated | target −27/8 = −3.375 |
|---|---|---|
| (1, 0.5) | −3.37499999998 | match |
| (3, 1.2) | −3.37499999805 | match |
| (0.5, 0.4) | −3.375000000 | match |

Kerr-AdS, virtual pair: (M,J) = (1, 0.5) and (2, 1.5) both extrapolate to −3.1249999995, matching −25/8.

KN-AdS, electric frame (M,Q) = (1, 0.4) at fixed J = 0.3: extrapolates to −3.37499999998. Background J = 0.6 and 0.9: −3.374999999978 and −3.374999999981. The electric charge is insensitive to background rotation.

KN-AdS, angular frame, M = 1, J = 0.3, deviations dev = charge + 25/8:

| Q | charge | dev | dev/q² |
|---|---|---|---|
| 0.2 | −3.11240000 | 0.01260000 | 0.31500 |
| 0.3 | −3.09636875 | 0.02863125 | 0.31813 |
| 0.4 | −3.07340000 | 0.05160000 | 0.32250 |
| 0.5 | −3.04296875 | 0.08203125 | 0.32813 |

dev/q² is exactly linear in q² with slope 1/16 and intercept 5/16, giving dev = (5/16)q² + (1/16)q⁴. Predictive test out of grid: q = 0.7 predicts −2.95686875, measured −2.95686874998 (eleven digits). J-independence: J = 0.15 and 0.6 at Q = 0.4 both give −3.073399999. Scale invariance: (M,Q,J) = (2, 0.8, 1.2) reproduces (1, 0.4, 0.3) exactly.

Physical pair non-constancy, electric frame at fixed J = 0.3, ℓ = 3000: values 0.40363, 0.34444, 0.50420 at (M,Q) = (1, 0.4), (1.5, 0.6), (1, 0.7). The virtual sheets are strictly more rigid than the physical sheets.

### 20.5 Exact Laurent-series protocol

The flat limits were then established exactly. Variable x = 1/ℓ. The virtual branch expands as

r_v = i/x − M + i(3M² − Q²) x/2 + O(x²)

(RN-AdS; the KN case is analogous with m replacing M at leading order). Method: (i) implicit differentiation of P(r(u,v), u, v) = 0 through third order, solving order by order for the branch partials as rational functions of (r, u, v, x), with the substitution of lower-order solutions performed after isolating the target derivative to avoid nested-derivative corruption; (ii) the branch root as a truncated Laurent series in x with Gaussian-rational coefficients, refined by Newton iteration in series arithmetic (five iterations from seed i/x − M); (iii) exact evaluation of all S-partials and the Brioschi formula in truncated Laurent-series arithmetic; (iv) the flat-limit charge is the x⁰ coefficient of R·S, and all negative-power coefficients are checked to vanish identically.

Truncation order NMAX = 8; all arithmetic exact over Q(i).

### 20.6 Exact results

RN-AdS, per virtual sheet, at (M,Q) = (1, 1/2) and (2, 1/3): R·S = −27/16 exactly, real, all negative powers identically zero. Pair charge −27/8.

KN-AdS, angular frame (M,J) = (1, 1/3), pair charges at rational Q:

| Q | exact charge | equals −25/8 + 5Q²/16 + Q⁴/16 |
|---|---|---|
| 0 | −25/8 | yes |
| 1/4 | −12719/4096 | yes |
| 1/2 | −779/256 | yes |
| 3/4 | −11999/4096 | yes |
| 1 | −11/4 | yes |

Five exact points determine the quartic polynomial uniquely:

charge|_(M,J) = −25/8 + (5/16)(Q/M)² + (1/16)(Q/M)⁴ = (q² + 10)(q² − 5)/16, q = Q/M.

KN-AdS, electric frame, background rotation: (J, M, Q) = (1/2, 1, 2/5) and (1/3, 2, 1/2) both give exactly −27/8.

### 20.7 Summary of exact constants

Per sheet: electric frame −27/16 = −3³/16, angular frame (uncharged background) −25/16 = −5²/16. All charges and deformation coefficients quantized in sixteenths per sheet. Scaling-weight conjecture (two points, falsifiable): pair charge = −29/8 + w/4 with w the scaling weight of the second fluctuation coordinate. Predicted tests: Kerr-Sen electric frame −27/8; Myers-Perry d = 5 interpolation at fractional weight.


## 21. Closed-form theorems, general split, monodromy closure (Sections 10.5-10.9)

**Symbolic proofs of the virtual charges.** Laurent-series arithmetic over the Gaussian rationals (truncation order 8), implicit branch derivatives to third order, Brioschi with the Hessian cancellation, Newton refinement of the branch series from seed i/x - M. Electric frame, M = 1 WLOG, Q symbolic: per-sheet R S = -27/16, negative powers identically zero. Angular frame, M = 1, J = 1/3 (J-independence proven exactly at multiple rational points), Q symbolic: per-sheet R S = -25/16 + 5Q^2/32 + Q^4/32, real. Rational-point checks: electric at (M,Q) = (1,1/2), (2,1/3); angular pair charges at Q = 0, 1/4, 1/2, 3/4, 1 equal to -25/8, -12719/4096, -779/256, -11999/4096, -11/4, matching the polynomial exactly (five points determine the quartic).

**General deck-symmetric theorem.** For S(+/-) = 2 pi (W(M) +/- sqrt(W^2 - J^2)), W arbitrary (W''' kept free): sum = -1 identically; split D = (3 - Sigma_W) nu / 2 - 1/nu with Sigma_W = W'W'''/W''^2 + W'^2/(W W''). Power law W = m^p gives Sigma_W = 2 for all p (Kerr p = 2, equal-spin MP5D p = 3/2 via S(+/-) proportional to m^{3/2} +/- sqrt(m^3 - 4 j^2) in linear coordinates (m, j) = (mu, mu a)). Kerr-Sen: W = M^2 - Q^2/2, Sigma_W = 2/(1 - q^2/2); deviation matches numerics to six digits at (M,J,Q) = (1, 0.3, 0.6) (0.204293 vs 0.204294 measured).

**Cross-validations against published closed forms.** (i) Kerr branch products against Aman-Bengtsson-Pidokrajt 2015 Eqs. (35), (37) in their (t,x) coordinates: outer branch to machine precision at four beta points, inner branch identically zero difference, and the -1 follows from their formulas alone. (ii) Equal-spin MP5D outer branch against Bravetti-Nettel-Quevedo R = -S(S^2+12J^2)/(S^4-16J^4), entropy convention s = S_std/pi: agreement to forty digits at three states, with the two-branch sum = -1 at each, independently reconfirming the Section 8 result. (iii) The Kerr-Sen sum = -1 reconfirmed numerically at three charge values, now a corollary of the general theorem.

**Monodromy closure.** alpha_i = omega r_i^2 / Delta'(r_i) (RN-AdS) and [omega(r_i^2+a^2) - m a(1+r_i^2/l^2)]/Delta'(r_i) (Kerr-AdS): total over the four roots zero to forty digits for arbitrary omega, m (residue theorem; equivalently alpha_i = (omega d_M + m d_J) S_i / 4 pi, so closure = entropy-sum universality by the Zhang-Gao criterion). Flat-limit split: physical pair -> 2 M omega, virtual pair -> -2 M omega exactly (verified at L = 100, 1000, 10000), identifying the virtual pair with the flat irregular-point (Stokes) content; the confluence r_v = +/- i l - M -> infinity as l -> infinity manufactures the irregular singularity.

**Rotation non-completability recheck.** Kerr-dS complete-root product Prod (r_i^2 + a^2) = P(ia) P(-ia) = 4 M^2 a^2 L^4, symbolic, reverified 2026-07-02.
