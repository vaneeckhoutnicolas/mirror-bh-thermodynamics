# Mirror-Constrained Black Hole Thermodynamics

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24139477.svg)](https://doi.org/10.5281/zenodo.24139477)

Companion research to Ahn, Bae, Jang, Kwon, *A Constraint-Free Formulation of Black Hole Thermodynamics from the Field Equations*, arXiv:2605.08235.

**Author:** N. Van Eeckhout, independent researcher, Brussels.

**Status (2026-11-11):** the manuscript in `paper/` is version 1 (July 2026). It is superseded and kept for the record: a critical recomputation (carried out with an AI assistant, with new code) confirmed the computations it reran and found errors of statement and of attribution, listed in [ERRATA.md](ERRATA.md). A shorter revised article is in preparation. Not submitted. Please do not cite version 1.

**Archive:** Zenodo, DOI [10.5281/zenodo.24139477](https://doi.org/10.5281/zenodo.24139477) (all versions; it always resolves to the latest one). The snapshot of 2026-11-11 is version `v0.3-errata`, DOI 10.5281/zenodo.24139478. Items E6 and E7 of the errata were added after that snapshot.

## Core results

1. **The diagonal invariant on the mirror family.** For the two-horizon Ruppeiner geometries of the branched double cover, the diagonal contraction R+S+ + R-S- equals -1 identically on the entire deck-symmetric family S(+/-) = 2 pi (W(M) +/- sqrt(W^2 - J^2)) with arbitrary W(M), with the branch split in closed form: D = (3 - Sigma_W) nu / 2 - 1/nu, Sigma_W = W'W'''/W''^2 + W'^2/(W W''). Sigma_W = 2 for every power law; Kerr-Sen deviates as the scale anomaly of its shifted level coordinate. Correction: version 1 also states that the integer holds exactly when the entropy product is mass-independent. That is not true in general (Kerr-Newman keeps a mass-independent product and breaks the integer, equation 7.17); see ERRATA.md, E1. For Kerr the values on each horizon follow from the curvature published by Aman, Bengtsson and Pidokrajt in 2015; see ERRATA.md, E7.

2. **Flat limit values on the virtual sheets.** Ruppeiner geometry extended to the complex roots of the AdS horizon quartic. On each virtual sheet the product R S has an exact rational flat limit: -27/16 in the electric fluctuation frame (unchanged by background rotation, shown symbolically for generic charge) and -25/16 + 5q^2/32 + q^4/32 in the angular frame, where the sum over the two sheets factorizes as (q^2 + 10)(q^2 - 5)/16. These values are correct and their origin is elementary. Version 1 calls them quantized curvature charges, which claims too much (ERRATA.md, E4).

3. **The identity of the virtual sheets.** The monodromy exponents of the radial wave equation close over the complete root set (equivalent, via the Zhang-Gao criterion, to the entropy-sum universality of Wang-Xu-Meng), and in the flat limit the virtual pair carries exactly -2 M omega, the Stokes content of the flat-space irregular singularity. The virtual horizons are the AdS unfolding of that singularity. The closure identity has earlier sources than those cited in version 1 (ERRATA.md, E3).

4. **Context beta.** The gap between physical-subset and complete-root-set invariants behaves as an omitted regression variable: apparent volatility of thermodynamic invariants is deterministic context, R^2 = 1 under full accounting.

All numerical claims are exact (Gaussian-rational Laurent-series arithmetic) or verified to forty digits, cross-validated against published closed forms (Aman, Bengtsson and Pidokrajt 2015; Bravetti, Momeni, Myrzakulov and Altaibayeva 2013; version 1 names other authors for the second one, see ERRATA.md, E6).

## Repository layout

- `ERRATA.md` : known errors of version 1 and their corrections.
- `paper/` : the manuscript (markdown source of record, LaTeX, compiled PDF, 31 pages).
- `ancillary/` : the ancillary file, 21 sections of explicit expressions, protocols and exact tables (intended for the arXiv `anc/` folder).
- `code/` : Python scripts reproducing every computation (sympy + mpmath, no other dependencies). See `code/README.md`. A run of all scripts from a clean clone is recorded in `code/RUN-LOG-2026-11-11.md`.
- `review/` : records of July 2026, not updated: the novelty review made for version 1 (16 logged searches, full-text readings, 10 attribution corrections, precaution notes) and the integration checklist of that time. Where they differ from `ERRATA.md`, the errata prevail.
- `archive/` : working drafts of the new sections, kept for provenance.

## Reproducing the computations

    pip install sympy mpmath
    cd code
    python3 kerr_calib.py        # sign convention: Kerr diagonal = -1
    python3 run_rn_generic.py    # symbolic proof: -27/16 per virtual sheet
    python3 run_kn_generic.py    # symbolic deformation polynomial
    python3 generalW2.py         # general W-family theorem
    python3 mp5d_check.py        # 40-digit cross-validation vs Bravetti et al.
    python3 abp_check.py         # cross-validation vs Aman-Bengtsson-Pidokrajt
    python3 monodromy.py         # monodromy closure and flat-limit split

## License

- `code/` : MIT License (see `code/LICENSE`).
- Manuscript, ancillary and review texts: (c) 2026 N. Van Eeckhout, all rights reserved pending arXiv submission (arXiv grants of license will apply upon submission).
