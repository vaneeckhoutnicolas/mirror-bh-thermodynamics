# Section 10. Virtual sheets and quantized curvature charges

*Insertable after Section 9 (context and the cosmological beta). Equation numbers 10.x, renumber as needed.*

## 10.1 The complete cover and a failed conjecture

Turning on the cosmological constant promotes the horizon condition from a quadratic to a quartic. For Reissner-Nordstrom-AdS at fixed AdS radius ℓ,

$$\frac{r^4}{\ell^2} + r^2 - 2Mr + Q^2 = 0, \tag{10.1}$$

so the two-sheeted physical cover of Sections 2 through 7 is embedded in a four-sheeted branched cover of parameter space. Two roots are the physical horizons r±. The other two form a complex conjugate pair, the virtual sheets. Section 9 established that Vieta symmetric functions are context-complete on the full root set: the entropy product over all four roots is π⁴Q⁴ℓ⁴, mass-free, while the truncation to the physical pair is not.

The four-face equivalence of Section 7 ties the diagonal invariant R₊S₊ + R₋S₋ to product mass-independence. Assembling the two results suggests a natural conjecture: the diagonal invariant, broken at finite pressure on the physical pair, should be restored as a Galois trace over the complete cover,

$$\sum_{i=1}^{4} R_i S_i \stackrel{?}{=} \text{const}, \tag{10.2}$$

where each branch entropy S_i(M,Q) = πr_i² defines its own Ruppeiner geometry (metric g = −Hess S, the convention calibrated so that Kerr yields exactly −1) and the conjugate pair contributes a real sum.

This conjecture is false. The four-root sum is real, as it must be, but not constant: at (M,Q,ℓ) = (1, 0.5, 10) it equals −3.211, at (1, 0.5, 5) it equals −2.279, at (2, 0.7, 8) it equals −0.729. Galois invariance guarantees only that the trace is a rational function of the coefficients, not that it is constant. We record the refutation and turn to what the decomposition revealed instead.

*In plain language: we hoped that adding up the invariant over all four sheets, real and virtual, would give back a conserved number. It does not. But splitting the sum into its physical and virtual halves uncovered something better.*

## 10.2 The virtual charges

Decompose the trace into the physical pair and the virtual pair and take the zero-pressure limit ℓ → ∞. The physical pair returns to its flat value, 0 for the (M,Q) family and −1 for the (M,J) family, which independently validates the numerical pipeline. The virtual pair does something unexpected: it converges to an exact rational number that depends on nothing except which two-plane of thermodynamic fluctuations defines the Ruppeiner geometry.

For electric fluctuations, coordinates (M,Q), including on a Kerr-Newman-AdS background with arbitrary fixed rotation,

$$\lim_{\ell \to \infty}\,(R_v S_v + R_{\bar v} S_{\bar v})\Big|_{(M,Q)} = -\frac{27}{8}, \tag{10.3}$$

independent of the background values of M, Q, and J. For angular fluctuations, coordinates (M,J), on a background of fixed charge Q,

$$\lim_{\ell \to \infty}\,(R_v S_v + R_{\bar v} S_{\bar v})\Big|_{(M,J)} = -\frac{25}{8} + \frac{5}{16}\,q^2 + \frac{1}{16}\,q^4, \qquad q \equiv \frac{Q}{M}, \tag{10.4}$$

independent of J and of overall scale, deformed only by the background charge. The deformation factorizes:

$$16 \times \text{charge}\big|_{(M,J)} = (q^2 + 10)(q^2 - 5). \tag{10.5}$$

Both statements are exact. They were first found numerically (Richardson extrapolation in 1/ℓ² agreeing with the rational values to ten or more digits, including a predictive out-of-grid test at q = 0.7 confirmed to eleven digits) and then derived analytically by the method of subsection 10.4, in exact Gaussian-rational arithmetic, at multiple rational parameter points. Equation 10.3 holds sheet by sheet: each virtual sheet carries exactly −27/16, a real number, with every negative power of 1/ℓ vanishing identically. The five exact rational charges determining the quartic polynomial 10.4 are listed in the ancillary file, Section 20.

*In plain language: the two ghost horizons, the complex roots nobody assigns a temperature to, carry a fixed curvature charge. In the electric frame that charge is minus twenty-seven eighths, always. Rotate the background as much as you like, it does not move. In the angular frame the charge starts at minus twenty-five eighths and is pushed by background charge along an exact polynomial, and by nothing else.*

## 10.3 The rigidity hierarchy

The virtual charges are more rigid than the physical integers. In the (M,Q) frame at fixed J ≠ 0, the flat-limit physical pair sum is not even constant: it takes the values 0.404, 0.344, 0.504 at (M,Q) = (1, 0.4), (1.5, 0.6), (1, 0.7) with J = 0.3. The virtual pair at those same points is −27/8 to full precision. The completion sector holds its value while the physical sector drifts with the background.

