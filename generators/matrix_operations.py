# generators/matrix_operations.py

import numpy as np
import random
from utils.config import Config

import formatters.latex_formatter

def generate_matrix_addition(problem_length):
    A = np.random.randint(Config.NUM_RANGE[0], Config.NUM_RANGE[1],
                         (problem_length, problem_length))
    B = np.random.randint(Config.NUM_RANGE[0], Config.NUM_RANGE[1],
                         (problem_length, problem_length))
    C = A + B
    problem_str, answer_str = formatters.latex_formatter.format_matrix_problem_answer(A, B, C, "addition", 1)
    return problem_str, answer_str

def generate_matrix_subtraction(problem_length):
    A = np.random.randint(Config.NUM_RANGE[0], Config.NUM_RANGE[1],
                         (problem_length, problem_length))
    B = np.random.randint(Config.NUM_RANGE[0], Config.NUM_RANGE[1],
                         (problem_length, problem_length))
    C = A - B
    problem_str, answer_str = formatters.latex_formatter.format_matrix_problem_answer(A, B, C, "subtraction", 1)
    return problem_str, answer_str

def generate_matrix_multiplication(problem_length):
    A = np.random.randint(Config.NUM_RANGE[0], Config.NUM_RANGE[1],
                         (problem_length, problem_length))
    B = np.random.randint(Config.NUM_RANGE[0], Config.NUM_RANGE[1],
                         (problem_length, problem_length))
    C = np.dot(A, B)
    problem_str, answer_str = formatters.latex_formatter.format_matrix_problem_answer(A, B, C, "multiplication", 1)
    return problem_str, answer_str

def generate_matrix_multiplication_varied(problem_length):
    """Generate matrix multiplication problems with related but not identical dimensions"""
    m = problem_length
    n = problem_length + random.choice([-1, 0, 1])
    p = problem_length + random.choice([-1, 0, 1])

    # Ensure dimensions are not less than 2
    n = max(2, n)
    p = max(2, p)

    A = np.random.randint(Config.NUM_RANGE[0], Config.NUM_RANGE[1], (m, n))
    B = np.random.randint(Config.NUM_RANGE[0], Config.NUM_RANGE[1], (n, p))
    C = np.dot(A, B)
    problem_str, answer_str = formatters.latex_formatter.format_matrix_problem_answer(A, B, C, "multiplication", 1)
    return problem_str, answer_str
