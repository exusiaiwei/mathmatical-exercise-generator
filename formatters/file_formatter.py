# formatters/file_formatter.py
from fractions import Fraction

def save_problems_by_type(problems_by_type, answers_by_type):
    # 集中管理各个部分的描述
    section_descriptions = {
        "Vector Arithmetic": {
            "Addition": "Find the sum of the following vectors $\\mathbf{u}$ and $\\mathbf{v}$",
            "Subtraction": "Find the difference of the following vectors $\\mathbf{u}$ and $\\mathbf{v}$",
            "Scalar Multiplication": "Find the scalar product of the following vector $\\mathbf{u}$ and scalar $k$"
        },
        "Matrix Arithmetic": {
            "Addition": "Find the sum of the following matrices $A$ and $B$",
            "Subtraction": "Find the difference of the following matrices $A$ and $B$",
            "Multiplication": "Find the product of the following matrices $A$ and $B$"
        },
        "Matrix Properties": {
            "Properties": "For each matrix $A$, find:\n\n" +
                        "a) rank($A$)\n\n" +
                        "b) nullity($A$)\n\n" +
                        "c) det($A$)\n\n" +
                        "d) $A^{-1}$ (if exists)\n\n" +
                        "e) basis of ker($A$)",
            "RREF": "Find the Reduced Row Echelon Form of the following matrix $A$"
        },
        "Calculus": {
            "Limit": "Calculate the following limits",
            "Derivative": "Calculate the derivatives of the following expressions",
            "Integral": "Calculate the indefinite and definite integrals of the following expressions",
            "Partial Derivative": "Calculate the partial derivatives of the following expressions"
        }
    }

    content = ["# Problems\n"]

    # 生成问题部分
    for section, problems in problems_by_type.items():
        content.append(f"## {section}\n")

        if section in section_descriptions:
            for op, desc in section_descriptions[section].items():
                if desc and op in problems:
                    content.append(f"### {op}\n{desc}\n")
                    for i, problem in enumerate(problems[op], 1):
                        # 简化问题描述，只保留数学定义
                        if isinstance(problem, str):
                            simplified = (problem.replace("Let ", "")
                                              .replace(". Compute", "")
                                              .replace("Find", "")
                                              .strip())
                            content.append(f"{i}. {simplified}\n")
                        elif isinstance(problem, dict) and "problem" in problem:
                            content.append(f"{i}. {problem['problem']}\n")

    # 生成解答部分
    content.append("\n# Solutions\n")

    for section, answers in answers_by_type.items():
        content.append(f"## {section}\n")
        for operation, answer_list in answers.items():
            content.append(f"### {operation}\n")
            # 每5个答案一行
            if isinstance(answer_list, list):
                for i in range(0, len(answer_list), 5):
                    content.append(' '.join(answer_list[i:i+5]))
                    content.append("")  # 添加空行
            elif isinstance(answer_list, dict):
                content.append(f"{answer_list['answer']}\n")

    # 写入文件
    return '\n'.join(content)

def format_vector_problem_answer(problem, answer, operation, index):
    vector_elements_u = ' \\\\ '.join([str(x) for x in problem[0]])
    vector_elements_v = ' \\\\ '.join([str(x) for x in problem[1]])
    answer_elements = ' \\\\ '.join([str(x) for x in answer])

    # 只显示向量定义
    problem_str = (
        f"$\\mathbf{{u}} = \\begin{{bmatrix}} {vector_elements_u} \\end{{bmatrix}}$, "
        f"$\\mathbf{{v}} = \\begin{{bmatrix}} {vector_elements_v} \\end{{bmatrix}}$\n"
    )
    answer_str = f"$\\begin{{bmatrix}} {answer_elements} \\end{{bmatrix}}$"
    return problem_str, answer_str

def format_matrix_problem_answer(A, B, C, operation, index):
    def matrix_to_latex(matrix):
        rows = []
        for row in matrix:
            rows.append(' & '.join(str(x) for x in row))
        return ' \\\\ '.join(rows)

    # 只显示矩阵定义
    problem_str = (
        f"$A = \\begin{{bmatrix}} {matrix_to_latex(A)} \\end{{bmatrix}}$, "
        f"$B = \\begin{{bmatrix}} {matrix_to_latex(B)} \\end{{bmatrix}}$\n"
    )
    answer_str = f"$\\begin{{bmatrix}} {matrix_to_latex(C)} \\end{{bmatrix}}$"
    return problem_str, answer_str

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

    # 只显示矩阵定义
    problem_str = f"$A = \\begin{{bmatrix}} {matrix_to_latex(matrix_data['original'])} \\end{{bmatrix}}$\n"

    # 添加解答步骤
    answer_str = (
        "**Solution**\n\n"
        "**Row Operations:**\n\n"
    )

    # 添加消元步骤
    for step in matrix_data['augmented_steps'][1:]:
        answer_str += f"$\\begin{{bmatrix}} {matrix_to_latex(step['matrix'], True)} \\end{{bmatrix}}$\n\n"

    # 添加结果
    answer_str += "**Results:**\n\n"

    # 处理逆矩阵和kernel的显示
    if matrix_data['inverse'] is not None:
        inverse_str = f"\\begin{{bmatrix}} {matrix_to_latex(matrix_data['inverse'])} \\end{{bmatrix}}"
    else:
        inverse_str = "\\text{does not exist}"

    if matrix_data['kernel'] is not None:
        kernel_str = f"\\text{{span}}\\left\\{{\\begin{{bmatrix}} {matrix_to_latex(matrix_data['kernel'])} \\end{{bmatrix}}\\right\\}}"
    else:
        kernel_str = "\\{\\mathbf{0}\\}"

    answer_str += (
        f"a) rank($A$) = {matrix_data['rank']}\n\n"
        f"b) nullity($A$) = {matrix_data['nullity']}\n\n"
        f"c) det($A$) = {Fraction(matrix_data['determinant']).limit_denominator()}\n\n"
        f"d) $A^{{-1}} = {inverse_str}$\n\n"
        f"e) ker($A$) = ${kernel_str}$\n\n"
    )

    return problem_str, answer_str

def format_rref_problem(matrix_data, index):
    def matrix_to_latex(matrix):
        rows = []
        for i in range(matrix.shape[0]):
            row_str = ' & '.join(f"{Fraction(x).limit_denominator()}" for x in matrix[i])
            rows.append(row_str)
        return ' \\\\ '.join(rows)

    # 只显示矩阵定义
    problem_str = f"$A = \\begin{{bmatrix}} {matrix_to_latex(matrix_data['original'])} \\end{{bmatrix}}$\n"

    # 添加解答
    answer_str = (
        "**Solution**\n\n"
        "**Row Operations:**\n\n"
    )

    # 添加步骤
    for i, (step, matrix) in enumerate(zip(matrix_data['steps'], matrix_data['intermediate_matrices']), 1):
        latex_op = step.replace("Add", "r_i := r_i +").replace("Subtract", "r_i := r_i -")
        answer_str += (
            f"({i}) ${latex_op}$\n\n"
            f"$\\begin{{bmatrix}} {matrix_to_latex(matrix)} \\end{{bmatrix}}$\n\n"
        )

    answer_str += (
        "**Result:**\n\n"
        f"$\\begin{{bmatrix}} {matrix_to_latex(matrix_data['rref'])} \\end{{bmatrix}}$\n\n"
    )

    return problem_str, answer_str
