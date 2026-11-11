# Section 10 addendum. Closed-form theorems, the branch-level level map, and frame sensitivity

*Companion to Section 10; results obtained while attacking the analytic derivation. Merge or keep as 10.7 through 10.9.*

## 10.7 Closed-form proofs of the virtual charges

The virtual charges of 10.3 and 10.4 are now symbolic theorems, not rational-point verifications. Carrying the Laurent-series machinery of 10.4 with the parameters left symbolic (mass set to one without loss of generality, since the flat-limit charge is dimensionless and scale invariance was verified exactly) gives, for the electric frame with generic symbolic Q, per virtual sheet:

$$R_v S_v = -\frac{27}{16}, \qquad \text{all negative powers of } 1/\ell \text{ vanishing identically}. \tag{10.8}$$

For the angular frame with generic symbolic Q (rotation fixed at a rational value, J-independence having been proven exactly at multiple points), per virtual sheet:

$$R_v S_v = -\frac{25}{16} + \frac{5}{32}\,q^2 + \frac{1}{32}\,q^4, \qquad q = \frac{Q}{M}, \tag{10.9}$$

a real number, so each sheet of the conjugate pair carries exactly half the pair charge. The generic series for the virtual branch, derived along the way, reads r_v = iℓ − M + i(3M² − Q²)/(2ℓ) + 2M(2M² − Q²)/ℓ² + O(ℓ⁻³).

## 10.8 The branch-level level map (open item 4)

For Kerr, the individual products R±S± admit an exact closed form. With ν ≡ √(N_R/N_L) = √(1 − J²/M⁴), which is also the entropy asymmetry (S₊ − S₋)/(S₊ + S₋):

$$R_+ S_+ = \frac{(\nu - 2)(\nu + 1)}{2\nu}, \qquad R_- S_- = -\frac{(\nu - 1)(\nu + 2)}{2\nu}, \tag{10.10}$$

equivalently

$$R_\pm S_\pm = -\frac{1}{2} \pm \frac{N_R - 2N_L}{2\sqrt{N_L N_R}}. \tag{10.11}$$

The sum is identically −1; the deck involution ν → −ν exchanges the two expressions, as the mirror requires. Equation 10.11 is the precise map from the curvature invariant to the Kerr/CFT level structure that open item 4 asked for, now at the level of individual branches: each horizon carries a universal charge of −1/2 plus a level-mismatch term of opposite sign, and the topological −1 is the trace over the two-sheet cover. The extremal divergence is the 1/ν pole at N_R → 0, and the branch products vanish at ν = 2 and ν = 1, the latter being Schwarzschild where R₋S₋ = 0 consistently with the inner branch degenerating.

The scope of the ν-map is now settled by a general theorem. For any family of the deck-symmetric form S± = 2π(W(M) ± √(W(M)² − J²)), with W an arbitrary function of the mass (third derivative kept free in the symbolic computation), two exact statements hold. First, the sum R₊S₊ + R₋S₋ equals −1 identically: the integer is a property of the ± structure alone, not of W, which at once explains the Kerr-Sen integer at all charge and replaces case-by-case verification (the product S₊S₋ = 4π²J² is automatically mass-free for the whole family, so this is the four-face equivalence holding family-wide). Second, the split obeys the closed form

