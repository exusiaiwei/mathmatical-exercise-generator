# generators/calculus_exercises.py

from typing import Dict, List
import sympy
import random
from sympy import log, exp


class CalculusExercises:
    """Class for generating calculus exercises"""

    @staticmethod
    def generate_limit_exercise() -> Dict:
        """生成极限计算练习"""
        x = sympy.Symbol("x")
        # 生成不同类型的极限问题
        types = ["polynomial", "rational", "logarithmic", "exponential"]
        exercise_type = random.choice(types)

        if exercise_type == "polynomial":
            degree = random.randint(1, 3)
            coeffs = [random.randint(-5, 5) for _ in range(degree + 1)]
            expr = sum(c * x**i for i, c in enumerate(coeffs))
            point = random.randint(-3, 3)

        elif exercise_type == "rational":
            num = x**2 - 1
            den = x - 1
            expr = num / den
            point = 1

        elif exercise_type == "logarithmic":
            expr = log(1 + x) / x
            point = 0

        else:  # exponential
            expr = (1 + 1 / x) ** x
            point = sympy.oo

        try:
            limit = sympy.limit(expr, x, point)
            problem_str = (
                f"Calculate the limit of the following expression: "
                f"$$\\lim_{{x \\to {point}}} {sympy.latex(expr)}$$"
            )
            answer_str = f"The limit is: $${sympy.latex(limit)}$$"
            return {
                "type": exercise_type,
                "problem": problem_str,
                "answer": answer_str,
            }
        except sympy.SympifyError:
            return CalculusExercises.generate_limit_exercise()

    @staticmethod
    def generate_derivative_exercise() -> Dict[str, str]:
        """Generate derivative calculation exercises"""
        x: sympy.Symbol = sympy.Symbol("x")
        types: List[str] = [
            "basic",
            "chain",
            "product",
            "quotient",
            "logarithmic",
            "exponential"
        ]
        exercise_type: str = random.choice(types)
        expr: sympy.Expr

        if exercise_type == "basic":
            funcs: List[sympy.Expr] = [
                x**n for n in range(2, 5)
            ] + [
                exp(x),
                log(x)
            ]
            expr = random.choice(funcs)

        elif exercise_type == "chain":
            inner: sympy.Expr = x**2 + sympy.Integer(random.randint(-3, 3))
            outer = random.choice([log, exp])
            expr = outer(inner)

        elif exercise_type == "product":
            f: sympy.Expr = x ** sympy.Integer(random.randint(1, 3))
            g: sympy.Expr = exp(x) if random.random() < 0.5 else log(x)
            expr = f * g

        elif exercise_type == "quotient":
            num: sympy.Expr = x ** sympy.Integer(random.randint(1, 3))
            den: sympy.Expr = x**2 + sympy.Integer(1)
            expr = num / den

        elif exercise_type == "logarithmic":
            expr = log(x**2 + 1) + log(x + 1)

        else:  # exponential
            expr = exp(x**2) + exp(2*x)

        derivative: sympy.Expr = sympy.diff(expr, x)
        problem_str = (
            "Calculate the derivative of the following expression: "
            f"$${sympy.latex(expr)}$$"
        )
        answer_str = f"The derivative is: $${sympy.latex(derivative)}$$"
        return {
            "type": exercise_type,
            "problem": problem_str,
            "answer": answer_str,
        }

        derivative: sympy.Expr = sympy.diff(expr, x)
        problem_str = (
            "Calculate the derivative of the following expression: "
            f"$${sympy.latex(expr)}$$"
        )
        answer_str = f"The derivative is: $${sympy.latex(derivative)}$$"
        return {
            "type": exercise_type,
            "problem": problem_str,
            "answer": answer_str,
        }

    @staticmethod
    def generate_integral_exercise() -> Dict:
        """Generate advanced integral exercises"""
        x = sympy.Symbol("x")
        types = [
            "basic", "substitution", "parts",
            "trig_sub", "partial_fractions",
            "improper", "special_functions"
        ]
        exercise_type = random.choice(types)

        if exercise_type == "basic":
            # Polynomial integration
            degree = random.randint(2, 4)
            coeffs = [random.randint(-5, 5) for _ in range(degree + 1)]
            expr = sum(c * x**i for i, c in enumerate(coeffs))

        elif exercise_type == "substitution":
            # More complex substitution problems
            options = [
                x * sympy.sqrt(x**2 + 1),
                1/(x * sympy.log(x)),
                sympy.exp(sympy.sin(x)) * sympy.cos(x)
            ]
            expr = random.choice(options)

        elif exercise_type == "parts":
            # Integration by parts with multiple steps
            options = [
                x**2 * sympy.exp(x),
                x**3 * sympy.log(x),
                sympy.exp(x) * sympy.sin(x)
            ]
            expr = random.choice(options)

        elif exercise_type == "trig_sub":
            # Trigonometric substitutions
            options = [
                1/sympy.sqrt(1 - x**2),
                1/(x**2 + 1),
                sympy.sqrt(4 - x**2)
            ]
            expr = random.choice(options)

        elif exercise_type == "partial_fractions":
            # Partial fractions decomposition
            options = [
                1/((x + 1)*(x - 2)),
                (3*x + 2)/(x**2 - 4),
                x/(x**2 - 5*x + 6)
            ]
            expr = random.choice(options)

        elif exercise_type == "improper":
            # Improper integrals
            options = [
                1/x**2,
                sympy.exp(-x),
                1/sympy.sqrt(x)
            ]
            expr = random.choice(options)
            a, b = 1, sympy.oo  # Set upper limit to infinity

        elif exercise_type == "special_functions":
            # Integration involving special functions
            options = [
                sympy.exp(-x**2),
                sympy.sin(x)/x,
                sympy.exp(x)/x
            ]
            expr = random.choice(options)

        # Calculate integral
        try:
            integral = sympy.integrate(expr, x)
            if exercise_type == "improper":
                definite = sympy.integrate(expr, (x, a, b))
                problem_str = (
                    f"Evaluate the improper integral:\n"
                    f"$$\\int_{{{a}}}^{{{b}}} {sympy.latex(expr)} dx$$"
                )
                answer_str = (
                    f"The improper integral converges to: $${sympy.latex(definite)}$$"
                )
            else:
                # For regular integrals
                a, b = sorted([random.randint(1, 5) for _ in range(2)])
                definite = sympy.integrate(expr, (x, a, b))
                problem_str = (
                    f"Find the indefinite integral and evaluate from {a} to {b}:\n"
                    f"$$\\int {sympy.latex(expr)} dx$$"
                )
                answer_str = (
                    f"The indefinite integral is: $${sympy.latex(integral)}$$\n"
                    f"Definite integral from {a} to {b}: $${sympy.latex(definite)}$$"
                )

            return {
                "type": exercise_type,
                "problem": problem_str,
                "answer": answer_str,
                "interval": (str(a), str(b)) if exercise_type != "improper" else (str(a), "∞")
            }
        except sympy.SympifyError:
            return CalculusExercises.generate_integral_exercise()

    @staticmethod
    def generate_partial_derivative_exercise() -> Dict:
        """Generate advanced partial derivative exercises"""
        x, y, z = sympy.symbols("x y z")
        types = [
            "basic", "exponential", "logarithmic",
            "higher_order", "mixed", "implicit", "chain_rule"
        ]
        exercise_type = random.choice(types)

        if exercise_type == "basic":
            expr = x**3*y**2 + 2*x*y**3 - 3*x**2*y
        elif exercise_type == "exponential":
            expr = exp(x**2 + y**2) * (x + y)
        elif exercise_type == "logarithmic":
            expr = log(x**3 + y**3) - log(x*y)
        elif exercise_type == "higher_order":
            expr = x**4*y**3 + 3*x**2*y**4
            order = random.choice(["second", "third"])
            if order == "second":
                partial = sympy.diff(expr, x, 2)
                problem_str = (
                    f"Find the second order partial derivative of:\n"
                    f"$$f(x,y) = {sympy.latex(expr)}$$\n"
                    "Find $\\frac{\\partial^2 f}{\\partial x^2}$"
                )
                answer_str = f"$$\\frac{{\\partial^2 f}}{{\\partial x^2}} = {sympy.latex(partial)}$$"
            else:
                partial = sympy.diff(expr, y, 3)
                problem_str = (
                    f"Find the third order partial derivative of:\n"
                    f"$$f(x,y) = {sympy.latex(expr)}$$\n"
                    "Find $\\frac{\\partial^3 f}{\\partial y^3}$"
                )
                answer_str = f"$$\\frac{{\\partial^3 f}}{{\\partial y^3}} = {sympy.latex(partial)}$$"
            return {
                "type": f"{order}_order",
                "problem": problem_str,
                "answer": answer_str,
            }
        elif exercise_type == "mixed":
            expr = x**3*y**2 + x*y**4
            partial = sympy.diff(expr, x, y)
            problem_str = (
                f"Find the mixed partial derivative of:\n"
                f"$$f(x,y) = {sympy.latex(expr)}$$\n"
                "Find $\\frac{\\partial^2 f}{\\partial x \\partial y}$"
            )
            answer_str = f"$$\\frac{{\\partial^2 f}}{{\\partial x \\partial y}} = {sympy.latex(partial)}$$"
            return {
                "type": "mixed",
                "problem": problem_str,
                "answer": answer_str,
            }
        elif exercise_type == "implicit":
            # Implicit differentiation example
            expr = x**2*y + y**2*x - x*y
            problem_str = (
                f"Given the implicit function:\n"
                f"$${sympy.latex(expr)} = 0$$\n"
                "Find $\\frac{\\partial y}{\\partial x}$"
            )
            dy_dx = -sympy.diff(expr, x)/sympy.diff(expr, y)
            answer_str = f"$$\\frac{{\\partial y}}{{\\partial x}} = {sympy.latex(dy_dx)}$$"
            return {
                "type": "implicit",
                "problem": problem_str,
                "answer": answer_str,
            }
        else:  # chain_rule
            # Multivariable chain rule example
            u = sympy.Function('u')(x, y)
            v = sympy.Function('v')(x, y)
            f = sympy.Function('f')(u, v)
            expr = f.diff(x)
            problem_str = (
                f"Given $u = u(x,y)$ and $v = v(x,y)$, use the chain rule to find:\n"
                f"$$\\frac{{\\partial f}}{{\\partial x}}$$\n"
                "where $f = f(u,v)$"
            )
            answer_str = (
                f"$$\\frac{{\\partial f}}{{\\partial x}} = "
                f"\\frac{{\\partial f}}{{\\partial u}}\\frac{{\\partial u}}{{\\partial x}} + "
                f"\\frac{{\\partial f}}{{\\partial v}}\\frac{{\\partial v}}{{\\partial x}}$$"
            )
            return {
                "type": "chain_rule",
                "problem": problem_str,
                "answer": answer_str,
            }

        # For basic types
        partial_x = sympy.diff(expr, x)
        partial_y = sympy.diff(expr, y)

        problem_str = (
            f"Find the partial derivatives of the function:\n"
            f"$$f(x,y) = {sympy.latex(expr)}$$\n"
            "Find $\\frac{\\partial f}{\\partial x}$ and "
            "$\\frac{\\partial f}{\\partial y}$"
        )
        answer_str = (
            f"$$\\frac{{\\partial f}}{{\\partial x}} = {sympy.latex(partial_x)}$$\n"
            f"$$\\frac{{\\partial f}}{{\\partial y}} = {sympy.latex(partial_y)}$$"
        )
        return {
            "type": exercise_type,
            "problem": problem_str,
            "answer": answer_str,
        }

    @staticmethod
    def generate_jacobian_exercise() -> Dict:
        """Generate Jacobian matrix exercises"""
        x, y = sympy.symbols("x y")
        types = ["basic", "logarithmic", "exponential", "polynomial"]
        exercise_type = random.choice(types)

        if exercise_type == "basic":
            f1 = x**2 + y**2
            f2 = x*y
        elif exercise_type == "logarithmic":
            f1 = sympy.log(x**2 + y**2)
            f2 = sympy.log(x + y)
        elif exercise_type == "exponential":
            f1 = sympy.exp(x + y)
            f2 = sympy.exp(x - y)
        else:  # polynomial
            f1 = x**3 + 2*x*y**2
            f2 = 3*x**2*y + y**3

        expr = sympy.Matrix([f1, f2])
        jac = expr.jacobian([x, y])

        problem_str = (
            f"Compute the Jacobian matrix for the following system:\n"
            f"$$\\mathbf{{F}}(x,y) = {sympy.latex(expr)}$$"
        )
        answer_str = (
            f"The Jacobian matrix is:\n"
            f"$${sympy.latex(jac)}$$"
        )
        return {
            "type": exercise_type,
            "problem": problem_str,
            "answer": answer_str,
        }

    @staticmethod
    def generate_linear_algebra_exercise() -> Dict:
        """生成线性代数理论问题"""
        types = ["rank", "kernel", "independence"]
        exercise_type = random.choice(types)

        if exercise_type == "rank":
            # 矩阵秩的问题
            rows = random.randint(2, 4)
            cols = random.randint(2, 4)
            matrix = sympy.randMatrix(rows, cols, min=0, max=5)
            problem_str = (
                f"Find the rank of the following matrix: "
                f"$${sympy.latex(matrix)}$$"
            )
            rank = matrix.rank()
            answer_str = f"The rank is: $${rank}$$"

        elif exercise_type == "kernel":
            # 核空间问题
            rows = random.randint(2, 3)
            cols = random.randint(2, 3)
            matrix = sympy.randMatrix(rows, cols, min=0, max=5)
            problem_str = (
                f"Find the kernel of the following matrix: "
                f"$${sympy.latex(matrix)}$$"
            )
            kernel = matrix.nullspace()
            answer_str = f"The kernel is: $${sympy.latex(kernel)}$$"

        else:  # independence
            # 线性独立性问题
            num_vectors = random.randint(2, 4)
            vectors = [sympy.randMatrix(3, 1, min=0, max=5) for _ in range(num_vectors)]
            problem_str = (
                "Determine if the following vectors are linearly independent: "
                f"$${', '.join(sympy.latex(v) for v in vectors)}$$"
            )
            matrix = sympy.Matrix.hstack(*vectors)
            is_independent = matrix.rank() == num_vectors
            answer_str = f"The vectors are {'linearly independent' if is_independent else 'linearly dependent'}"

        return {
            "type": exercise_type,
            "problem": problem_str,
            "answer": answer_str,
        }
