from fractions import Fraction
import numpy as np

def format_vector_problem_answer(problem, answer, operation, index):
    vector_elements_u = ' \\\\ '.join([str(x) for x in problem[0]])
    vector_elements_v = ' \\\\ '.join([str(x) for x in problem[1]])
    answer_elements = ' \\\\ '.join([str(x) for x in answer])

    # 简化为只显示向量
    problem_str = (
        f"$\\mathbf{{u}} = \\begin{{bmatrix}} {vector_elements_u} \\end{{bmatrix}}$, "
        f"$\\mathbf{{v}} = \\begin{{bmatrix}} {vector_elements_v} \\end{{bmatrix}}$\n\n"
    )
    answer_str = f"$\\begin{{bmatrix}} {answer_elements} \\end{{bmatrix}}$"
    return problem_str, answer_str

def format_matrix_problem_answer(A, B, C, operation, index):
    def matrix_to_latex(matrix):
        rows = []
        for i in range(matrix.shape[0]):
            rows.append(' & '.join(str(x) for x in matrix[i]))
        return ' \\\\ '.join(rows)

    problem_str = f"Let $A = \\begin{{bmatrix}} {matrix_to_latex(A)} \\end{{bmatrix}}$ and $B = \\begin{{bmatrix}} {matrix_to_latex(B)} \\end{{bmatrix}}$"
    answer_str = f"{index}: $\\begin{{bmatrix}} {matrix_to_latex(C)} \\end{{bmatrix}}$"
    return problem_str, answer_str

def format_gaussian_problem_answer(augmented, rref, solution, index):
    def matrix_to_latex(matrix):
        rows = []
        for i in range(matrix.shape[0]):
            rows.append(' & '.join(str(x) for x in matrix[i]))
        return ' \\\\ '.join(rows)

    problem_str = f"Solve the system of linear equations represented by the augmented matrix: $\\begin{{bmatrix}} {matrix_to_latex(augmented)} \\end{{bmatrix}}$"
    rref_str = f"{index}: RREF = $\\begin{{bmatrix}} {matrix_to_latex(rref)} \\end{{bmatrix}}$"
    solution_str = f"{index}: x = $\\begin{{bmatrix}} {matrix_to_latex(solution)} \\end{{bmatrix}}$"
    return problem_str, rref_str, solution_str


def format_matrix_properties_problem(matrix_data, index):
    def matrix_to_latex(matrix, is_augmented=False):
        if matrix is None:
            return "\\text{does not exist}"
        rows = []
        for i in range(matrix.shape[0]):
            if is_augmented:
                left = ' & '.join(f"{Fraction(x).limit_denominator()}" for x in matrix[i,:matrix.shape[0]])
                right = ' & '.join(f"{Fraction(x).limit_denominator()}" for x in matrix[i,matrix.shape[0]:])
                rows.append(f"{left} & | & {right}")
            else:
                rows.append(' & '.join(f"{Fraction(x).limit_denominator()}" for x in matrix[i]))
        return ' \\\\ '.join(rows)

    def parse_row_numbers(desc):
        """从描述中提取行号"""
        numbers = [int(x) for x in desc.split() if x.isdigit()]
        return numbers[-2], numbers[-1]  # 返回最后两个数字作为行号

    def operation_to_latex(op_type, i, j, factor=None):
        if op_type == "swap":
            return f"r_{i} \\leftrightarrow r_{j}"
        elif op_type == "multiply":
            return f"r_{i} := {factor}r_{i}"
        elif op_type == "subtract":
            if factor == 1:
                return f"r_{j} := r_{j} - r_{i}"
            else:
                return f"r_{j} := r_{j} - ({factor})r_{i}"

    problem_str = (
        f"$A = \\begin{{bmatrix}} {matrix_to_latex(matrix_data['original'])} \\end{{bmatrix}}$\n\n"
    )

    answer_str = (
        "**Solution**\n\n"
        "**Row Operations:**\n\n"  # 移除斜体部分
    )


    # 添加消元步骤（使用数学符号）
    for i, step in enumerate(matrix_data['augmented_steps'][1:], 1):
        desc = step['description']
        try:
            if "Swap" in desc:
                r1, r2 = parse_row_numbers(desc)
                op = operation_to_latex("swap", r1, r2)
            elif "Multiply" in desc:
                row = int(''.join(filter(str.isdigit, desc.split("row")[1].split()[0])))
                factor = Fraction(''.join(c for c in desc.split("by")[1].strip() if c.isdigit() or c in '.-/'))
                op = operation_to_latex("multiply", row, None, factor)
            else:  # Subtract
                factor = Fraction(''.join(c for c in desc.split("times")[0] if c.isdigit() or c in '.-/'))
                r1, r2 = parse_row_numbers(desc)
                op = operation_to_latex("subtract", r1, r2, factor)
        except (ValueError, IndexError):
            # 如果解析失败，使用原始描述
            op = desc

        answer_str += (
            f"Step {i}: ${op}$\n"
            f"$\\begin{{bmatrix}} {matrix_to_latex(step['matrix'], True)} \\end{{bmatrix}}$\n\n"
        )

    answer_str += (
        "**Results:**\n\n"
        f"a) rank($A$) = {matrix_data['rank']}\n\n"
        f"b) nullity($A$) = {matrix_data['nullity']}\n\n"
        f"c) det($A$) = {Fraction(matrix_data['determinant']).limit_denominator()}\n\n"
    )
    # 修正逆矩阵和kernel的表示
    if matrix_data['inverse'] is not None:
        inverse_str = f"\\begin{{bmatrix}} {matrix_to_latex(matrix_data['inverse'])} \\end{{bmatrix}}"
    else:
        inverse_str = "\\text{does not exist}"

    if matrix_data['kernel'] is not None:
        kernel_str = f"\\text{{span}}\\left\\{{\\begin{{bmatrix}} {matrix_to_latex(matrix_data['kernel'])} \\end{{bmatrix}}\\right\\}}"
    else:
        kernel_str = "\\{\\mathbf{0}\\}"

    answer_str += (
        f"d) $A^{{-1}} = {inverse_str}$\n\n"
        f"e) ker($A$) = ${kernel_str}$\n\n"
    )

    return problem_str, answer_str


