# SOH Operator–Defect Crosswalk v0.1

Status: **EXACT GEOMETRIC CROSSWALK / LEAN OPERATOR INTERFACE / ANALYTIC INCOMING EDGE OPEN**

## 1. Two existing defects

The native theta/PhaseNav construction uses the half-axis closure defect

[
mathcal C(s)=left(Re(s)-rac12ight)^2.
]

The reciprocal–conjugation formulation uses

[
Delta_{m RC}(u)
=
left|u^{-1}-overline uight|^2,
qquad
u=Omega(s)=rac{s}{1-s}.
]

Both vanish on exactly the same locus, but they are not merely qualitatively
equivalent. Away from (s=0,1), they are related by an exact positive weight.

## 2. Exact algebraic identity

Write

[
A=|s|^2,qquad B=|1-s|^2.
]

Then

[
|u|^2=rac AB.
]

Since

[
u^{-1}-overline u
=
rac{1-|u|^2}{u},
]

we obtain

[
Delta_{m RC}(u)
=
rac{(1-|u|^2)^2}{|u|^2}
=
rac{(A-B)^2}{AB}.
]

But for (s=sigma+it),

[
A-B
=
sigma^2+t^2-igl((1-sigma)^2+t^2igr)
=
2sigma-1.
]

Therefore

[
oxed{
Delta_{m RC}(Omega(s))
=
rac{(2Re s-1)^2}
{|s|^2,|1-s|^2}
=
rac{4,mathcal C(s)}
{|s|^2,|1-s|^2}.
}
]

Hence, away from (0,1),

[
oxed{
Delta_{m RC}(Omega(s))=0
iff
mathcal C(s)=0
iff
Re(s)=rac12.
}
]

The denominator is strictly positive on every non-trivial zeta zero.

## 3. Consequence for the two proof routes

The PhaseNav closure defect and the reciprocal–conjugation orbit defect are
the same horizontal defect up to the explicit positive conformal weight

[
w(s)=rac{4}{|s|^2|1-s|^2}.
]

So the theta route and the projective orbit route do not have two independent
open geometric conditions. They have one open zero-to-defect implication
written in two metrics.

This does **not** prove the implication

[
zeta(s)=0Longrightarrow mathcal C(s)=0.
]

It only proves that any independent mechanism forcing either defect to vanish
forces the other one to vanish as well.

## 4. Operator-facing theorem interface

The formal Lean layer now exposes the following sufficient schema.

Let (E(s)) be an independently constructed scalar energy and let (c>0).
If every non-trivial zeta zero satisfies

[
E(s)=0
]

and

[
oxed{
c,Delta_{m RC}(Omega(s))le E(s),
}
]

then RH follows.

This is formalized as

`riemannHypothesis_of_coercive_zero_energy`

in

`SecretOfAHalfFormal/RadialDefect.lean`.

The theorem is purely an interface. It does not manufacture (E), the
coercivity constant, or the zero-mode relation.

## 5. C005 / theta common target

This sharpens the projection–complement programme. The desired operator result
is no longer vaguely “positivity implies the half-axis.” A sufficient incoming
edge has the concrete form

[
oxed{
mathcal E_s
ge
c,
rac{4(Re(s)-1/2)^2}
{|s|^2|1-s|^2}
}
]

for a canonical energy (mathcal E_s) that vanishes when the xi/zeta detector
vanishes.

A theta Hilbert-space realization could use a residual-energy coercivity
bound. A Weil/C005 realization could use a Schur-complement coercive lower
bound after the finite/complement split. Either route is acceptable if the
energy is independently derived and its zero-mode relation does not import RH
or an RH-equivalent criterion.

## 6. Current proof frontier

The remaining analytic obligation can now be stated narrowly:

[
oxed{
	ext{construct a canonical zero-mode energy }E
	ext{ and prove }
Ege c,Delta_{m RC}
	ext{ with }c>0.
}
]

The geometry, defect equivalence, seam equivalence, spectral-flow topology,
zeta-zero discreteness, and abstract coercivity endgame are already separated
from this incoming analytic theorem.

`proof_of_rh = false`
