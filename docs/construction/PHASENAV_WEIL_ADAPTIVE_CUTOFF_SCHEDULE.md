# PhaseNav–Weil Adaptive Cutoff Schedule v0.6

## Purpose

Version 0.5 certified removal of the omitted prime-power tail for every fixed
finite Hermite section. Version 0.6 controls a diagonal sequence in which the
basis size and prime cutoff grow together.

This is not fixed-cutoff uniformity, global Weil positivity, or a proof of RH.

## Schedule

For basis size `N`, base cutoff `Q0`, and slope `c>0`, define

```text
U_N = log Q_N = max(log Q0, c N)
Q_N = ceil(exp(U_N))
```

When the base branch is active, `Q_N` is exactly `Q0`; no floating-point
successor of the integer cutoff is introduced.

The reciprocal tail coordinate becomes

```text
z_tail = 1 / log(x),    0 <= z_tail <= 1/U_N.
```

## Elementary envelope

For degree `d`, width `w`, and logarithmic coordinate `u`, let

```text
h_d(u) = u^(d+1) exp(-u^2/(4w^2)+u/2) / w^d
alpha_d(u) = u/(2w^2) - 1/2 - (d+1)/u.
```

Because `alpha_d` is increasing, `alpha_d(U)>0` implies

```text
integral_U^infinity h_d(u) du <= h_d(U) / alpha_d(U).
```

For an `N x N` Hermite section, use the bounds

```text
maximum degree        = 2N-2
terms per entry       <= N
linearization factor  <= 2^(3N-3) (N-1)!
```

together with the row-sum norm. This gives the coarse certificate

```text
B_N(U) = [N^2 2^(3N-3) (N-1)! / pi]
         [U^(2N-1) exp(-U^2/(4w^2)+U/2)
          / (w^(2N-2) alpha_(2N-2)(U))].
```

## Asymptotic theorem

For every fixed `c>0`, setting `U_N=cN` yields

```text
log B_N(cN) = -c^2 N^2/(4w^2) + O(N log N).
```

Therefore `B_N(cN) -> 0`. The quadratic Gaussian decay dominates factorial,
polynomial, and finite-section growth.

## Declared audit

```text
w       = 0.8
Q0      = 100000
c       = 2
N       = 1..20
target  = 1e-12
```

The sharp v0.5 incomplete-gamma certificate is evaluated at each scheduled
cutoff. All sections pass. The maximum is

```text
3.280365246530569e-14 at N=5.
```

At `N=20`, the certified bound is approximately `6.58e-222`.

## Claims

- `SOH-L021` — exact adaptive-cutoff collapse theorem.
- `SOH-N006` — numerical certificate for the declared schedule through `N=20`.

Open:

- one fixed cutoff uniform in basis size;
- positivity of all infinite-cutoff sections;
- closure of the complete arithmetic form;
- null-space implication to native PhaseNav closure;
- `SOH-C005`.

The authoritative native source is
`construction/phasenav/secret_of_half_weil_adaptive_cutoff_schedule.pnv`.
