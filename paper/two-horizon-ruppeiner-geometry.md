# Two horizon Ruppeiner geometry of level homogeneous black hole entropies

**Version 2, November 2026. Preprint, not peer reviewed.**

**Author.** N. Van Eeckhout, independent researcher, Brussels. ORCID: 0000-0002-5256-3185. Date: November 2026.

## Abstract

The Ruppeiner metric of the Kerr black hole is known in closed form on
both of its horizons, and the curvature of entropies of the quasi
homogeneous form $S=M^{a}f(M^{b}J)$ is known in general, through the
work of Åman, Bengtsson and Pidokrajt. We extend these results to
entropies of the form $S=W(M)\,s(J/W(M))$ with an arbitrary level
function $W$, a class that contains Kerr in any dimension, the Kerr Sen
black hole at fixed charge and the five dimensional Myers Perry black
hole with equal spins. In the coordinates $(M,\,j=J/W)$ the metric is
diagonal, and the product of the scalar curvature and the entropy is
$RS=-\frac{s}{2\alpha}\bigl[\Sigma_{W}+js'''/s''+j^{2}s''/\alpha\bigr]$
with $\alpha=s-js'$. The level function enters only through
$\Sigma_{W}=W'W'''/W''^{2}+W'^{2}/(WW'')$, which equals $2$ exactly for
power laws and exponentials. For the two branch family
$S_{\pm}=2\pi\bigl(W\pm\sqrt{W^{2}-J^{2}}\bigr)$ this gives
$R_{\pm}S_{\pm}=-\tfrac12\pm\bigl[(3-\Sigma_{W})\nu/2-1/\nu\bigr]$ with
$\nu=(S_{+}-S_{-})/(S_{+}+S_{-})$. Hence $R_{+}S_{+}+R_{-}S_{-}=-1$ for
every level function, while $R_{+}S_{-}+R_{-}S_{+}=3$ holds only if
$\Sigma_{W}=2$. We prove an exact converse: among entropies with
$S_{+}+S_{-}=4\pi W(M)$ and $S_{+}S_{-}=4\pi^{2}k(J)$, the sum equals
$-1$ for every $W$ if and only if $k$ is the square of an affine
function. A mass independent entropy product is therefore not
sufficient: for Kerr Newman at fixed charge the sum is
$-1+Q^{4}(3M^{4}-J^{2})/(4M^{4}J^{2})+O(Q^{6})$. The single horizon
value $RS=-1$ of five dimensional Kerr, published in 2006, is the
companion case $S\propto\sqrt{W^{2}-J^{2}}$. Every statement is replayed
by a computer algebra script that accompanies the article.

*Preprint, not peer reviewed. The script `replay_short_article.py`
replays every statement; its check tags are listed in
Appendix <a href="#app:replay" data-reference-type="ref"
data-reference="app:replay">9</a>.*

# Introduction

Thermodynamic fluctuation theory equips the space of equilibrium states
with the Ruppeiner metric, the negative Hessian of the entropy in the
conserved quantities \[1\]. For black holes, Åman, Bengtsson and
Pidokrajt have obtained a body of closed form results. For the Kerr
black hole with one spin in any dimension, \[2\] introduces the
coordinate $J/S$, writes the Weinhold metric in a flat diagonal form,
obtains the Ruppeiner metric from it through the conformal factor $1/T$,
and gives the curvature scalar for every dimension; in five dimensions
it is $R=-1/S$. In \[3\] the Hessian metric of any potential of the
quasi homogeneous form $x^{a}f(x^{b}y)$ is studied, with a flatness
theorem and a general formula for the curvature scalar. In \[4\] both
horizons of the Kerr black hole are treated: the metrics of the outer
and of the inner horizon are written in diagonal form, and the entropy
and the curvature scalar are written in coordinates that cover the state
spaces of both horizons.

The entropy $S_{-}$ of the inner horizon and the product $S_{+}S_{-}$
have a long history of their own \[5,6,7,8,9,10\]. For Kerr the product
is $4\pi^{2}J^{2}$ and does not depend on the mass. A recent formulation
of black hole thermodynamics obtained directly from the field equations
\[11\] was the starting point of this work.

This article asks what the Ruppeiner curvatures of the two horizons
satisfy as a pair. For Kerr the answer can be read off from \[4\]. In
terms of their angular coordinate $\beta$, which covers the outer
horizon for $|\beta|\le\pi/4$ and the inner one for
$\pi/4\le|\beta|\le\pi/2$, their entropy and curvature scalar give
$RS=f(\cos2\beta)$ with $f(x)=-\tfrac12-\tfrac1x+\tfrac x2$. At given
$M$ and $J$ the outer horizon is $\cos2\beta=\nu$ and the inner one
$\cos2\beta=-\nu$, where $\nu=\sqrt{1-J^{2}/M^{4}}$. Hence
$$\label{eq:kerrpair}
R_{+}S_{+}+R_{-}S_{-}=-1,
\qquad
R_{+}S_{-}+R_{-}S_{+}=3 ,$$ two relations that we have not found stated.
Our purpose is to identify the structure responsible for them and its
exact scope. The results are the following.

1.  For entropies $S=W(M)\,s(J/W(M))$, with $W$ an arbitrary function,
    the Ruppeiner metric is diagonal in the coordinates $(M,J/W)$ and
    the two functions $W$ and $s$ separate
    (Proposition <a href="#prop:diag" data-reference-type="ref"
    data-reference="prop:diag">1</a>). For Kerr this is the form of
    \[4\].

2.  The product $RS$ has a closed form in which $W$ enters only through
    one scale invariant combination $\Sigma_{W}$, and linearly
    (Proposition <a href="#prop:curv" data-reference-type="ref"
    data-reference="prop:curv">2</a>). One has $\Sigma_{W}=2$ exactly
    when $W$ is a power law or an exponential
    (Lemma <a href="#lem:sigma" data-reference-type="ref"
    data-reference="lem:sigma">1</a>); for power laws the formula is a
    case of the general curvature of \[3\].

3.  For the two branch family $S_{\pm}=2\pi(W\pm\sqrt{W^{2}-J^{2}})$ the
    first relation of <a href="#eq:kerrpair" data-reference-type="eqref"
    data-reference="eq:kerrpair">[eq:kerrpair]</a> holds for every level
    function, and the second one holds only if $\Sigma_{W}=2$
    (Theorem <a href="#thm:mirror" data-reference-type="ref"
    data-reference="thm:mirror">1</a> and
    Corollary <a href="#cor:cross" data-reference-type="ref"
    data-reference="cor:cross">1</a>). The Kerr Sen black hole at fixed
    charge is an example with $\Sigma_{W}\neq2$.

4.  The value $RS=-1$ on the single horizon of five dimensional Kerr
    \[2\] is the case $S\propto\sqrt{W^{2}-J^{2}}$ of the same formula
    (Proposition <a href="#prop:odd" data-reference-type="ref"
    data-reference="prop:odd">3</a>).

5.  Conversely, if $S_{+}+S_{-}=4\pi W(M)$ and
    $S_{+}S_{-}=4\pi^{2}k(J)$, the first relation of
    <a href="#eq:kerrpair" data-reference-type="eqref"
    data-reference="eq:kerrpair">[eq:kerrpair]</a> holds for every $W$
    if and only if $k$ is the square of an affine function
    (Theorem <a href="#thm:converse" data-reference-type="ref"
    data-reference="thm:converse">2</a>). A mass independent product is
    not enough: Kerr Newman at fixed charge violates the relation at
    order $Q^{4}$ (Corollary <a href="#cor:kn" data-reference-type="ref"
    data-reference="cor:kn">2</a>).

The scope is deliberately narrow. All statements concern the Hessian
metric in two fluctuating charges, with every other parameter held
fixed, and Hessian metrics are not covariant under nonlinear changes of
the charges. The entropy of the inner horizon is used in the formal
sense of the literature cited above. We do not propose a physical
interpretation of the number $-1$, and we do not treat a cosmological
constant.

What is taken from earlier work is stated where it is used: the diagonal
form for Kerr \[4\], the coordinate $J/S$ and the conformal relation
with the Weinhold metric \[2\], the power law case of the curvature
formula \[3\], and the five dimensional value \[2\]. What we add is the
arbitrary level function, the statements on the pair of horizons, and
the converse.

Every displayed statement is an exact identity that a script checks
symbolically, or a numerical statement at stated precision. The
correspondence between statements and checks is given in
Appendix <a href="#app:replay" data-reference-type="ref"
data-reference="app:replay">9</a>.

# Setting

## Conventions

We use units $G=c=\hbar=k_{B}=1$, so that the entropy of a horizon is a
quarter of its area. Let $S(M,J)$ be an entropy as a function of the
mass $M$ and of one further conserved charge $J$. The Ruppeiner metric
is $$\label{eq:rup}
g=-\frac{\partial^{2}S}{\partial x^{a}\partial x^{b}}\,dx^{a}dx^{b},
\qquad (x^{1},x^{2})=(M,J),$$ and $R$ denotes its scalar curvature, with
the sign for which the unit round sphere has $R=2$. With this convention
the curvature scalars of \[2\], \[4\] and \[17\] are reproduced with
their signs.

Two elementary invariances are used throughout. First, under an affine
change of the coordinates $(M,J)$ the Hessian transforms as a tensor, so
$R$ and $S$ are unchanged as functions on the state space. Second, under
$S\to cS$ with a constant $c>0$ one has $g\to cg$ and $R\to R/c$, so the
product $RS$ is unchanged. The product $RS$ can therefore be compared
between papers that normalize the entropy and the charge differently.

## Level homogeneous entropies

<div id="def:lh" class="definition">

**Definition 1**. An entropy $S(M,J)$ is *level homogeneous* if there
are a function $W$ of the mass, the *level function*, and a function $s$
of one variable, the *shape function*, such that $$\label{eq:class}
S(M,J)=W(M)\,s(j),\qquad j=\frac{J}{W(M)} .$$ We assume that $W$, $W'$,
$W''$, $s$, $s''$ and $$\label{eq:alpha}
\alpha(j)=s(j)-j\,s'(j)$$ do not vanish on the domain considered.

</div>

Equivalently, the fundamental relation has the form $$\label{eq:phi}
W(M)=S\,\varphi\!\left(\frac{J}{S}\right),$$ where $\varphi$ is defined
by $s\,\varphi(j/s)=1$. From
<a href="#eq:class" data-reference-type="eqref"
data-reference="eq:class">[eq:class]</a>, $$\label{eq:first}
\frac{\partial S}{\partial M}=W'\alpha,\qquad \frac{\partial S}{\partial J}=s' ,$$
so that the temperature is $T=1/(W'\alpha)$, and $\alpha$ is the
derivative of $S$ with respect to $W$ at fixed $J$.

For a power law $W=M^{a}$, relation
<a href="#eq:class" data-reference-type="eqref"
data-reference="eq:class">[eq:class]</a> reads $S=M^{a}s(M^{-a}J)$. This
is the case $a+b=0$ of the potentials $x^{a}f(x^{b}y)$ of \[3\], called
quasi homogeneous there; see also \[12\], cited in \[3\], and \[13\].
For a general level function the entropy
<a href="#eq:class" data-reference-type="eqref"
data-reference="eq:class">[eq:class]</a> is homogeneous of degree one in
the pair $(W(M),J)$ but it is not quasi homogeneous in $(M,J)$. This is
why a separate name is used.

## Examples

1.  *Kerr.* $S_{\pm}=2\pi\bigl(M^{2}\pm\sqrt{M^{4}-J^{2}}\bigr)$, that
    is $W=M^{2}$ and $s_{\pm}(j)=2\pi\bigl(1\pm\sqrt{1-j^{2}}\bigr)$; in
    the form <a href="#eq:phi" data-reference-type="eqref"
    data-reference="eq:phi">[eq:phi]</a>,
    $\varphi(\sigma)=1/(4\pi)+\pi\sigma^{2}$ for both signs \[4\].

2.  *Kerr Sen at fixed charge $Q$.*
    $S_{\pm}=2\pi\bigl(W\pm\sqrt{W^{2}-J^{2}}\bigr)$ with
    $W=M^{2}-Q^{2}/2$ \[14,15\].

3.  *Myers Perry in five dimensions with equal angular momenta
    $J_{1}=J_{2}=J$.* $S_{\pm}=2\pi\bigl(W\pm\sqrt{W^{2}-J^{2}}\bigr)$
    with $W=(\pi/8)\,\mu^{3/2}$ and $\mu=8M/(3\pi)$ \[16,17\].

4.  *Kerr with one spin in $d$ dimensions.* In the normalization of
    \[2\], relation <a href="#eq:phi" data-reference-type="eqref"
    data-reference="eq:phi">[eq:phi]</a> holds with
    $W=(4M/(d-2))^{(d-2)/(d-3)}$ and $\varphi(u)=(1+4u^{2})^{1/(d-3)}$.
    For $d=5$ this is $S=\sqrt{W^{2}-4J^{2}}$.

In (a), (b) and (c) the two signs are the outer and the inner horizon.
For the lower sign $\partial S/\partial M<0$: the temperature of the
inner horizon is negative \[4\].

# The diagonal form of the metric

<div id="prop:diag" class="proposition">

**Proposition 1**. *For a level homogeneous entropy
<a href="#eq:class" data-reference-type="eqref"
data-reference="eq:class">[eq:class]</a>, the Ruppeiner metric in the
coordinates $(M,j)$ is $$\label{eq:diag}
g=-\,W''(M)\,\alpha(j)\,dM^{2}-W(M)\,s''(j)\,dj^{2} ,$$ and in the
coordinates $(M,J)$ its determinant is $$\label{eq:det}
\det g=\frac{W''\,s''\,\alpha}{W} .$$*

</div>

<div class="proof">

*Proof.* By <a href="#eq:first" data-reference-type="eqref"
data-reference="eq:first">[eq:first]</a>, $dS=W'\alpha\,dM+s'\,dJ$.
Since $M$ and $J$ are the coordinates in which the Hessian is taken, a
second differentiation gives
$$\frac{\partial^{2}S}{\partial x^{a}\partial x^{b}}\,dx^{a}dx^{b}
=\bigl(W''\alpha\,dM+W'\alpha'\,dj\bigr)\,dM+s''\,dj\,dJ .$$ Now
$dJ=W\,dj+jW'\,dM$ and $\alpha'=-j\,s''$, so the two terms in $dM\,dj$
cancel and the right hand side is $W''\alpha\,dM^{2}+W s''\,dj^{2}$. The
determinant follows from $dM\wedge dJ=W\,dM\wedge dj$. ◻

</div>

<div id="rem:prior" class="remark">

*Remark 1*. (i) For Kerr, with $s_{\pm}$ of example (a), equation
<a href="#eq:diag" data-reference-type="eqref"
data-reference="eq:diag">[eq:diag]</a> is equation (29) of \[4\] on both
horizons; their coordinate $a=J/M^{2}$ is our $j$.

\(ii\) In terms of $\sigma=J/S$ and of the function $\varphi$ of
<a href="#eq:phi" data-reference-type="eqref"
data-reference="eq:phi">[eq:phi]</a>, the metric
<a href="#eq:diag" data-reference-type="eqref"
data-reference="eq:diag">[eq:diag]</a> reads $$\label{eq:sigmaform}
g=\frac{1}{\varphi-\sigma\varphi'}\Bigl[-W''(M)\,dM^{2}+W(M)\,\frac{\varphi''}{\varphi}\,d\sigma^{2}\Bigr],$$
because $\varphi-\sigma\varphi'=1/\alpha$. The bracket divided by $W'$
is the Weinhold metric, the Hessian of $M$ in $(S,J)$, and
$(\varphi-\sigma\varphi')/W'$ is the temperature. Equation
<a href="#eq:sigmaform" data-reference-type="eqref"
data-reference="eq:sigmaform">[eq:sigmaform]</a> is thus the conformal
relation between the two metrics used in \[2\]. The coordinate $J/S$ and
the diagonal Weinhold form are due to \[2\] for Kerr in any dimension,
and \[3\] treats the power law class. What
Proposition <a href="#prop:diag" data-reference-type="ref"
data-reference="prop:diag">1</a> adds is the arbitrary level function,
and the form <a href="#eq:diag" data-reference-type="eqref"
data-reference="eq:diag">[eq:diag]</a> in which $W$ and $s$ separate.

\(iii\) By <a href="#eq:det" data-reference-type="eqref"
data-reference="eq:det">[eq:det]</a> the metric is indefinite where
$W''s''\alpha/W<0$. This is the case on both branches of the family of
Section <a href="#sec:mirror" data-reference-type="ref"
data-reference="sec:mirror">5</a> when $WW''>0$.

</div>

# The curvature

<div id="prop:curv" class="proposition">

**Proposition 2**. *For a level homogeneous entropy
<a href="#eq:class" data-reference-type="eqref"
data-reference="eq:class">[eq:class]</a>, $$\label{eq:RS}
R\,S=-\frac{s}{2\alpha}\left[\Sigma_{W}+\frac{j\,s'''}{s''}+\frac{j^{2}s''}{\alpha}\right],$$
where $$\label{eq:sigmaW}
\Sigma_{W}=\frac{W'W'''}{W''^{2}}+\frac{W'^{2}}{W\,W''} .$$*

</div>

<div class="proof">

*Proof.* For a metric $E\,du^{2}+G\,dv^{2}$ the Gaussian curvature is
$$\label{eq:gauss}
K=-\frac{E_{vv}+G_{uu}}{2EG}+\frac{E_{u}G_{u}+E_{v}^{2}}{4E^{2}G}+\frac{E_{v}G_{v}+G_{u}^{2}}{4EG^{2}} ,$$
an algebraic identity in $E$, $G$ and their derivatives, valid for
either signature, and $R=2K$. Take $u=M$, $v=j$, $E=-W''\alpha$ and
$G=-W\beta$ with $\beta=s''$, as given by
<a href="#eq:diag" data-reference-type="eqref"
data-reference="eq:diag">[eq:diag]</a>. Then
$$K=\frac{1}{4W\alpha}\left[\frac{2(\alpha''+\beta)}{\beta}-\Sigma_{W}-\frac{\alpha'^{2}}{\alpha\beta}-\frac{\alpha'\beta'}{\beta^{2}}\right].$$
Since $\alpha'=-j\beta$ and $\alpha''=-\beta-j\beta'$, the bracket
equals $-\bigl[\Sigma_{W}+j\beta'/\beta+j^{2}\beta/\alpha\bigr]$, and
$RS=2KWs$. ◻

</div>

<div id="rem:linear" class="remark">

*Remark 2*. The level function enters
<a href="#eq:RS" data-reference-type="eqref"
data-reference="eq:RS">[eq:RS]</a> only through $\Sigma_{W}$, and
linearly. By <a href="#eq:first" data-reference-type="eqref"
data-reference="eq:first">[eq:first]</a> its coefficient is
$-s/(2\alpha)=-\tfrac12\,(\partial\ln S/\partial\ln W)^{-1}$. The
combination $\Sigma_{W}$ is invariant under $W\to cW$ and under affine
changes of $M$.

</div>

<div id="lem:sigma" class="lemma">

**Lemma 1**. *Let $W$, $W'$ and $W''$ be nonzero on an interval. Then
$\Sigma_{W}=2$ on that interval if and only if $W=c\,(M-M_{0})^{p}$ or
$W=c\,e^{\lambda M}$, with constants $c$, $M_{0}$, $p$, $\lambda$.*

</div>

<div class="proof">

*Proof.* Put $h=W'/W''$ and $\ell=W/W'$. Then $h'=1-W'W'''/W''^{2}$ and
$\ell'=1-\ell/h$, so that $\Sigma_{W}=1-h'+h/\ell$. Hence $\Sigma_{W}=2$
if and only if $h'=(h-\ell)/\ell$. Together with $\ell'=(h-\ell)/h$ this
gives $(h/\ell)'=0$, so $h=\kappa\ell$ with a constant $\kappa$, and
$\ell'=1-1/\kappa$ is constant. If $\kappa=1$, $\ell$ is constant and
$W$ is an exponential. Otherwise $\ell=(M-M_{0})/p$ with
$1/p=1-1/\kappa$, and $W$ is a power of $M-M_{0}$. Conversely both
families give $\Sigma_{W}=2$ by direct substitution. ◻

</div>

<div id="rem:abp" class="remark">

*Remark 3* (Relation to the general curvature of \[3). \]For $W=M^{a}$
the class <a href="#eq:class" data-reference-type="eqref"
data-reference="eq:class">[eq:class]</a> is the case $a+b=0$ of \[3\],
and $\Sigma_{W}=2$. Equation (17) of that paper gives the curvature
scalar of the Hessian metric of $\psi=x^{a}f(x^{b}y)$ for general $a$,
$b$ and $f$, as a sum of seven terms. With $\psi=S$ it is the scalar
curvature of the Ruppeiner metric in the convention used here. At
$a+b=0$ three of the seven terms vanish, and the remaining four give
exactly <a href="#eq:RS" data-reference-type="eqref"
data-reference="eq:RS">[eq:RS]</a> with $\Sigma_{W}=2$:
$$R=-\frac{2ss''+j\,ss'''-2j\,s's''-j^{2}s's'''+j^{2}s''^{2}}{2\,s''\,M^{a}\,(s-js')^{2}} .$$
For power laws
Proposition <a href="#prop:curv" data-reference-type="ref"
data-reference="prop:curv">2</a> is therefore contained in \[3\]. What
it adds is the case of a level function that is not a power law, where
the only change is that the factor $2$ of the combination $2s''(s-js')$
in the numerator becomes $\Sigma_{W}$.

</div>

<div id="rem:ap50" class="remark">

*Remark 4*. For example (d), equation
<a href="#eq:RS" data-reference-type="eqref"
data-reference="eq:RS">[eq:RS]</a> gives
$$R\,S=-\frac{1-12\kappa u^{2}}{(1-4\kappa u^{2})(1+4\kappa u^{2})},\qquad \kappa=\frac{d-5}{d-3},\quad u=\frac JS ,$$
which is equation (50) of \[2\].

</div>

# The two branch family

Consider, for a level function $W$ with $W'W''\neq0$, the two entropies
$$\label{eq:family}
S_{\pm}=2\pi\Bigl(W(M)\pm\sqrt{W(M)^{2}-J^{2}}\Bigr),\qquad W>|J|>0 ,$$
and put $$\label{eq:nu}
\nu=\sqrt{1-\frac{J^{2}}{W^{2}}}=\frac{S_{+}-S_{-}}{S_{+}+S_{-}}\in(0,1) .$$
One has $S_{+}+S_{-}=4\pi W$ and $S_{+}S_{-}=4\pi^{2}J^{2}$. Examples
(a), (b) and (c) of
Section <a href="#sec:examples" data-reference-type="ref"
data-reference="sec:examples">2.3</a> are of this form.

<div id="thm:mirror" class="theorem">

**Theorem 1**. *For the family
<a href="#eq:family" data-reference-type="eqref"
data-reference="eq:family">[eq:family]</a>, $$\label{eq:split}
R_{\pm}S_{\pm}=-\frac12\pm D,\qquad D=\frac{(3-\Sigma_{W})\,\nu}{2}-\frac1\nu .$$
Consequently, for every level function, $$\label{eq:sum}
R_{+}S_{+}+R_{-}S_{-}=-1 .$$*

</div>

<div class="proof">

*Proof.* The family <a href="#eq:family" data-reference-type="eqref"
data-reference="eq:family">[eq:family]</a> is
<a href="#eq:class" data-reference-type="eqref"
data-reference="eq:class">[eq:class]</a> with $s_{\pm}=2\pi(1\pm\nu)$
and $\nu=\sqrt{1-j^{2}}$. For the upper sign,
$$s'=-\frac{2\pi j}{\nu},\qquad s''=-\frac{2\pi}{\nu^{3}},\qquad s'''=-\frac{6\pi j}{\nu^{5}},\qquad \alpha=\frac{2\pi(1+\nu)}{\nu} .$$
Hence $s/(2\alpha)=\nu/2$, $js'''/s''=3(1-\nu^{2})/\nu^{2}$ and
$j^{2}s''/\alpha=-(1-\nu)/\nu^{2}$, and
<a href="#eq:RS" data-reference-type="eqref"
data-reference="eq:RS">[eq:RS]</a> gives $$\label{eq:f}
R_{+}S_{+}=-\frac\nu2\left[\Sigma_{W}+\frac{2+\nu-3\nu^{2}}{\nu^{2}}\right]=f(\nu),
\qquad
f(x)=-\frac12-\frac1x+\frac{(3-\Sigma_{W})\,x}{2} .$$ The lower sign is
obtained by replacing $\nu$ by $-\nu$ in all these expressions, so that
$R_{-}S_{-}=f(-\nu)$. The sum is twice the even part of $f$, which is
the constant $-\tfrac12$, and $D$ is its odd part. ◻

</div>

The exchange of the two horizons is the involution $\nu\to-\nu$ of the
double cover <a href="#eq:family" data-reference-type="eqref"
data-reference="eq:family">[eq:family]</a>. Equation
<a href="#eq:sum" data-reference-type="eqref"
data-reference="eq:sum">[eq:sum]</a> states that the part of $RS$ which
is even under this involution does not depend on the level function or
on the state. The odd part carries $\Sigma_{W}$ and diverges in the
extremal limit $\nu\to0$.

<div id="cor:cross" class="corollary">

**Corollary 1**. *For the family
<a href="#eq:family" data-reference-type="eqref"
data-reference="eq:family">[eq:family]</a>, $$\label{eq:cross}
R_{+}S_{-}+R_{-}S_{+}=3+\frac{2\,(\Sigma_{W}-2)\,\nu^{2}}{1-\nu^{2}} .$$
The cross sum equals $3$ identically if and only if $\Sigma_{W}=2$, that
is, by Lemma <a href="#lem:sigma" data-reference-type="ref"
data-reference="lem:sigma">1</a>, if and only if the level function is a
power law or an exponential.*

</div>

<div class="proof">

*Proof.* $S_{\mp}/S_{\pm}=(1\mp\nu)/(1\pm\nu)$, and
<a href="#eq:split" data-reference-type="eqref"
data-reference="eq:split">[eq:split]</a>. ◻

</div>

#### Kerr.

Here $\Sigma_{W}=2$ and <a href="#eq:split" data-reference-type="eqref"
data-reference="eq:split">[eq:split]</a> is equivalent to
$$\label{eq:kerr}
R_{\pm}=\frac{1}{4\pi M^{2}}\mp\frac{1}{2\pi\sqrt{M^{4}-J^{2}}} .$$ In
\[4\] the entropy and the curvature scalar are written in coordinates
that cover both horizons, their equations (35) and (37). In our notation
they give $RS=f(\cos2\beta)$ with $\Sigma_{W}=2$, the outer horizon
being $\cos2\beta=\nu$ and the inner one $\cos2\beta=-\nu$. For Kerr,
relations <a href="#eq:kerrpair" data-reference-type="eqref"
data-reference="eq:kerrpair">[eq:kerrpair]</a> thus follow in one line
from \[4\], where the two branches are not combined.

#### Myers Perry in five dimensions with equal spins.

The level function is a power law, so $\Sigma_{W}=2$ and both branch
values are the Kerr ones as functions of $\nu$. In the normalization of
\[17\], where $S_{+}S_{-}=4J^{2}$, one has
$\nu=(S^{2}-4J^{2})/(S^{2}+4J^{2})$ on the outer branch, and
<a href="#eq:split" data-reference-type="eqref"
data-reference="eq:split">[eq:split]</a> becomes
$$R=-\frac{S\,(S^{2}+12J^{2})}{S^{4}-16J^{4}} ,$$ which is the Ruppeiner
curvature given in Section III.2 of \[17\]. Equal angular momenta in any
dimension are studied in \[18\].

#### Kerr Sen at fixed charge.

With $W=M^{2}-Q^{2}/2$ and $q=Q/M$, $$\label{eq:kerrsen}
\Sigma_{W}=\frac{2}{1-q^{2}/2},\qquad
D=\frac{(2-3q^{2})\,\nu}{2\,(2-q^{2})}-\frac1\nu,\qquad
R_{+}S_{-}+R_{-}S_{+}=3+\frac{4q^{2}\nu^{2}}{(2-q^{2})(1-\nu^{2})} .$$
The sum <a href="#eq:sum" data-reference-type="eqref"
data-reference="eq:sum">[eq:sum]</a> holds for every value of the
charge, while the split and the cross sum depend on it. This example
lies outside the class of \[3\], because its level function is not a
power law.

# The single branch companion

<div id="prop:odd" class="proposition">

**Proposition 3**. *Let $S=c\,\sqrt{W(M)^{2}-J^{2}}$ with a constant
$c>0$. Then $$\label{eq:odd}
R\,S=-\frac{\Sigma_{W}}{2}-\Bigl(1-\frac{\Sigma_{W}}{2}\Bigr)\frac{J^{2}}{W^{2}} .$$
In particular $RS=-1$ identically if and only if $\Sigma_{W}=2$.*

</div>

<div class="proof">

*Proof.* This is <a href="#eq:class" data-reference-type="eqref"
data-reference="eq:class">[eq:class]</a> with $s=c\,\nu$,
$\nu=\sqrt{1-j^{2}}$, for which $s'=-cj/\nu$, $s''=-c/\nu^{3}$,
$s'''=-3cj/\nu^{5}$ and $\alpha=c/\nu$. Equation
<a href="#eq:RS" data-reference-type="eqref"
data-reference="eq:RS">[eq:RS]</a> gives
$RS=-\tfrac{\nu^{2}}{2}\bigl[\Sigma_{W}+2j^{2}/\nu^{2}\bigr]$. ◻

</div>

Example (d) with $d=5$ is of this form, with a power law level function,
and <a href="#eq:odd" data-reference-type="eqref"
data-reference="eq:odd">[eq:odd]</a> is then $R=-1/S$: this is equation
(51) of \[2\]. For a family
<a href="#eq:family" data-reference-type="eqref"
data-reference="eq:family">[eq:family]</a> one has
$4\pi\sqrt{W^{2}-J^{2}}=S_{+}-S_{-}$. The number $-1$ therefore appears
in two places: on the single horizon of five dimensional Kerr with one
spin \[2\], and as the sum over the two horizons of a family
<a href="#eq:family" data-reference-type="eqref"
data-reference="eq:family">[eq:family]</a>. Both are consequences of
Proposition <a href="#prop:curv" data-reference-type="ref"
data-reference="prop:curv">2</a>. We do not know of a deeper reason that
would relate the two.

# The exact converse

<div id="thm:converse" class="theorem">

**Theorem 2**. *Let $k$ be a smooth positive function on an interval,
with $k'\neq0$, and for a level function $W$ with $W'W''\neq0$ consider
$$\label{eq:kclass}
S_{\pm}=2\pi\Bigl(W(M)\pm\sqrt{W(M)^{2}-k(J)}\Bigr),\qquad W^{2}>k ,$$
so that $S_{+}+S_{-}=4\pi W(M)$ and $S_{+}S_{-}=4\pi^{2}k(J)$. The
identity $R_{+}S_{+}+R_{-}S_{-}=-1$ holds for every level function $W$
if and only if $\sqrt k$ is affine: $$\label{eq:affine}
k(J)=(aJ+b)^{2} .$$*

</div>

<div class="proof">

*Proof.* If <a href="#eq:affine" data-reference-type="eqref"
data-reference="eq:affine">[eq:affine]</a> holds, the affine change of
coordinate $\hat J=aJ+b$ maps
<a href="#eq:kclass" data-reference-type="eqref"
data-reference="eq:kclass">[eq:kclass]</a> to
<a href="#eq:family" data-reference-type="eqref"
data-reference="eq:family">[eq:family]</a>. By the first invariance of
Section <a href="#sec:setting" data-reference-type="ref"
data-reference="sec:setting">2</a>, $R$ and $S$ are unchanged, and
Theorem <a href="#thm:mirror" data-reference-type="ref"
data-reference="thm:mirror">1</a> applies.

Conversely, put $\rho=\sqrt{W^{2}-k}$ and $X=2kk''-k'^{2}$. A direct
computation, described in
Appendix <a href="#app:converse" data-reference-type="ref"
data-reference="app:converse">10</a>, gives $$\label{eq:NDelta}
R_{+}S_{+}+R_{-}S_{-}+1=\frac{N}{A_{+}^{2}A_{-}^{2}},
\qquad
A_{\pm}=(k'^{2}+2k''\rho^{2})\,(W\pm\rho)\,W''-X\,W'^{2} ,$$ where $N$
is even in $\rho$ and, after the substitution $\rho^{2}=W^{2}-k$, is a
polynomial in $W$, $W'$, $W''$, $W'''$ whose coefficients are
polynomials in $k$, $k'$, $k''$, $k'''$. It has $25$ terms, and the
coefficient of the monomial $W''^{4}$ is $k^{2}X^{4}$. At a given state
the admissible values of $(W,W',W'',W''')$ form an open subset of
$\mathbb{R}^{4}$, defined by $W^{2}>k$ and $W'W''\neq0$, and a level
function can be chosen with any of these values. If the identity holds
for every level function, the polynomial $N$ vanishes on an open set,
hence identically, and in particular $k^{2}X^{4}=0$. Since $k>0$, this
gives $X=0$ at every point of the interval. Finally
$X=4k^{3/2}\,(\sqrt k)''$, so $\sqrt k$ is affine. ◻

</div>

<div id="rem:limit" class="remark">

*Remark 5*. The obstruction $X$ can be made explicit. The terms of $N$
of highest degree in $W''$ add up to
$kX\,(X-2k''W^{2})^{3}\,(k-W^{2})\,W''^{4}$, so that, at fixed $W$, $W'$
and $W'''$, $$\label{eq:limit}
R_{+}S_{+}+R_{-}S_{-}\;\longrightarrow\;-1+\frac{X\,\rho^{2}}{k\,(k'^{2}+2k''\rho^{2})}
\qquad\text{as } W''\to\infty .$$ For $k=J^{2}+C$ the limit is
$-1+C\rho^{2}/\bigl((J^{2}+C)(W^{2}-C)\bigr)$.

</div>

In the class <a href="#eq:kclass" data-reference-type="eqref"
data-reference="eq:kclass">[eq:kclass]</a> the entropy product does not
depend on the mass, by construction. Mass independence of the product,
which holds for a wide range of black holes \[8\], is therefore not
sufficient for <a href="#eq:sum" data-reference-type="eqref"
data-reference="eq:sum">[eq:sum]</a>. What
<a href="#eq:sum" data-reference-type="eqref"
data-reference="eq:sum">[eq:sum]</a> requires is that the product be the
square of an affine function of the fluctuating charge.

<div id="cor:kn" class="corollary">

**Corollary 2** (Kerr Newman at fixed charge). *For the Kerr Newman
black hole at fixed charge $Q$,
$$S_{\pm}=2\pi\Bigl(W\pm\sqrt{W^{2}-J^{2}-Q^{4}/4}\Bigr),\qquad W=M^{2}-\frac{Q^{2}}{2},$$
which is of the form <a href="#eq:kclass" data-reference-type="eqref"
data-reference="eq:kclass">[eq:kclass]</a> with $k=J^{2}+Q^{4}/4$ and
$2kk''-k'^{2}=Q^{4}$. The product $S_{+}S_{-}=\pi^{2}(4J^{2}+Q^{4})$
does not depend on the mass, and at fixed $J\neq0$ $$\label{eq:kn}
R_{+}S_{+}+R_{-}S_{-}=-1+\frac{Q^{4}\,(3M^{4}-J^{2})}{4M^{4}J^{2}}+O(Q^{6}) .$$
At $(M,J,Q)=(1,\tfrac12,\tfrac15)$ the sum is $-0.9950920929\ldots$ More
generally, for $k=J^{2}+C$ with a constant $C$ and any level function,
$$\label{eq:firstorder}
R_{+}S_{+}+R_{-}S_{-}=-1+\frac{C}{J^{2}}\Bigl[\nu^{2}\,(1+2AB+4A^{2})+A\,(1-8\nu^{2})\Bigr]+O(C^{2}),$$
with $A=W'^{2}/(WW'')$, $B=W'W'''/W''^{2}$ and
$\nu=\sqrt{1-J^{2}/W^{2}}$.*

</div>

<div class="proof">

*Proof.* The Kerr Newman entropies are $\pi(r_{\pm}^{2}+a^{2})$ with
$r_{\pm}=M\pm\sqrt{M^{2}-a^{2}-Q^{2}}$ and $a=J/M$, which is the stated
form. Equation <a href="#eq:firstorder" data-reference-type="eqref"
data-reference="eq:firstorder">[eq:firstorder]</a> is the first order
term in $C$ of the exact expression of the sum, and
<a href="#eq:kn" data-reference-type="eqref"
data-reference="eq:kn">[eq:kn]</a> is its value for $W=M^{2}-Q^{2}/2$
and $C=Q^{4}/4$, where $A=2+O(Q^{2})$ and $B=0$. ◻

</div>

# Discussion

The relations <a href="#eq:kerrpair" data-reference-type="eqref"
data-reference="eq:kerrpair">[eq:kerrpair]</a> of the Kerr black hole
have a simple origin. The entropies of the two horizons are the two
branches of one function of the form $W\,s(J/W)$, exchanged by an
involution, and the curvature formula
<a href="#eq:RS" data-reference-type="eqref"
data-reference="eq:RS">[eq:RS]</a> depends on the level function through
a single number. The sum over the two branches is blind to that number,
and the cross sum is not. The converse shows that the sum rule is tied
to this precise form: it is lost as soon as the entropy product, though
still independent of the mass, is not the square of an affine function
of the fluctuating charge.

Several limits should be kept in mind. First, the results depend on the
frame: they hold for the Hessian in $(M,J)$ at fixed values of all other
parameters. Other two dimensional frames, such as mass and electric
charge at fixed angular momentum, and the geometry with three
fluctuating charges, are not covered. Second, the inner horizon enters
only through its formal entropy, and nothing is claimed about its
physical status as a thermodynamic system. Third, with a cosmological
constant the entropies are not of the form
<a href="#eq:class" data-reference-type="eqref"
data-reference="eq:class">[eq:class]</a> in $(M,J)$, and we make no
statement about that case. Fourth, we have no physical interpretation of
the value $-1$, nor of its appearance both in
<a href="#eq:sum" data-reference-type="eqref"
data-reference="eq:sum">[eq:sum]</a> and on the single horizon of five
dimensional Kerr.

Two questions seem natural. Is there a geometric reason for
<a href="#eq:sum" data-reference-type="eqref"
data-reference="eq:sum">[eq:sum]</a> in the picture of \[3,4\], where
the state space is a wedge in a flat space and the Ruppeiner metric is
conformal to the flat one? And is there an analogue of
Theorem <a href="#thm:mirror" data-reference-type="ref"
data-reference="thm:mirror">1</a> for three fluctuating charges, where
the Kerr Newman family would be the first test?

# Statement on the use of an AI assistant

The author had no human collaborator. The work was done in sessions with
an AI assistant (Claude, Anthropic), which took part in every stage: the
derivations, the literature search and the drafting of the text. No
computed result rests on the assistant’s word: each one is stated as an
exact symbolic identity or as a numerical statement at stated precision,
and is replayed by the script described below, which the author has run.
The author takes full responsibility for the content.

# Code and data availability

The script `replay_short_article.py` checks every statement listed in
Appendix <a href="#app:replay" data-reference-type="ref"
data-reference="app:replay">9</a>. It uses Python with `sympy` and
`mpmath` only and runs in less than a minute. It includes a check of our
transcription of equations (17) and (18) of \[3\] against a direct
computation, for general exponents. The script is archived with this
article on Zenodo and in the repository
`github.com/vaneeckhoutnicolas/mirror-bh-thermodynamics`. The identifier
10.5281/zenodo.24139477 designates the Zenodo record as a whole and
resolves to its latest version. That record also holds an earlier and
longer version of this work (July 2026), which is superseded; its known
errors are listed in the file `ERRATA.md` of the record.

# Replay table

Each line gives a check tag of `replay_short_article.py` and the
statement it covers.

<div class="center">

  Tag        Statement
  ---------- -----------------------------------------------------------------------------------------------------------------------------------
  A1         first derivatives <a href="#eq:first" data-reference-type="eqref"
             data-reference="eq:first">[eq:first]</a>
  A2, A3     Proposition <a href="#prop:diag" data-reference-type="ref"
             data-reference="prop:diag">1</a>: <a href="#eq:diag" data-reference-type="eqref"
             data-reference="eq:diag">[eq:diag]</a> and <a href="#eq:det" data-reference-type="eqref"
             data-reference="eq:det">[eq:det]</a>
  A4         Proposition <a href="#prop:curv" data-reference-type="ref"
             data-reference="prop:curv">2</a>: <a href="#eq:RS" data-reference-type="eqref"
             data-reference="eq:RS">[eq:RS]</a>, by direct computation of the Hessian curvature
  A5         the same through <a href="#eq:gauss" data-reference-type="eqref"
             data-reference="eq:gauss">[eq:gauss]</a>
  A6         the form <a href="#eq:sigmaform" data-reference-type="eqref"
             data-reference="eq:sigmaform">[eq:sigmaform]</a>
  B1, B2     Lemma <a href="#lem:sigma" data-reference-type="ref"
             data-reference="lem:sigma">1</a>
  B3, C6     Kerr Sen: <a href="#eq:kerrsen" data-reference-type="eqref"
             data-reference="eq:kerrsen">[eq:kerrsen]</a>
  C0 to C2   Theorem <a href="#thm:mirror" data-reference-type="ref"
             data-reference="thm:mirror">1</a>: <a href="#eq:split" data-reference-type="eqref"
             data-reference="eq:split">[eq:split]</a>, <a href="#eq:sum" data-reference-type="eqref"
             data-reference="eq:sum">[eq:sum]</a>, <a href="#eq:f" data-reference-type="eqref"
             data-reference="eq:f">[eq:f]</a>
  C3         Corollary <a href="#cor:cross" data-reference-type="ref"
             data-reference="cor:cross">1</a>: <a href="#eq:cross" data-reference-type="eqref"
             data-reference="eq:cross">[eq:cross]</a>
  C4         Kerr: <a href="#eq:kerr" data-reference-type="eqref"
             data-reference="eq:kerr">[eq:kerr]</a>
  C5         Remark <a href="#rem:prior" data-reference-type="ref"
             data-reference="rem:prior">1</a> (iii)
  D1         Theorem <a href="#thm:mirror" data-reference-type="ref"
             data-reference="thm:mirror">1</a> again, by a route that does not use Propositions <a href="#prop:diag" data-reference-type="ref"
             data-reference="prop:diag">1</a> and <a href="#prop:curv" data-reference-type="ref"
             data-reference="prop:curv">2</a>
  D2 to D6   Theorem <a href="#thm:converse" data-reference-type="ref"
             data-reference="thm:converse">2</a>, the limit <a href="#eq:limit" data-reference-type="eqref"
             data-reference="eq:limit">[eq:limit]</a> and Appendix <a href="#app:converse" data-reference-type="ref"
             data-reference="app:converse">10</a>
  E1 to E5   Corollary <a href="#cor:kn" data-reference-type="ref"
             data-reference="cor:kn">2</a>: <a href="#eq:kn" data-reference-type="eqref"
             data-reference="eq:kn">[eq:kn]</a>, <a href="#eq:firstorder" data-reference-type="eqref"
             data-reference="eq:firstorder">[eq:firstorder]</a> and the numerical value
  F1         Remark <a href="#rem:prior" data-reference-type="ref"
             data-reference="rem:prior">1</a> (i): equation (29) of \[4\]
  F2         equations (35) and (37) of \[4\], and <a href="#eq:kerrpair" data-reference-type="eqref"
             data-reference="eq:kerrpair">[eq:kerrpair]</a>
  F3, F4     example (c) and the curvature of \[17\]
  F5         Remark <a href="#rem:ap50" data-reference-type="ref"
             data-reference="rem:ap50">4</a>: equations (50) and (51) of \[2\]
  F6         Proposition <a href="#prop:odd" data-reference-type="ref"
             data-reference="prop:odd">3</a>: <a href="#eq:odd" data-reference-type="eqref"
             data-reference="eq:odd">[eq:odd]</a>
  F7         Remark <a href="#rem:abp" data-reference-type="ref"
             data-reference="rem:abp">3</a>: equation (17) of \[3\] at $a+b=0$
  F8         equations (17) and (18) of \[3\] for general exponents, and the sign convention

</div>

# The computation behind Theorem <a href="#thm:converse" data-reference-type="ref"
data-reference="thm:converse">2</a>

The entropies <a href="#eq:kclass" data-reference-type="eqref"
data-reference="eq:kclass">[eq:kclass]</a> are $S_{\pm}=2\pi(W\pm\rho)$
with $\rho^{2}=W^{2}-k$, so that
$$\frac{\partial\rho}{\partial M}=\frac{WW'}{\rho},\qquad \frac{\partial\rho}{\partial J}=-\frac{k'}{2\rho} .$$
With these two rules every derivative of $S_{\pm}$ is a rational
function of $\rho$, of $W$, $W'$, $W''$, $W'''$ and of $k'$, $k''$,
$k'''$. The scalar curvature of the metric
<a href="#eq:rup" data-reference-type="eqref"
data-reference="eq:rup">[eq:rup]</a> is computed from the derivatives of
$S$ up to third order, and the lower sign is obtained from the upper one
by $\rho\to-\rho$. The result is
<a href="#eq:NDelta" data-reference-type="eqref"
data-reference="eq:NDelta">[eq:NDelta]</a>.

The numerator $N$ is even in $\rho$. After the substitution
$\rho^{2}=W^{2}-k$ it is a polynomial in $(W,W',W'',W''')$ with $25$
terms, of degree four in $W''$ and of degree one in $W'''$. Three facts
about it are used or recorded.

1.  The coefficient of the monomial $W''^{4}$ is $k^{2}X^{4}$. This is
    the only fact used in the proof of
    Theorem <a href="#thm:converse" data-reference-type="ref"
    data-reference="thm:converse">2</a>.

2.  The terms of degree four in $W''$ add up to
    $kX\,(X-2k''W^{2})^{3}\,(k-W^{2})\,W''^{4}$, and the coefficient of
    $W''^{4}$ in $A_{+}^{2}A_{-}^{2}$ is $k^{2}\,(2k''W^{2}-X)^{4}$.
    Their quotient is the limit
    <a href="#eq:limit" data-reference-type="eqref"
    data-reference="eq:limit">[eq:limit]</a>.

3.  As a cross check, the $25$ coefficients generate an ideal of
    $\mathbb{Q}[k,k',k'',k''']$ whose reduced Gröbner basis, for the
    lexicographic order $k'''>k''>k'>k$, is $$\begin{gathered}
    k^{2}k'k''^{2}k''',\qquad k\,k'^{3}k''k''',\qquad k'^{5}k''',\qquad k''^{2}\,X\,(2kk''+k'^{2}),\\
    k'^{2}k''^{2}\,X,\qquad k'^{4}k''\,X,\qquad k'^{6}\,X .
    \end{gathered}$$ For $k'\neq0$ its zero set is $k'''=0$ and $X=0$.
    No further condition is hidden in the other coefficients, since
    $X=0$ on an interval implies $k'''=0$.

These statements are replayed by checks D2 to D6. Run with the argument
`coefficients`, the script also prints the $25$ coefficients.

<div class="thebibliography">

99

G. Ruppeiner, Rev. Mod. Phys. 67 (1995) 605; erratum 68 (1996) 313.

J. E. Åman and N. Pidokrajt, Phys. Rev. D 73 (2006) 024017,
arXiv:hep-th/0510139.

J. E. Åman, I. Bengtsson and N. Pidokrajt, Gen. Rel. Grav. 38 (2006)
1305, arXiv:gr-qc/0601119.

J. E. Åman, I. Bengtsson and N. Pidokrajt, Entropy 17 (2015) 6503,
doi:10.3390/e17096503, arXiv:1507.06097.

A. Curir, Nuovo Cimento B 51 (1979) 262.

I. Okamoto and O. Kaburaki, Mon. Not. R. Astron. Soc. 255 (1992) 539.

M. Ansorg and J. Hennig, Phys. Rev. Lett. 102 (2009) 221102.

M. Cvetič, G. W. Gibbons and C. N. Pope, Phys. Rev. Lett. 106 (2011)
121301.

A. Castro and M. J. Rodriguez, Phys. Rev. D 86 (2012) 024008.

B. Chen, S. X. Liu and J. J. Zhang, JHEP 11 (2012) 017.

G. Ahn, I. Bae, G. Jang and Y. Kwon, arXiv:2605.08235.

A. Hankey and H. E. Stanley, Phys. Rev. B 6 (1972) 3515.

H. Quevedo, M. N. Quevedo and A. Sánchez, arXiv:1812.10599.

A. Sen, Phys. Rev. Lett. 69 (1992) 1006.

P. Pradhan, Eur. Phys. J. C 76 (2016) 131; erratum 81 (2021) 896;
arXiv:1503.04514.

R. C. Myers and M. J. Perry, Ann. Phys. 172 (1986) 304.

A. Bravetti, D. Momeni, R. Myrzakulov and A. Altaibayeva, Adv. High
Energy Phys. 2013 (2013) 549808, arXiv:1303.2077.

J. E. Åman and N. Pidokrajt, Eur. Phys. J. C 73 (2013) 2601,
arXiv:1004.5550.

</div>
