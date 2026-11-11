# Two horizon Ruppeiner geometry of level homogeneous black hole entropies

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24139477.svg)](https://doi.org/10.5281/zenodo.24139477)

**Author:** N. Van Eeckhout, independent researcher, Brussels. ORCID [0000-0002-5256-3185](https://orcid.org/0000-0002-5256-3185).

**Status (November 2026):** version 2 is a short article of eleven pages, in `paper/`. It is a preprint and has not been peer reviewed. One script, `code/replay_short_article.py`, replays every statement of the article. Version 1 (July 2026, *Mirror-Constrained Black Hole Thermodynamics*, 31 pages) is superseded: it is kept unchanged in `archive/version-1/`, and its known errors are listed in [ERRATA.md](ERRATA.md). Please do not cite version 1.

**Archive:** Zenodo, DOI [10.5281/zenodo.24139477](https://doi.org/10.5281/zenodo.24139477). This identifier covers all versions and always resolves to the latest one. Version 2 is release `v2.0-article`, DOI [10.5281/zenodo.24147106](https://doi.org/10.5281/zenodo.24147106). Version 1 is release `v0.3-errata`, DOI [10.5281/zenodo.24139478](https://doi.org/10.5281/zenodo.24139478); that snapshot holds items E1 to E5 of the errata, and the current [ERRATA.md](ERRATA.md) is the complete list.

## What the article shows

The Ruppeiner metric is the negative Hessian of the entropy S in the conserved charges (M, J), and R is its scalar curvature.

1. **A diagonal form.** For entropies of the form S = W(M) s(J/W(M)), with W an arbitrary function (the level function), the metric is diagonal in the coordinates (M, j = J/W): ds^2 = - W''(M) (s - j s') dM^2 - W(M) s''(j) dj^2.

2. **A curvature formula.** R S = -(s/(2a)) [Sigma_W + j s'''/s'' + j^2 s''/a] with a = s - j s'. The level function enters only through Sigma_W = W'W'''/W''^2 + W'^2/(W W''), which equals 2 exactly for power laws and exponentials.

3. **Two horizons.** For S(+/-) = 2 pi (W +/- sqrt(W^2 - J^2)), with nu = (S+ - S-)/(S+ + S-): R(+/-) S(+/-) = -1/2 +/- [(3 - Sigma_W) nu/2 - 1/nu]. Hence R+S+ + R-S- = -1 for every level function, while R+S- + R-S+ = 3 holds only if Sigma_W = 2. Examples: Kerr, Kerr Sen at fixed charge, five dimensional Myers Perry with equal spins.

4. **An exact converse.** Among entropies with S+ + S- = 4 pi W(M) and S+ S- = 4 pi^2 k(J), the sum equals -1 for every W if and only if k is the square of an affine function. A mass independent entropy product is therefore not sufficient: for Kerr Newman at fixed charge the sum is -1 + Q^4 (3 M^4 - J^2)/(4 M^4 J^2) + O(Q^6).

5. **A single horizon companion.** For S proportional to sqrt(W^2 - J^2), R S = -Sigma_W/2 - (1 - Sigma_W/2) J^2/W^2. With a power law W this is R S = -1, the value published in 2006 for the five dimensional Kerr black hole with one angular momentum.

## What is taken from earlier work

- The Ruppeiner metric of Kerr on both horizons, in diagonal form, and its curvature: Aman, Bengtsson and Pidokrajt (2015). For Kerr, the two relations of item 3 follow in one line from their formulas, where the two horizons are not combined.
- The coordinate J/S, the conformal relation with the Weinhold metric, and the curvature of Kerr in any dimension: Aman and Pidokrajt (2006).
- The curvature of quasi homogeneous potentials, which contains item 2 for power law level functions: Aman, Bengtsson and Pidokrajt (2006).
- The curvature of five dimensional Myers Perry with equal spins: Bravetti, Momeni, Myrzakulov and Altaibayeva (2013).

What the article adds is the arbitrary level function, the statements on the pair of horizons, and the converse. Full references are in the article.

## Checking the article

    pip install sympy mpmath
    python3 code/replay_short_article.py

The last line must read `36 checks, 0 failed`. The run takes less than a minute. The tags printed by the script are those of Appendix A of the article. See `code/README.md`.

## Method

The author had no human collaborator. The work was done in sessions with an AI assistant (Claude, Anthropic), which took part in every stage: the derivations, the literature search and the drafting of the text. No computed result rests on the assistant's word: each one is an exact symbolic identity or a numerical statement at stated precision, replayed by the script above. See `AUTHORS.md`.

## Repository layout

- `paper/` : the article (LaTeX source, PDF, and a markdown rendering).
- `code/` : the replay script of the article.
- `ERRATA.md` : known errors of version 1.
- `archive/version-1/` : version 1 as it was in July 2026, superseded. Manuscript, ancillary file, scripts with a run log, novelty review, drafts.
- `AUTHORS.md`, `CITATION.cff`, `LICENSE.md`.

## License

- Code (`code/` and `archive/version-1/code/`): MIT License.
- Texts (`paper/`, `ERRATA.md`, `archive/`): (c) 2026 N. Van Eeckhout, all rights reserved. See `LICENSE.md`.
