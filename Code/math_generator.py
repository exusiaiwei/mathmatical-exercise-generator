# This file will generate math problems for exercises, it can generate problems and answers in latex format, and save them into a markdown file.
# The problems will be generated in a random order, and the answers will be placed at the end of the file.

import random
import numpy as np

# 定义生成问题的数量
num_problems = 10

# 定义生成数字的范围
num_range = [-10, 10]

# 定义问题的长度
problem_length = 3

# 生成问题和答案的函数
def vector_addition(problem_length):
    a = [random.randint(num_range[0], num_range[1]) for i in range(problem_length)]
    b = [random.randint(num_range[0], num_range[1]) for i in range(problem_length)]
    c = [a[i] + b[i] for i in range(problem_length)]
    return a, b, c

def vector_subtraction(problem_length):
    a = [random.randint(num_range[0], num_range[1]) for i in range(problem_length)]
    b = [random.randint(num_range[0], num_range[1]) for i in range(problem_length)]
    c = [a[i] - b[i] for i in range(problem_length)]
    return a, b, c

def vector_scalar_multiplication(problem_length):
    a = [random.randint(num_range[0], num_range[1]) for i in range(problem_length)]
    b = random.randint(num_range[0], num_range[1])
    c = [a[i] * b for i in range(problem_length)]
    return a, b, c

# 格式化问题和答案
def format_problem_answer(problem, answer, operation, index):
    problem_str = f"Let $\\mathbf{{u}} = \\begin{{bmatrix}} {problem[0][0]} \\\\ {problem[0][1]} \\\\ {problem[0][2]} \\end{{bmatrix}}$ and $\\mathbf{{v}} = \\begin{{bmatrix}} {problem[1][0]} \\\\ {problem[1][1]} \\\\ {problem[1][2]} \\end{{bmatrix}}$. Compute $\\mathbf{{u}} {operation} \\mathbf{{v}}$."
    answer_str = f"{index}: $\\begin{{bmatrix}} {answer[0]} \\\\ {answer[1]} \\\\ {answer[2]} \\end{{bmatrix}}$"
    return problem_str, answer_str

# 保存到文件
def save_problems_by_type(filename, problems_by_type, answers_by_type):
    with open(filename, 'a') as file:
        file.write("# Exercise\n\n")
        for problem_type, problems in problems_by_type.items():
            file.write(f"## {problem_type}\n\n")
            for operation, problem_list in problems.items():
                file.write(f"### {operation}\n\n")
                for i, problem in enumerate(problem_list):
                    file.write(str(i+1) + '. ' + problem + '\n\n')
        file.write("# Answer\n\n")
        for problem_type, answers in answers_by_type.items():
            file.write(f"## {problem_type}\n\n")
            for operation, answer_list in answers.items():
                file.write(f"### {operation}\n\n")
                for i in range(0, len(answer_list), 5):
                    file.write(' '.join(answer_list[i:i+5]) + '\n\n')

# 生成问题和答案
problems_by_type = {
    "Vector Arithmetic": {
        "Addition": [],
        "Subtraction": [],
        "Scalar Multiplication": []
    },
    "Matrix Arithmetic": {
        "Addition": [],
        "Subtraction": [],
        "Multiplication": []
    }
}
answers_by_type = {
    "Vector Arithmetic": {
        "Addition": [],
        "Subtraction": []
    },
    "Matrix Arithmetic": {
        "Addition": [],
        "Subtraction": [],
        "Multiplication": []
    }
}

# 生成向量加法问题和答案
for i in range(num_problems):
    a, b, c = vector_addition(problem_length)
    problem, answer = format_problem_answer((a, b), c, '+', i+1)
    problems_by_type["Vector Arithmetic"]["Addition"].append(problem)
    answers_by_type["Vector Arithmetic"]["Addition"].append(answer)
for i in range(num_problems):
    a, b, c = vector_subtraction(problem_length)
    problem, answer = format_problem_answer((a, b), c, '-', i+1)
    problems_by_type["Vector Arithmetic"]["Subtraction"].append(problem)
    answers_by_type["Vector Arithmetic"]["Subtraction"].append(answer)

# 增加新的任务类型
def matrix_addition():
    A = np.random.randint(num_range[0], num_range[1], (2, 2))
    B = np.random.randint(num_range[0], num_range[1], (2, 2))
    C = A + B
    return A, B, C

def matrix_multiplication():
    A = np.random.randint(num_range[0], num_range[1], (2, 2))
    B = np.random.randint(num_range[0], num_range[1], (2, 2))
    C = np.dot(A, B)
    return A, B, C

def format_matrix_problem_answer(A, B, C, operation, index):
    problem_str = f"Let $A = \\begin{{bmatrix}} {A[0,0]} & {A[0,1]} \\\\ {A[1,0]} & {A[1,1]} \\end{{bmatrix}}$ and $B = \\begin{{bmatrix}} {B[0,0]} & {B[0,1]} \\\\ {B[1,0]} & {B[1,1]} \\end{{bmatrix}}$. Compute $A {operation} B$."
    answer_str = f"{index}: $\\begin{{bmatrix}} {C[0,0]} & {C[0,1]} \\\\ {C[1,0]} & {C[1,1]} \\end{{bmatrix}}$"
    return problem_str, answer_str

# 生成矩阵加法问题和答案
for i in range(num_problems):
    A, B, C = matrix_addition()
    problem, answer = format_matrix_problem_answer(A, B, C, '+', i+1)
    problems_by_type["Matrix Arithmetic"]["Addition"].append(problem)
    answers_by_type["Matrix Arithmetic"]["Addition"].append(answer)

for i in range(num_problems):
    A, B, C = matrix_addition()
    problem, answer = format_matrix_problem_answer(A, B, C, '-', i+1)
    problems_by_type["Matrix Arithmetic"]["Subtraction"].append(problem)
    answers_by_type["Matrix Arithmetic"]["Subtraction"].append(answer)

for i in range(num_problems):
    A, B, C = matrix_multiplication()
    problem, answer = format_matrix_problem_answer(A, B, C, '*', i+1)
    problems_by_type["Matrix Arithmetic"]["Multiplication"].append(problem)
    answers_by_type["Matrix Arithmetic"]["Multiplication"].append(answer)

# 保存到文件
save_problems_by_type('exercise.qmd', problems_by_type, answers_by_type)