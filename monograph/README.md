# Monograph build

The monograph is modular LaTeX. Its entry point is `main.tex`.

## Reproducible build

From the repository root:

```bash
python scripts/generate_monograph_assets.py
python scripts/run_phasenav_weil_hermite_ladder.py
python scripts/run_zero_undefined_duality.py
cd monograph
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Outputs

- `main.pdf` — compiled 97-page Version 0.4 monograph;
- `figures/` — deterministic PDF and PNG figures;
- `generated/` — generated LaTeX tables;
- `main.log` — TeX build log.

## Version 0.4 additions

- Chapter 17: explicit PhaseNav–Weil Hermite dense-core ladder;
- Chapter 18: zero–undefined reciprocal duality, spinor fixed state and Fisher–Rao midpoint;
- explicit NaN boundary guard;
- updated claim ledger and executable receipts.

## Claim boundary

The new reciprocal and information-geometric lemmas are exact. The interpretation of `UNDEFINED_BOTTOM` as an informational endpoint is exploratory. Global PhaseNav–Weil positivity, native zero closure, and the canonical bridge from every non-trivial zeta zero remain open. Version 0.4 does not claim a proof of the Riemann Hypothesis.
