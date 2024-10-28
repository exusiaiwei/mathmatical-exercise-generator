# main.py

from utils.config import Config
from generators.vector_operations import generate_vector_addition, generate_vector_subtraction, generate_vector_scalar_multiplication
from generators.matrix_operations import generate_matrix_addition, generate_matrix_subtraction, generate_matrix_multiplication
from generators.gaussian import GaussianElimination
from utils.file_handler import ExerciseFileHandler

def main():
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
        }#,
        #"Linear Algebra": {
        #    "Gaussian Elimination (Solution)": [],
        #    "Gaussian Elimination (RREF)": []
        #}
    }

    answers_by_type = {
        "Vector Arithmetic": {
            "Addition": [],
            "Subtraction": [],
            "Scalar Multiplication": []
        },
        "Matrix Arithmetic": {
            "Addition": [],
            "Subtraction": [],
            "Multiplication": []
        }#,
        #"Linear Algebra": {
        #    "Gaussian Elimination (Solution)": [],
        #    "Gaussian Elimination (RREF)": []
        #}
    }

    # Generate problems
    for i in range(Config.NUM_PROBLEMS):
        # Vector arithmetic problems
        # Addition
        a, b, c = generate_vector_addition(Config.PROBLEM_LENGTH)
        problem, answer = format_vector_problem_answer((a, b), c, '+', i+1)
        problems_by_type["Vector Arithmetic"]["Addition"].append(problem)
        answers_by_type["Vector Arithmetic"]["Addition"].append(answer)

        # Subtraction
        a, b, c = generate_vector_subtraction(Config.PROBLEM_LENGTH)
        problem, answer = format_vector_problem_answer((a, b), c, '-', i+1)
        problems_by_type["Vector Arithmetic"]["Subtraction"].append(problem)
        answers_by_type["Vector Arithmetic"]["Subtraction"].append(answer)

        # Scalar multiplication
        a, k, c = generate_vector_scalar_multiplication(Config.PROBLEM_LENGTH)
        problem = f"Let $\\mathbf{{u}} = \\begin{{bmatrix}} {a[0]} \\\\ {a[1]} \\\\ {a[2]} \\end{{bmatrix}}$. Compute ${k}\\mathbf{{v}}$."
        latex_vector = ' \\\\ '.join(map(str, c))
        answer = f"{i+1}: $\\begin{{bmatrix}} {latex_vector} \\end{{bmatrix}}$"
        problems_by_type["Vector Arithmetic"]["Scalar Multiplication"].append(problem)
        answers_by_type["Vector Arithmetic"]["Scalar Multiplication"].append(answer)

        # Matrix arithmetic problems
        # Addition
        A, B, C = generate_matrix_addition(Config.PROBLEM_LENGTH)
        problem, answer = format_matrix_problem_answer(A, B, C, '+', i+1)
        problems_by_type["Matrix Arithmetic"]["Addition"].append(problem)
        answers_by_type["Matrix Arithmetic"]["Addition"].append(answer)

        # Subtraction
        A, B, C = generate_matrix_subtraction(Config.PROBLEM_LENGTH)
        problem, answer = format_matrix_problem_answer(A, B, C, '-', i+1)
        problems_by_type["Matrix Arithmetic"]["Subtraction"].append(problem)
        answers_by_type["Matrix Arithmetic"]["Subtraction"].append(answer)

        # Multiplication
        A, B, C = generate_matrix_multiplication(Config.PROBLEM_LENGTH)
        problem, answer = format_matrix_problem_answer(A, B, C, '\\cdot', i+1)
        problems_by_type["Matrix Arithmetic"]["Multiplication"].append(problem)
        answers_by_type["Matrix Arithmetic"]["Multiplication"].append(answer)

        # Gaussian elimination problems
        #gaussian = GaussianElimination()
        #augmented, rref, solution = gaussian.#generate_problem(Config.PROBLEM_LENGTH)
        #problem, rref_answer, solution_answer = format_gaussian_problem_answer(
        #    augmented, rref, solution, i+1)
        #problems_by_type["Linear Algebra"]["Gaussian Elimination (Solution)"].append(problem)
        #answers_by_type["Linear Algebra"]["Gaussian Elimination (Solution)"].append(solution_answer)
        #answers_by_type["Linear Algebra"]["Gaussian Elimination (RREF)"].append(rref_answer)

    # 格式化内容
    content = format_problems_content(problems_by_type, answers_by_type)

    # 处理文件生成
    file_handler = ExerciseFileHandler()
    output_name = file_handler.prepare_exercise_file(
        content,
        Config.NUM_PROBLEMS
    )

    print(f"Generated exercise {output_name}")

def format_vector_problem_answer(problem, answer, operation, index):
    vector_elements_u = ' \\\\ '.join(map(str, problem[0]))
    vector_elements_v = ' \\\\ '.join(map(str, problem[1]))
    answer_elements = ' \\\\ '.join(map(str, answer))

    problem_str = f"Let $\\mathbf{{u}} = \\begin{{bmatrix}} {vector_elements_u} \\end{{bmatrix}}$ and $\\mathbf{{v}} = \\begin{{bmatrix}} {vector_elements_v} \\end{{bmatrix}}$. Compute $\\mathbf{{u}} {operation} \\mathbf{{v}}$."
    answer_str = f"{index}: $\\begin{{bmatrix}} {answer_elements} \\end{{bmatrix}}$"
    return problem_str, answer_str

def format_matrix_problem_answer(A, B, C, operation, index):
    def matrix_to_latex(matrix):
        rows = []
        for i in range(matrix.shape[0]):
            rows.append(' & '.join(map(str, matrix[i])))
        return ' \\\\ '.join(rows)

    problem_str = f"Let $A = \\begin{{bmatrix}} {matrix_to_latex(A)} \\end{{bmatrix}}$ and $B = \\begin{{bmatrix}} {matrix_to_latex(B)} \\end{{bmatrix}}$. Compute $A {operation} B$."
    answer_str = f"{index}: $\\begin{{bmatrix}} {matrix_to_latex(C)} \\end{{bmatrix}}$"
    return problem_str, answer_str

def format_gaussian_problem_answer(augmented, rref, solution, index):
    def matrix_to_latex(matrix):
        rows = []
        for i in range(matrix.shape[0]):
            rows.append(' & '.join(map(str, matrix[i])))
        return ' \\\\ '.join(rows)

    problem_str = f"Solve the system of linear equations represented by the augmented matrix: $\\begin{{bmatrix}} {matrix_to_latex(augmented)} \\end{{bmatrix}}$"
    rref_str = f"{index}: RREF = $\\begin{{bmatrix}} {matrix_to_latex(rref)} \\end{{bmatrix}}$"
    solution_str = f"{index}: x = $\\begin{{bmatrix}} {matrix_to_latex(solution)} \\end{{bmatrix}}$"
    return problem_str, rref_str, solution_str

def format_problems_content(problems, answers):
    content = []
    content.append("# Exercise\n")

    for problem_type, problems in problems.items():
        content.append(f"## {problem_type}\n")
        for operation, problem_list in problems.items():
            content.append(f"### {operation}\n")
            for i, problem in enumerate(problem_list, 1):
                content.append(f"{i}. {problem}\n")

    content.append("\n# Answer\n")
    for answer_type, answers in answers.items():
        content.append(f"## {answer_type}\n")
        for operation, answer_list in answers.items():
            content.append(f"### {operation}\n")
            for i in range(0, len(answer_list), 5):
                content.append(' '.join(answer_list[i:i+5]) + '\n')

    return '\n'.join(content)

if __name__ == "__main__":
    main()