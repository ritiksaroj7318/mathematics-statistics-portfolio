from projects.p01_linear_algebra.solution import run as linear_algebra
from projects.p02_numerical_methods.solution import run as numerical_methods
from projects.p03_statistics.solution import run as statistics
from projects.p04_optimization.solution import run as optimization
from projects.p05_ai_answer_evaluation.solution import run as evaluation

if __name__ == "__main__":
    for title, fn in [
        ("Linear algebra", linear_algebra),
        ("Numerical methods", numerical_methods),
        ("Statistics", statistics),
        ("Optimization", optimization),
        ("AI answer evaluation", evaluation),
    ]:
        print(f"\n{'=' * 12} {title} {'=' * 12}")
        fn()
