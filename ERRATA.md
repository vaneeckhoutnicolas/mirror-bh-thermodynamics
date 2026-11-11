# Errata for version 1 (July 2026)

Version 1 of the manuscript is kept unchanged, for the record. Since the release of version 2 it is in `archive/version-1/`, and the paths quoted below were updated accordingly. This file lists the errors found by the author and by a critical recomputation of 2026-11-11, and what the revised article, now in `paper/`, says instead. That recomputation was carried out with an AI assistant (Claude, Anthropic) using new code that shares nothing with the scripts of this repository; it is not a review by an external physicist.

What the recomputation confirmed: the Kerr closed forms and both integers of Section 7; the statement of Section 7.11 on the two parameter family (7.23); the general theorem of Section 10.6 for the mirror family, with its branch split; the flat limit values of Section 10 (electric frame symbolically, angular frame at exact rational points). Nothing else was rechecked. In particular the three parameter Kerr Newman results of Section 7, the first order coefficient (6.1), the checks across families of Section 8 and the numerical statements of Sections 9 and 10.9 stand as the author's own computations.

## E1. The equivalence of Sections 7.11 and 8 is stated too strongly

Version 1 states that the diagonal invariant R+S+ + R-S- is a mass independent integer exactly when the entropy product is mass independent, and lists this as item (vi) of an equivalence valid for the Kerr Newman family.

This is not correct. Kerr Newman has a mass independent entropy product for every charge, while equation (7.17) of the same manuscript shows that the invariant departs from -1 as soon as the charge is nonzero. Mass independence of the product is therefore not sufficient. The recomputation confirms it in the angular frame at fixed charge: there the entropy product is 4 pi^2 (J^2 + Q^4/4), free of the mass, and the invariant is not identically -1 when the charge is nonzero.

What version 1 does prove: the invariant equals -1 on the whole mirror family S(+/-) = 2 pi (W(M) +/- sqrt(W^2 - J^2)) (Section 10.6), and inside the two parameter family (7.23) the integer requires A = B. The revised article states the result in that form, with a precise converse.

## E2. Section 9.4: rotation

Version 1 states that charge is "context completable" and rotation is not, on the basis of the product of the quantities r_i^2 + a^2, which depends on the mass parameter m of the metric. The physical entropy product of the complete root set is free of the mass when written with the physical angular momentum J. Rotation is completable exactly as charge is; the boundary of the mechanism is the pure mass Schwarzschild de Sitter case (Visser). The link drawn in that section with the branch split of Section 10.6 is withdrawn.

## E3. Sections 9.5 and 10.9: attribution of the closure identity

Version 1 presents the closure of the monodromy exponents over the complete root set as a junction between two literatures that do not cite each other. Earlier sources exist and must be credited:

- V. Cardoso, J. Natário, R. Schiappa, *Asymptotic Quasinormal Frequencies for Black Holes in Non-Asymptotically Flat Spacetimes*, arXiv:hep-th/0403132 (2004). For Schwarzschild de Sitter the negative root is treated as a fictitious horizon with its own surface gravity, and the identity 1/k_H + 1/k_C + 1/k_F = 0 is derived from the absence of monodromy at infinity. This is the same closure with the same mechanism.
- A. Chanson, J. Ciafre, M. J. Rodriguez, arXiv:2004.14405, where the closure over the Kerr anti de Sitter root set appears explicitly.
- P. Zhao, H. Lu, arXiv:2407.13079, for sums over horizons obtained from the residue at infinity.

The sentence "two literatures state the same closure without citing each other" is withdrawn.

## E4. Section 10: status of the virtual sheet values

The values -27/16 and -25/16 + 5 q^2/32 + q^4/32 are correct. Their origin is elementary. The entropy of a complex root expands at large l as

    S_v / pi = - l^2 - 2 i M l - (2 M^2 - Q^2) + i M (5 M^2 - 3 Q^2) / l + ...