$$R_\pm S_\pm = -\frac{1}{2} \pm D, \qquad D = \frac{(3 - \Sigma)\,\nu}{2} - \frac{1}{\nu}, \qquad \Sigma \equiv \frac{W' W'''}{W''^2} + \frac{W'^2}{W\,W''}, \tag{10.10b}$$

where ν is the entropy asymmetry. The scale-invariant quantity Σ equals 2 for every power law W = m^p, independently of p, so the Kerr split D = ν/2 − 1/ν is shared by all scale-covariant families: this is why equal-spin Myers-Perry in five dimensions (p = 3/2) follows the Kerr map exactly (verified numerically at machine precision, alongside a forty-digit cross-validation of our outer-branch curvature against the closed form of Bravetti, Nettel, and Quevedo). Kerr-Sen has W = M² − Q²/2, a shifted power law, giving Σ = 2/(1 − q²/2) with q = Q/M; the resulting deviation from the Kerr split matches the measured values exactly. The interpretation: the trace is topological and blind to the level coordinate, while the branch split measures the scale anomaly of the level coordinate, which background charge induces and rotation does not.

## 10.9 Frame sensitivity of the geometric face

A caution uncovered by testing whether 10.10 is universal. For Kerr-Newman in the two-dimensional angular frame (M,J) at fixed Q, the diagonal sum R₊S₊ + R₋S₋ is not −1 and not constant: it drifts continuously with Q (values −0.41, −0.60, −9.78 at various (M,J,Q); it approaches −1 only as Q → 0). The product face S₊S₋ = 4π²(J² + Q⁴/4) remains exactly mass-free for KN, so the four-face equivalence as stated requires a specification of which fluctuation frame realizes the geometric face. Resolution: this is consistent with the paper as written. Section 7.11 already records that the Kerr-Newman product remains mass-independent while the integer moves through curvature couplings to the charge direction, with the perturbative breaking coefficient given in (7.17). The values above are the nonperturbative continuation of that result, so no correction to Section 7 is needed; the enrichment is that the exact ν-map (10.10) now identifies what the charge deformation is deforming away from. The natural universality test is Kerr-Sen, where the two-horizon sum is known to stay at −1 for all charge: if its individual products also satisfy (10.10) with its own ν, the ν-map is the canonical branch-level form for every A = B family. The theme stands: geometric invariants of the cover are properties of fluctuation frames, while the product and CFT faces are frame-blind.

## 10.10 The monodromy bridge, sharpened to isomonodromy

The Castro-Lapan-Maloney-Rodriguez monodromy program attaches to each root r_i of the horizon polynomial a monodromy exponent proportional to (ω − m Ω_i)/(4π T_i), including complex exponents at virtual roots in the AdS case. These exponents are frequency-dependent, so they cannot equal the virtual charges directly. The correct bridge candidate is isomonodromy: the study, via Painleve transcendents (Novaes, Carneiro da Cunha), of how monodromy data deform as the singular points of the radial equation move. The singular points are precisely the roots r_i(M, Q, ℓ), so isomonodromic deformation theory lives on exactly the parameter space that carries the Ruppeiner branch geometry. The sharp open question for the fifth face: are the quantized virtual charges (10.8, 10.9) isomonodromic invariants of the AdS radial equation in the zero-frequency or zero-pressure limit? A match of −27/16 or of the polynomial (q² + 10)(q² − 5)/16 against known Painleve VI (four regular singular points) invariants would close the loop.

## 10.11 Monodromy closure and the identity of the virtual sheets

Two exact statements sharpen the bridge. For a neutral massless scalar on RN-AdS the monodromy exponent at each root is α_i = ω r_i²/Δ'(r_i) up to normalization, and for Kerr-AdS it is α_i = [ω(r_i² + a²) − m a(1 + r_i²/ℓ²)]/Δ'(r_i). In both cases

$$\sum_{i=1}^{4} \alpha_i = 0 \quad \text{identically, for all } \omega \text{ and } m, \tag{10.12}$$

verified to forty digits and provable in one line by the residue theorem applied to the defining one-form, since the AdS quartic leaves no residue at infinity. The physical content of 10.12 is sharper than folklore: the exponent at horizon i is the first-law entropy shift per absorbed quantum, αᵢ = (ω ∂_M + m ∂_J) Sᵢ / 4π, so the total over the complete root set is the same derivative of the entropy sum Ŝ. The closure Σαᵢ = 0 is therefore exactly equivalent, via the criterion of Zhang and Gao (arXiv:1410.7222), to the mass- and angular-momentum-independence of the all-horizon entropy sum established by Wang, Xu, and Meng (arXiv:1310.6811) and Du-Tian: two literatures, black hole monodromy and entropy relations, have been stating the same fact without citing each other, and the virtual horizons are the agents of the closure in both. It is the wave-equation face of the Vieta completion of Section 9, with the per-quantum entropy shift standard, the sum universality theirs, and the junction ours.

Second, the flat-limit bookkeeping. As ℓ → ∞ the physical pair sum tends to 2Mω, the known flat value, while the virtual pair sum tends to exactly −2Mω. In flat space, that 2Mω of monodromy content is carried by the irregular singular point at infinity, as Stokes data. In AdS there is no irregular point: the two virtual roots sit at r ≈ ±iℓ − M as regular singular points, and in the flat limit they run off to infinity and merge, which is precisely the standard confluence that manufactures an irregular singularity from two regular ones. The identity of the virtual sheets is therefore this: they are the AdS unfolding of the flat-space irregular singularity. Everything the flat theory compresses into Stokes data at infinity, the AdS theory displays as two regular points, and those points are the virtual horizons.

*In plain language: in flat space the black hole's wave equation hides part of its structure at infinity, folded up in a mathematical object called an irregular singularity. Turning on the cosmological constant unfolds it into two visible points, and those two points are exactly the ghost horizons whose curvature charges we computed. The charges are properties of the unfolded object.*

This gives the isomonodromy program its precise target. The massless scalar equation on RN-AdS is Fuchsian with five regular singular points (the four roots plus infinity, where the exponents are the AdS conformal weights). Its isomonodromic deformations form a two-time Garnier system, since five points on the sphere have two independent cross-ratios, and the thermodynamic fluctuation plane (M, Q) at fixed ℓ has exactly that dimension. The map from the fluctuation frame to the Garnier deformation space is therefore a map between equal-dimensional spaces, and the natural conjecture is that the Ruppeiner branch geometry pulls back structures of the Garnier system, with the branch entropies related to the logarithm of the isomonodromic tau function localized at each singular point. Whether −27/16 appears as tau-function data of the confluence limit is the concrete computation this leaves open.