def format_rref_problem(matrix_data, index):
    def fraction_to_latex(frac):
        if frac.denominator == 1:
            return str(frac.numerator)
        return f"\\frac{{{frac.numerator}}}{{{frac.denominator}}}"

    def matrix_to_latex(matrix):
        rows = []
        for i in range(matrix.shape[0]):
            row_str = ' & '.join(fraction_to_latex(x) for x in matrix[i])
            rows.append(row_str)
        return ' \\\\ '.join(rows)

    def operation_to_latex(step_desc):
        # 将文字描述转换为数学符号
        if "Add" in step_desc:
            parts = step_desc.split()
            factor = Fraction(parts[1])
            r1 = int(parts[4])
            r2 = int(parts[7])
            if factor == 1:
                return f"r_{r2} := r_{r2} + r_{r1}"
            else:
                return f"r_{r2} := r_{r2} + ({factor})r_{r1}"
        elif "Subtract" in step_desc:
            parts = step_desc.split()
            factor = Fraction(parts[1])
            r1 = int(parts[4])
            r2 = int(parts[7])
            if factor == 1:
                return f"r_{r2} := r_{r2} - r_{r1}"
            else:
                return f"r_{r2} := r_{r2} - ({factor})r_{r1}"
        elif "Multiply" in step_desc:
            parts = step_desc.split()
            row = int(parts[2])
            factor = Fraction(parts[4])
            return f"r_{row} := ({factor})r_{row}"
        return step_desc  # 如果无法解析，返回原始描述

    problem_str = (
        f"$A = \\begin{{bmatrix}} {matrix_to_latex(matrix_data['original'])} \\end{{bmatrix}}$\n\n"
    )

    answer_str = (
        "**Solution**\n\n"
        "**Elementary Row Operations:**\n\n"
    )

    for i, (step, matrix) in enumerate(zip(matrix_data['steps'], matrix_data['intermediate_matrices']), 1):
        latex_op = operation_to_latex(step)
        answer_str += (
            f"({i}) ${latex_op}$\n\n"
            f"$\\quad \\begin{{bmatrix}} {matrix_to_latex(matrix)} \\end{{bmatrix}}$\n\n"
        )

    answer_str += (
        "**Result:**\n\n"
        f"$\\begin{{bmatrix}} {matrix_to_latex(matrix_data['rref'])} \\end{{bmatrix}}$\n\n"
    )

    return problem_str, answer_str