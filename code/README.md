# Computation scripts

Dependencies: Python 3, sympy, mpmath. Convention throughout: Ruppeiner metric g = -Hess S, calibrated so the Kerr diagonal invariant equals -1 (kerr_calib.py).

Core library:
- series_lib.py : exact truncated Laurent series over the Gaussian rationals (add, mul, inverse, powers), expression evaluator, Newton root refinement, Brioschi curvature for Hessian metrics.
- impl2.py : implicit partial derivatives of a branch r(u,v) of P(r,u,v) = 0 to third order, with corruption-safe substitution ordering.

Symbolic theorems:
- run_rn_analytic.py : per-sheet charge -27/16 at rational points (RN-AdS).
- run_rn_generic.py : the same for generic symbolic Q (closed-form theorem).
- run_kn_analytic.py / run_kn_electric.py / run_kn_generic.py : Kerr-Newman-AdS charges, deformation polynomial, electric-frame rigidity.
- generalW.py / generalW2.py : the general deck-symmetric W-family theorem (sum = -1, split D, power-law criterion).
- kerr_individual.py : closed-form Kerr branch products (nu-map).
- kerrsen_symbolic.py : Kerr-Sen split attempt (heavy; the W-family theorem supersedes it).

Numerics and cross-validation:
- kerr_calib.py, rn_flat.py : calibration and RN flatness.
- rnads.py, asympt.py, kerr_ads.py, kn_ads.py, crosscheck.py : numerical discovery pipeline (branch tracking, Richardson extrapolation, deformation scan, predictive test).
- kn_universal.py, kn_universal_num.py : nu-map universality tests.
- mp5d_check.py : Myers-Perry 5D vs Bravetti-Nettel-Quevedo, 40 digits.
- kerrsen_numap.py : Kerr-Sen sum reconfirmation and nu-map counterexample.
- abp_check.py : both Kerr branches vs Aman-Bengtsson-Pidokrajt eq. (37).
- monodromy.py : exponent closure and flat-limit -2 M omega split.
- analytic_rn.py : first (slow) symbolic attempt, kept for provenance.