and the curvature of a Hessian metric involves no derivative of the entropy beyond the third. In the electric frame the leading metric is constant and the third derivatives of the cubic term are constants, so the limit of R S is a pure number, whatever the state. With rotation, J enters only at order 1/l^2, which is why background rotation does not change the electric value. In the angular frame the limit depends on the ratio q = Q/M, as stated in version 1.

The expressions "quantized curvature charges" and "rigidity hierarchy" claim more than this supports, and the comparison with the physical sheets in Section 10.3 should not be read as a physical statement.

## E5. Presentation

The following elements of version 1 do not belong in a research article and are absent from the revision: the simulated panel of Section 11 and the note on method that announces it; the asides in plain language of Sections 9 and 10; the lists of novelty declared by the author (Sections 7.10 and 12); the framing as a companion to arXiv:2605.08235, on which the curvature results do not depend. Two drafting remnants are also removed: the first sentence of Section 5 and the closing note.

## E6. Reference list: two wrong entries

Added on 2026-11-11, after the release `v0.3-errata`. Found while the references of the revised article were checked one by one against their records.

1. The paper cited for the five dimensional Myers Perry black hole with equal angular momenta, Adv. High Energy Phys. 2013, 549808 (arXiv:1303.2077, DOI 10.1155/2013/549808), is by A. Bravetti, D. Momeni, R. Myrzakulov and A. Altaibayeva. Version 1 attributes it to A. Bravetti, F. Nettel and H. Quevedo: in the reference list, in Sections 8, 10.6 and 12, in the closing note and in the ancillary file. The same wrong names stood in `README.md`, `AUTHORS.md` and the README of the scripts of version 1, which were corrected together with this item; they remain in the files of July under `archive/version-1/review/` and `archive/version-1/drafts/`, which are kept as records. The formula taken from that paper is the right one: its Ruppeiner curvature for equal angular momenta, R = -S (S^2 + 12 J^2)/(S^4 - 16 J^4) in the normalization of that paper (its Section III.2), which `archive/version-1/code/mp5d_check.py` uses in the equivalent form R S = -u^2 (u^2 + 12)/(u^4 - 16) with u = S/J. The cross validation at forty digits stands.

2. The article of P. Pradhan cited for the Kerr Sen black hole (arXiv:1503.04514) is Eur. Phys. J. C 76 (2016) 131, not 31. An erratum to that article exists, Eur. Phys. J. C 81 (2021) 896.

Ten entries of the reference list were rechecked that day, four against the record of arXiv, of the publisher or of INSPIRE and six against the reference lists of published papers. These two were wrong. The other entries have not been rechecked.

## E7. Sections 7, 7.10, 10.6 and 12: what was already in the literature

Added on 2026-11-11, with E6.

1. For the Kerr black hole, Åman, Bengtsson and Pidokrajt (arXiv:1507.06097) write the entropy and the curvature scalar of the Ruppeiner metric in coordinates that cover the outer and the inner horizon (their equations 35 and 37). Equation (10.8) of version 1, R(+/-) S(+/-) = -1/2 +/- (nu/2 - 1/nu), is equivalent to these two equations; Section 10.6 mentions the agreement as a check of conventions. The closed form of each Kerr sheet, which Section 7.10 lists as new, is therefore a rewriting of a published result. The sum R+S+ + R-S- = -1 and the cross sum R+S- + R-S+ = 3 follow from the same two equations in one line. That paper does not combine the two horizons: for Kerr, the combination is what version 1 adds.

2. The value R S = -1 on a single horizon was published in 2006 for the five dimensional Kerr black hole with one angular momentum (Åman and Pidokrajt, arXiv:hep-th/0510139, equation 51). Version 1 does not cite it next to its integer.

The title of Section 7 ("An original result") and the statements of novelty of Sections 7.10 and 12 must be read with these two facts. The general theorem of Section 10.6, for an arbitrary function W, is not affected.

## How version 1 was produced

Version 1 was produced by the author working alone with an AI assistant (Claude, Anthropic). Every computed result comes with a script that replays it; the assistant also took part in the derivations, the literature search and the drafting. See `AUTHORS.md`.
