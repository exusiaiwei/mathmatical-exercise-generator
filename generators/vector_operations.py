# generators/vector_operations.py

import random
from utils.config import Config


def generate_vector_addition(problem_length):
    a = [random.randint(Config.NUM_RANGE[0], Config.NUM_RANGE[1])
         for _ in range(problem_length)]
    b = [random.randint(Config.NUM_RANGE[0], Config.NUM_RANGE[1])
         for _ in range(problem_length)]
    c = [a[i] + b[i] for i in range(problem_length)]

    problem = (
        f"Let $\\mathbf{{u}} = \\begin{{bmatrix}} {a[0]} \\\\ {a[1]} \\\\ "
        f"{a[2]} \\end{{bmatrix}}$ and $\\mathbf{{v}} = \\begin{{bmatrix}} "
        f"{b[0]} \\\\ {b[1]} \\\\ {b[2]} \\end{{bmatrix}}$. "
        f"Compute $\\mathbf{{u}} + \\mathbf{{v}}$."
    )
    latex_vector = ' \\\\ '.join(map(str, c))
    answer = f"$\\begin{{bmatrix}} {latex_vector} \\end{{bmatrix}}$"

    return problem, answer


def generate_vector_subtraction(problem_length):
    a = [random.randint(Config.NUM_RANGE[0], Config.NUM_RANGE[1])
         for _ in range(problem_length)]
    b = [random.randint(Config.NUM_RANGE[0], Config.NUM_RANGE[1])
         for _ in range(problem_length)]
    c = [a[i] - b[i] for i in range(problem_length)]

    problem = (
        f"Let $\\mathbf{{u}} = \\begin{{bmatrix}} {a[0]} \\\\ {a[1]} \\\\ "
        f"{a[2]} \\end{{bmatrix}}$ and $\\mathbf{{v}} = \\begin{{bmatrix}} "
        f"{b[0]} \\\\ {b[1]} \\\\ {b[2]} \\end{{bmatrix}}$. "
        f"Compute $\\mathbf{{u}} - \\mathbf{{v}}$."
    )
    latex_vector = ' \\\\ '.join(map(str, c))
    answer = f"$\\begin{{bmatrix}} {latex_vector} \\end{{bmatrix}}$"

    return problem, answer


def generate_vector_scalar_multiplication(problem_length):
    a = [random.randint(Config.NUM_RANGE[0], Config.NUM_RANGE[1])
         for _ in range(problem_length)]
    b = random.randint(Config.NUM_RANGE[0], Config.NUM_RANGE[1])
    c = [a[i] * b for i in range(problem_length)]
    return a, b, c
