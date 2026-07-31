# DHSE-001 — Stage I preregistration: word-length robustness

## Status before execution

- Branch: `experiment/dhse-001` only.
- No Stage I result is recorded in this document.
- No merge, pull request, monograph inclusion or claim promotion is authorized.

## Scientific question

Does the centre-blind excess at the self-dual odds coordinate `q=1`
persist when the operator-word length is varied, without changing the
coefficient universe, centre set, projective radius or whole-line forcing
predicate after observing results?

## Frozen operator universe

- complete coefficient cube `K=6`;
- matrices `[a,b,c,d]` with
  - `1 <= a,d <= 6`,
  - `0 <= b,c <= 6`,
  - `ad-bc > 0`;
- expected admissible map count: `1073`;
- ordered branch pairs `(L,R)`: `1073^2 = 1,151,329`;
- exact integer arithmetic only;
- reciprocal conjugation `[a,b,c,d] -> [d,c,b,a]` must close the universe.

## Frozen words

Every binary word over `{L,R}` is included at each declared length:

- length 1: `2` words;
- length 2: `4` words;
- length 3: `8` words;
- length 4: `16` words.

Words are applied from left to right. No word is selected or excluded after
execution.

## Frozen centres and radius

The nine reciprocal odds centres are

`1/16, 1/8, 1/4, 1/2, 1, 2, 4, 8, 16`.

The target is `q=1`, equivalent to probability `p=1/2`.

The projective residual remains

`d_q(z)=|z-q|/(z+q)`

with the unchanged radius `1/10`. Thus the target interval around `q` is

`[9q/11, 11q/9]`.

## Frozen forcing predicate

For a composed positive Möbius map

`W(z)=(A*z+B)/(C*z+D)`,

a pair-word event forces centre `q` only when the image of the entire positive
line lies inside the target interval:

- `C > 0`;
- `B/D >= 9q/11`;
- `A/C <= 11q/9`.

The same predicate and code path are used for every centre, word and length.

## Primary decision rule

For each length separately, aggregate all words of that length.

A length passes when:

1. `q=1` has strictly more forcing events than every control centre;
2. its count is at least `5/4` of the median count of the eight controls;
3. every reciprocal centre pair has exactly equal counts.

The preregistered conclusion is:

- `WORD_LENGTH_ROBUST_HALF_EXCESS` if lengths 1–4 all pass;
- `MULTISTEP_HALF_EXCESS` if length 1 fails but lengths 2–4 all pass;
- `PARTIAL_WORD_LENGTH_PERSISTENCE` if at least two declared lengths pass but neither rule above applies;
- `WORD_LENGTH_UNSTABLE` otherwise.

## Secondary diagnostics

Recorded but unable to alter the primary conclusion:

- complete centre-count profile at each length;
- target forcing rate;
- target-to-control-median ratio;
- contribution of every individual word;
- reversal/complement symmetry diagnostics;
- successive target-rate ratios.

## Interpretation boundary

A positive result would establish persistence only for complete binary words of
lengths 1–4 in the declared uniform `K=6` integer Möbius universe. It would not
prove an all-length or all-operator theorem. IEEE `NaN` remains outside the
state space and no Riemann-hypothesis claim is promoted.
