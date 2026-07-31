# Monograph build

The monograph is modular LaTeX. Its entry point is `main.tex`.

## Reproducible build

From the repository root:

```bash
python scripts/generate_monograph_assets.py
python scripts/run_phasenav_weil_hermite_ladder.py
python scripts/run_zero_undefined_duality.py
python scripts/run_phasenav_weil_prime_tail.py
python scripts/run_phasenav_weil_adaptive_cutoff.py
cd monograph
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Outputs

- `main.pdf` — compiled Version 0.6 monograph;
- `figures/` — deterministic PDF and PNG figures;
- `generated/` — generated LaTeX tables;
- `main.log` — TeX build log.

## Version 0.6 additions

- Chapter 20: basis-adaptive prime cutoffs;
- elementary `h(U)/alpha(U)` tail envelope;
- coarse Hermite finite-section majorant;
- exact asymptotic collapse for every schedule `Q_N=exp(cN)`, `c>0`;
- deterministic sharp-certificate audit through `N=20`.

## Claim boundary

The adaptive diagonal tail is controlled when the cutoff grows exponentially
with the basis size. One fixed cutoff uniform in all basis sizes, positivity of
all infinite-cutoff sections, continuity of the full regularized Weil form and
the null-space implication to native closure remain open. Version 0.6 does not
claim a proof of the Riemann Hypothesis.
