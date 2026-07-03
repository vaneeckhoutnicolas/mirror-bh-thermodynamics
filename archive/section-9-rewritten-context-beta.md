# Section 9 (rewritten). Context and the cosmological beta

*Replacement for the existing Section 9 of the white paper, restructured after the novelty review (attribution A9). The identity layer is now attributed to the entropy-relations literature; the section claims only the decomposition, the statistical demonstration, and the completability boundary. Equations renumbered 9.x.*

## 9.1 Prior art and positioning

The algebraic backbone of this section belongs to an established corpus. The mass-independence of the all-horizon entropy product was proven family by family by Cvetič, Gibbons, and Pope, and the all-horizon entropy sum, with virtual horizons explicitly included, was shown by Wang, Xu, and Meng and by Du and Tian to depend only on the cosmological constant and matter couplings. Xu, Wang, and Meng further derived first-law and Smarr structure on the virtual horizons themselves. Visser exhibited the Schwarzschild-de Sitter counterexample for the product. Most importantly, Zhang and Gao reduced the whole question to two criteria that follow from the per-horizon first law, ∂S_i/∂M = 1/T_i: the entropy product over a set of horizons is mass-independent if and only if Σ 1/(T_i S_i) = 0 over that set, and the sum if and only if Σ 1/T_i = 0, together with a Vandermonde lemma and a sharp Laurent-exponent criterion on f(r) that decides both without solving for the roots.

This section adds no new identity to that corpus. What it adds is a change of question. The literature asks which relations are mass-independent over which sets of roots. We ask what the gap between the physical subset and the complete root set does to an observer who only sees the physical subset, and we show that the gap behaves exactly like an omitted variable in a regression: what looks like broken universality, or like noise, is deterministic context that has been left out of the accounting.

*In plain language: previous work established which combinations of horizons give clean, mass-free numbers, provided you count the ghost horizons too. Our question is different: what does the world look like if you refuse to count the ghosts? The answer is that it looks noisy and broken, and that all of the noise is fake.*

## 9.2 The decomposition: local invariant equals universal over context

Reissner-Nordström-de Sitter has the horizon quartic

$$r^4 - \ell^2 r^2 + 2M\ell^2 r - Q^2\ell^2 = 0, \tag{9.1}$$

with three physical roots r₋, r₊, r_c and one negative virtual root r_o. Vieta gives the complete-set product as the constant term, so the complete-set entropy product is mass-free, consistent with the corpus above:

$$S_{\text{all}} \equiv \pi^4 (r_- r_+ r_c\, r_o)^2 = \pi^4 Q^4 \ell^4. \tag{9.2}$$

The physical-subset product is then forced into the form

$$S_{\text{phys}} \equiv \pi^3 (r_- r_+ r_c)^2 = \frac{\pi^3 Q^4 \ell^4}{\Sigma^2}, \qquad \Sigma \equiv r_- + r_+ + r_c = -r_o, \tag{9.3}$$

where the second equality in the definition of Σ is Vieta again (the quartic has no cubic term). Equation 9.3 is the organizing statement of the section: the local invariant equals the universal invariant divided by a context factor, and the context factor Σ, the sum of the physical radii, is identically the virtual root. All the mass dependence of the physical product is carried by Σ. Verified exactly: at Q = 1, ℓ = 10, S_all/π⁴ = 10000 for every M, while S_phys/π³ runs through 80.55, 79.51, 78.51, 77.55, 76.61 as M runs from 1.3 to 1.7, with the identity Q⁴ℓ⁴/Σ² = (r₋r₊r_c)² holding to machine precision.

*In plain language: the clean number is always there. When you only count the horizons you can see, you are looking at the clean number divided by the size of the box, and the box grows with the mass. The mess is the box, not the law.*

## 9.3 The beta and the regression

Because 9.3 is a power law, the language of factor regression applies literally. Write log S_phys = 4 log Q + 4 log ℓ − 2 log Σ + const: the exponents are betas, and Σ is the context factor whose omission biases everything else. Across a cloud of 400 black holes with independently drawn (M, Q, ℓ), regressing log S_phys on the full context (log Q, log ℓ, log Σ) recovers the betas (4, 4, −2) exactly, with R² = 1 to machine precision. Regressing on log Σ alone yields R² = 0.12. The residual scatter of the naive regression is not statistical noise: it is the signature of omitted variables, and it vanishes identically when the accounting is completed. The same lesson holds for the breakings established earlier in the paper: the Kerr-AdS breaking of the diagonal invariant is an exact analytic function of the pressure parameter ε (a degree-five polynomial fit reaches R² = 1.0000000000), and the scattered Myers-Perry d = 6 values collapse onto a single deterministic surface F(J_a/M², J_b/M²) once scaling is quotiented out. Nothing in this landscape is random.

*In plain language: in finance, if a stock looks wildly volatile, the first suspicion is not that the world is random but that your model is missing a factor. Here we can prove it: add the missing factor, the ghost horizon, and the volatility drops to exactly zero. Not approximately. Exactly.*

## 9.4 Completability and its boundary

The Vieta carrier identity, physical product times virtual product equals a mass-free constant, was checked explicitly for d = 4 through 7 in the charged de Sitter family. The d = 5 case is special in a way that must be distinguished from the known dimension statements of the corpus (which concern the mass-independence of complete-set sums for d > 4): in d = 5 the reduced polynomial in x = r² has degree equal to the number of physical horizons, so the physical product is already mass-free by itself, with no virtual completion needed. We call this self-completion, and d = 5 is the only dimension in the range examined where it occurs.

Rotation marks the boundary of the mechanism. For Kerr-de Sitter, the entropy factor is r_i² + a², and the complete-set product evaluates by Vieta to

$$\prod_{i=1}^{4} (r_i^2 + a^2) = P(ia)\,P(-ia) \;\propto\; M^2, \tag{9.4}$$

mass-dependent even over all four roots. Charge is context-completable; rotation is not. The frame-dragging factor leaves an irreducible beta that no accounting of virtual horizons removes. This is the same charge-rotation asymmetry that reappears, with its exact mechanism, in the branch-split anomaly of the Section 10 addendum: there the quantity Σ = W′W‴/W″² + W′²/(WW″) detects the scale anomaly that background charge induces and rotation never does, and here rotation is the sector whose context cannot be completed at all. The two statements are faces of one asymmetry and their common origin is open.

## 9.5 The junction with the wave equation

The completion statement of this section has a wave-equation face, developed in the Section 10 addendum: the monodromy exponent of a mode (ω, m) at horizon i is the first-law entropy shift per absorbed quantum, so the total exponent over the complete root set is the (ω ∂_M + m ∂_J) derivative of the entropy sum, and its vanishing is exactly the sum universality of Wang, Xu, and Meng, by the criterion of Zhang and Gao. The two literatures state the same closure without citing each other; the virtual horizons are the agents of it in both. The identities are theirs; the junction, and the identification of the virtual roots as the unfolded irregular singularity carrying quantized curvature charges, are the contribution of this paper.

*In plain language: the bookkeeping that makes the entropy numbers clean and the bookkeeping that makes waves scatter consistently around the black hole turn out to be the same bookkeeping, kept by the same ghosts. Two communities discovered it separately, in different words, and never noticed.*
