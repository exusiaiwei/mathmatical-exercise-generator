def format_vector_problem_answer(problem, answer, operation, index):
    vector_elements_u = ' \\\\ '.join([str(x) for x in problem[0]])
    vector_elements_v = ' \\\\ '.join([str(x) for x in problem[1]])
    answer_elements = ' \\\\ '.join([str(x) for x in answer])

    problem_str = f"Let $\\mathbf{{u}} = \\begin{{bmatrix}} {vector_elements_u} \\end{{bmatrix}}$ and $\\mathbf{{v}} = \\begin{{bmatrix}} {vector_elements_v} \\end{{bmatrix}}$. Compute $\\mathbf{{u}} {operation} \\mathbf{{v}}$."
    answer_str = f"{index}: $\\begin{{bmatrix}} {answer_elements} \\end{{bmatrix}}$"
    return problem_str, answer_str

def format_matrix_problem_answer(A, B, C, operation, index):
    def matrix_to_latex(matrix):
        rows = []
        for i in range(matrix.shape[0]):
            rows.append(' & '.join(str(x) for x in matrix[i]))
        return ' \\\\ '.join(rows)

    problem_str = f"Let $A = \\begin{{bmatrix}} {matrix_to_latex(A)} \\end{{bmatrix}}$ and $B = \\begin{{bmatrix}} {matrix_to_latex(B)} \\end{{bmatrix}}$. Compute $A {operation} B$."
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