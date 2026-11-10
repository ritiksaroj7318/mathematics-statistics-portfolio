# Computational Mathematics & Statistics Portfolio

**Ritik Saroj**  
B.Sc. (Hons.) Mathematics | Computational Mathematics | Statistics | Python

This repository contains reproducible, independently prepared technical work samples demonstrating mathematical reasoning, numerical computation, statistical analysis, optimization, and systematic evaluation of computational results.

> **Scope note:** These are portfolio projects, not claims of paid AI-training employment, peer-reviewed research, or professional software contributions.

## Technical areas
- Linear algebra: numerical rank, least-squares estimation, conditioning
- Numerical methods: root finding and convergence checks
- Statistics: estimation, confidence intervals, hypothesis testing, regression diagnostics
- Optimization: constrained resource allocation using linear programming
- Model evaluation: structured checks for mathematical and computational correctness

## Projects

| Project | What it demonstrates | Main tools |
|---|---|---|
| [01 — Linear Algebra & Least Squares](projects/01_linear_algebra/README.md) | Solve overdetermined systems, residuals, conditioning | NumPy |
| [02 — Numerical Root Finding](projects/02_numerical_methods/README.md) | Bisection and Newton methods with convergence criteria | Python, NumPy |
| [03 — Statistical Analysis](projects/03_statistics/README.md) | Descriptive statistics, confidence intervals, regression | NumPy, SciPy |
| [04 — Optimization](projects/04_optimization/README.md) | Linear programming and constraint verification | SciPy |
| [05 — AI Math Answer Evaluation](projects/05_ai_answer_evaluation/README.md) | Rubric-based checking of reasoning, code, and numerical claims | Python |

## Run locally

```bash
git clone https://github.com/ritiksaroj7318/mathematics-statistics-portfolio.git
cd mathematics-statistics-portfolio
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
python run_all.py
```

## Repository structure

```text
.
├── README.md
├── requirements.txt
├── run_all.py
└── projects/
    ├── 01_linear_algebra/
    ├── 02_numerical_methods/
    ├── 03_statistics/
    ├── 04_optimization/
    └── 05_ai_answer_evaluation/
```

## About

I hold a B.Sc. (Hons.) in Mathematics from the University of Delhi and have experience teaching mathematics. This portfolio is intended to provide public, reproducible evidence of my current technical work in mathematical computation and evaluation.

**Contact:** Add your preferred professional email before publishing.
