# Monograph build

The monograph is modular LaTeX. Its entry point is `main.tex`.

## Reproducible build

From the repository root:

```bash
python scripts/generate_monograph_assets.py
python scripts/run_phasenav_weil_hermite_ladder.py
python scripts/run_zero_undefined_duality.py
python scripts/run_phasenav_weil_prime_tail.py
cd monograph
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Outputs

- `main.pdf` — compiled 103-page Version 0.5 monograph;
- `figures/` — deterministic PDF and PNG figures;
- `generated/` — generated LaTeX tables;
- `main.log` — TeX build log.

## Version 0.5 additions

- Chapter 19: reciprocal compactification of the logarithmic prime tail;
- exact monotonicity threshold and upper-incomplete-gamma tail formula;
- entrywise prime-tail certificates;
- finite-section operator-norm and Weyl eigenvalue enclosures;
- deterministic `N<=6`, `Q=100000` receipt.

## Claim boundary

Controlled prime-cutoff removal is proved for every fixed declared finite Hermite section. Uniform control as the basis size tends to infinity, positivity of all sections, continuity of the full regularized Weil form, and the null-space implication to native closure remain open. Version 0.5 does not claim a proof of the Riemann Hypothesis.
