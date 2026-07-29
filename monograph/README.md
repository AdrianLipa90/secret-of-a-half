# Monograph build

The monograph is modular LaTeX. Its entry point is `main.tex`.

## Reproducible build

From the repository root:

```bash
python scripts/generate_monograph_assets.py
cd monograph
pdflatex -interaction=nonstopmode -halt-on-error main.tex
/usr/bin/bibtex.original main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

When `latexmk` and an unshadowed `bibtex` are available, the equivalent short build is:

```bash
cd monograph
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

## Outputs

- `main.pdf` — compiled monograph;
- `figures/` — deterministic PDF and PNG figures;
- `generated/` — LaTeX tables generated from the numerical CSV files;
- `main.log` — TeX build log.

## Claim boundary

The elementary balance, entropy, cancellation, involution and eta lemmas are proved in the text. The native theta bridge proves its covariance and closure identity, but the implication from every non-trivial zero to native self-dual closure remains open. Therefore Version 0.2 is an ansatz monograph with an executable native PhaseNav construction with a conditional critical-line theorem, not a proof of the Riemann Hypothesis.
