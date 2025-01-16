# main.py

from utils.config import Config
from utils.file_handler import ExerciseFileHandler
from generators.vector_operations import (
    generate_vector_addition,
    generate_vector_subtraction,
    generate_vector_scalar_multiplication
)
from generators.matrix_operations import (
    generate_matrix_addition,
    generate_matrix_subtraction,
    generate_matrix_multiplication
)
from generators.matrix_properties import RREFGenerator, MatrixProperties
from formatters.latex_formatter import format_rref_problem
from generators.calculus_exercises import CalculusExercises

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
        },
        "Matrix Properties": {
            "Properties": [],
            "RREF": []
        },
        "Calculus": {
            "Limit": [],
            "Derivative": [],
            "Integral": [],
            "Partial Derivative": []
        }
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
        },
        "Matrix Properties": {
            "Properties": [],
            "RREF": []
        },
        "Calculus": {
            "Limit": [],
            "Derivative": [],
            "Integral": [],
            "Partial Derivative": []
        }
    }

    # Generate problems
    for i in range(Config.NUM_PROBLEMS):
        # Vector arithmetic problems
        # Addition
        problem, answer = generate_vector_addition(Config.PROBLEM_LENGTH)
        problems_by_type["Vector Arithmetic"]["Addition"].append(problem)
        answers_by_type["Vector Arithmetic"]["Addition"].append(answer)

        # Subtraction
        problem, answer = generate_vector_subtraction(Config.PROBLEM_LENGTH)
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
        problem, answer = generate_matrix_addition(Config.PROBLEM_LENGTH)
        problems_by_type["Matrix Arithmetic"]["Addition"].append(problem)
        answers_by_type["Matrix Arithmetic"]["Addition"].append(answer)

        # Subtraction
        problem, answer = generate_matrix_subtraction(Config.PROBLEM_LENGTH)
        problems_by_type["Matrix Arithmetic"]["Subtraction"].append(problem)
        answers_by_type["Matrix Arithmetic"]["Subtraction"].append(answer)

        # Multiplication
        problem, answer = generate_matrix_multiplication(Config.PROBLEM_LENGTH)
        problems_by_type["Matrix Arithmetic"]["Multiplication"].append(problem)
        answers_by_type["Matrix Arithmetic"]["Multiplication"].append(answer)

        # Calculus problems
        # Limit
        limit_exercise = CalculusExercises.generate_limit_exercise()
        problems_by_type["Calculus"]["Limit"].append(limit_exercise["problem"])
        answers_by_type["Calculus"]["Limit"].append(limit_exercise["answer"])

        # Derivative
        derivative_exercise = CalculusExercises.generate_derivative_exercise()
        problems_by_type["Calculus"]["Derivative"].append(derivative_exercise["problem"])
        answers_by_type["Calculus"]["Derivative"].append(derivative_exercise["answer"])

        # Integral
        integral_exercise = CalculusExercises.generate_integral_exercise()
        problems_by_type["Calculus"]["Integral"].append(integral_exercise["problem"])
        answers_by_type["Calculus"]["Integral"].append(integral_exercise["answer"])

        # Partial Derivative
        partial_derivative_exercise = CalculusExercises.generate_partial_derivative_exercise()
        problems_by_type["Calculus"]["Partial Derivative"].append(partial_derivative_exercise["problem"])
        answers_by_type["Calculus"]["Partial Derivative"].append(partial_derivative_exercise["answer"])

        problem, answer = MatrixProperties.generate_from_rref(Config.PROBLEM_LENGTH)
        problems_by_type["Matrix Properties"]["Properties"].append(problem)
        answers_by_type["Matrix Properties"]["Properties"].append(answer)

        # 添加 RREF 问题生成
        rref_data = RREFGenerator.generate_rref_problem(Config.PROBLEM_LENGTH)
        rref_problem, rref_answer = format_rref_problem(rref_data, i+1)
        problems_by_type["Matrix Properties"]["RREF"].append(rref_problem)
        answers_by_type["Matrix Properties"]["RREF"].append(rref_answer)
    # 格式化内容
    file_handler = ExerciseFileHandler()
    output_name = file_handler.prepare_exercise_file(
        problems_by_type,  # 直接传入 problems_by_type
        answers_by_type,   # 直接传入 answers_by_type
        Config.NUM_PROBLEMS
    )

    print(f"Generated exercise {output_name}")

if __name__ == "__main__":
    main()