This is the curvature-level image of the context decomposition of Section 9. There, S_phys carried all the mass dependence and S_all was context-free; the regression made apparent volatility exactly equal to omitted context. Here, R·S on the virtual sheets is a pure number of the fluctuation frame, a zero-beta quantity, while all context sensitivity, to background hair and to pressure, is carried by the physical sheets. The virtual completion is the zero-beta sector of the branched cover.

The charge-rotation asymmetry of Section 9 also reappears, with an inversion we flag honestly. In Section 9, charge was context-completable and rotation was not. Here, background rotation is inert everywhere (proven exactly in the electric frame, equation 10.3, and verified numerically across J in the angular frame), while background charge is the sole agent of deformation, acting only on the angular frame through the even polynomial of 10.4. In both cases J and Q play structurally distinct roles; the direction of the distinction differs, and understanding why is an open question. We note that Q enters the deformation starting at q², whereas the level mismatch of Section 7 carries charge as Q⁴/4 inside N_L − N_R; the two exponents do not match naively and any CFT reading of the virtual charges must account for this.

## 10.4 Analytic derivation

The flat limit is controlled by the asymptotics of the virtual root. Writing x = 1/ℓ, the virtual branch of 10.1 is

$$r_v = \frac{i}{x} - M + \frac{i(3M^2 - Q^2)}{2}\,x + O(x^2), \tag{10.6}$$

with the conjugate sheet obtained by i → −i. The branch entropy S_v = πr_v² = π(−ℓ² − 2iMℓ − 2M² + Q²) + O(1/ℓ) diverges as −πℓ², while the leading Hessian metric is the constant Lorentzian form diag(4π, −2π). Curvature therefore enters at order ℓ⁻², and the product R·S is finite in the limit.

The exact evaluation proceeds as follows. Implicit differentiation of 10.1 gives all partial derivatives of the branch through third order as rational functions of (r, M, Q, x); the Brioschi formula for a Hessian metric requires nothing beyond third order, since the second-derivative block of the numerator cancels identically for any metric that is a Hessian. Substituting for r the Laurent series 10.6, extended by Newton iteration in truncated Laurent-series arithmetic over the Gaussian rationals, turns R·S into an exact Laurent series in x. Every coefficient of a negative power vanishes identically, and the constant term is −27/16 per sheet. The same machinery applied to Kerr-Newman-AdS in the (M,J) frame, with a = J/M, Ξ = 1 − a²x², m = MΞ², and S = π(r² + a²)/Ξ, yields the exact rational charges that determine 10.4, and applied in the (M,Q) frame it yields −27/8 identically under background rotation. Full protocol and tables in the ancillary file, Section 20.

## 10.5 Quantization pattern and a conjecture

Per virtual sheet the two frame charges are −27/16 and −25/16, that is, −3³/16 and −5²/16. All exact values obtained, including the deformation coefficients 5/16 and 1/16, are quantized in sixteenths. We flag the 3³ and 5² pattern as an observation, not a claim.

The two undeformed charges fit a one-parameter formula in the scaling weight w of the second fluctuation coordinate (w = 1 for Q, which scales like M, and w = 2 for J, which scales like M²):

$$\text{charge} = -\frac{29}{8} + \frac{w}{4}. \tag{10.7}$$

Two data points determine a line, so 10.7 is a conjecture, not a result. It is falsifiable: Kerr-Sen in its electric frame should give −27/8, and the five-dimensional Myers-Perry family, where the angular momentum carries weight 3/2 relative to the appropriate power of the mass, would test the interpolation. Both computations use the machinery of 10.4 unchanged.

## 10.6 Status within the program

The naive completion of the diagonal invariant fails: pressure does not conserve the four-sheet trace. What the completion does instead is split the invariant into rigid, quantized pieces attached to the Galois orbits of the horizon polynomial, with the virtual orbit carrying frame-dependent pure numbers and the physical orbit carrying all the context. The four-face equivalence of Section 7 gave the physical integer four readings, thermodynamic, geometric, and two CFT readings. The virtual charge is a fifth object, attached to the completion rather than to either horizon, and it currently has no CFT face. Whether −27/8 and the polynomial (q² + 10)(q² − 5)/16 admit a level-structure reading, and whether the inert role of J here is the mirror image of its obstruction role in Section 9, are the two questions this section leaves open.

*In plain language: we did not find the conserved total we were looking for. We found something stranger: the imaginary part of the black hole's family tree carries fixed rational numbers, more stable than anything on the real side, and we can now compute them exactly. What they count, nobody knows yet.*
