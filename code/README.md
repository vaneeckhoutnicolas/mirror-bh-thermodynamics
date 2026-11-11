# Replay script of the article

`replay_short_article.py` checks every numbered statement of the article in `../paper/`. It imports nothing from this repository. Dependencies: Python 3, sympy, mpmath.

    pip install sympy mpmath
    python3 replay_short_article.py

Each check prints its tag, the statement it covers, and `ok` or `FAILED`. The last line must read `36 checks, 0 failed`. The run takes less than a minute. Tested with Python 3.12 and 3.13, sympy 1.14.0 and mpmath 1.3.0.

The tags are those of Appendix A of the article:

- A: the class S = W(M) s(J/W(M)), the diagonal form and the curvature formula.
- B: the combination Sigma_W.
- C: the two branch family, the cross sum, Kerr and Kerr Sen.
- D: the same theorem by an independent route, and the converse.
- E: Kerr Newman at fixed charge.
- F: published closed forms used for comparison.

With the argument `coefficients` the script also prints the 25 coefficients described in Appendix B of the article:

    python3 replay_short_article.py coefficients

The scripts of version 1 are in `../archive/version-1/code/`, with a run log.
