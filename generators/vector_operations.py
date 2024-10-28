# generators/vector_operations.py

import random
from utils.config import Config

def generate_vector_addition(problem_length):
    a = [random.randint(Config.NUM_RANGE[0], Config.NUM_RANGE[1])
         for _ in range(problem_length)]
    b = [random.randint(Config.NUM_RANGE[0], Config.NUM_RANGE[1])
         for _ in range(problem_length)]
    c = [a[i] + b[i] for i in range(problem_length)]
    return a, b, c

def generate_vector_subtraction(problem_length):
    a = [random.randint(Config.NUM_RANGE[0], Config.NUM_RANGE[1])
         for _ in range(problem_length)]
    b = [random.randint(Config.NUM_RANGE[0], Config.NUM_RANGE[1])
         for _ in range(problem_length)]
    c = [a[i] - b[i] for i in range(problem_length)]
    return a, b, c

def generate_vector_scalar_multiplication(problem_length):
    a = [random.randint(Config.NUM_RANGE[0], Config.NUM_RANGE[1])
         for _ in range(problem_length)]
    b = random.randint(Config.NUM_RANGE[0], Config.NUM_RANGE[1])
    c = [a[i] * b for i in range(problem_length)]
    return a, b, c