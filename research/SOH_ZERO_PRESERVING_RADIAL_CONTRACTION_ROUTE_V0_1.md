# SOH Zero-Preserving Radial Contraction Route v0.1

Status: **EXACT DISCRETENESS REDUCTION / CANDIDATE DYNAMICAL INCOMING EDGE / RH OPEN**

## 1. Exact input from mathlib

Mathlib proves that the zero set of the Riemann zeta function is a discrete
subset of the complex plane. Therefore any sequence of zeta zeros converging
to a zeta zero is eventually constant.

This has now been packaged in Lean as:

`SecretOfAHalfFormal.ZeroAccumulation.zetaZero_sequence_eventually_eq_limit`.

For a map (F:mathbb C	omathbb C), if

[
zeta(z)=0Longrightarrow zeta(F(z))=0
]

and the orbit (F^n(z_0)) converges to a zeta zero (ho), then Lean proves

[
oxed{F^n(z_0)=hoquad	ext{for all sufficiently large }n.}
]

Consequently a zero-preserving orbit cannot remain distinct from its limiting
zero at every finite step.

## 2. Radial projective coordinate

Use

[
u=Omega(s)=rac{s}{1-s},qquad q=|u|.
]

The critical line is exactly

[
Re(s)=rac12iff q=1.
]

The Stage-D Collatz word gives the real contraction

[
W_r(q)=rac{3q+1}{4},
]

with

[
W_r(q)-1=rac34(q-1)
]

and unique fixed point (q=1).

Thus every real radius satisfies

[
W_r^n(q)longrightarrow1.
]

## 3. Candidate phase-preserving lift

For (u
e0), a natural lift of the radial selector is

[
mathcal R(u)
=
rac{W_r(|u|)}{|u|},u.
]

It preserves the angular coordinate and changes only the projective radius:

[
|mathcal R(u)|=W_r(|u|).
]

Hence

[
mathcal R^n(u)
longrightarrow
rac{u}{|u|}.
]

The limiting point lies on the unit circle and therefore corresponds, through
(Omega^{-1}), to the Riemann critical line.

## 4. Conditional zero-set theorem schema

Suppose one independently proves that the lifted map, or another map with the
same radial contraction property, preserves the non-trivial zeta-zero set:

[
oxed{
zeta(s)=0
Longrightarrow
zeta(F(s))=0.
}
]

If an off-axis zero produced an orbit converging to a critical-line zero while
never reaching it at a finite step, this would contradict discreteness of the
zeta zero set.

Accordingly a viable proof route would have the form

[
oxed{
egin{array}{c}
	ext{independent zero-set invariance}\
+ 	ext{strict radial contraction}\
+ 	ext{finite critical-line zero limit}\
+ 	ext{no finite landing off the fixed layer}
end{array}
Longrightarrow
mathrm{RH}.
}
]

## 5. Firewall

The crucial statement is **not proved**:

[
zeta(s)=0Longrightarrowzeta(F(s))=0
]

for the radial Collatz lift.

It must not be inferred merely from:

- the functional equation;
- reciprocal/conjugation symmetry;
- the fact that the Collatz word contracts (q) to one;
- numerical evidence;
- the RH-equivalent seam condition.

Indeed the holomorphic affine contraction (umapsto(3u+1)/4) cannot preserve
all non-trivial zeta zeros, since every orbit would converge to (u=1), whose
inverse projective point is (s=1/2), not a zeta zero. Any viable candidate
must preserve enough angular/spectral information for the limiting point to be
an actual critical-line zero.

## 6. Current incoming-edge target

The sharpened research target is therefore:

[
oxed{
	ext{derive a zero-preserving, phase/spectral-compatible radial contraction}
}
]

from arithmetic, Weil-operator, theta-kernel, or slice-gluing structure without
assuming an RH-equivalent premise.

If such a map is obtained, the topological endgame is already formalized in
Lean using discreteness of zeta zeros.

`proof_of_rh = false`
