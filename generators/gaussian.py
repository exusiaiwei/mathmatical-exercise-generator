import numpy as np
from fractions import Fraction
from utils.config import Config

class GaussianElimination:
    @staticmethod
    def generate_problem(problem_length):
        # Generate coefficient matrix (ensure it has a solution)
        A = np.random.randint(Config.GAUSSIAN_RANGE[0], Config.GAUSSIAN_RANGE[1],
                            (problem_length, problem_length))
        x = np.random.randint(Config.GAUSSIAN_RANGE[0], Config.GAUSSIAN_RANGE[1],
                            (problem_length, 1))
        b = np.dot(A, x)

        # Construct augmented matrix
        augmented = np.hstack((A, b))

        # Compute RREF and solution set
        rref_matrix = GaussianElimination.compute_rref(augmented.copy())

        return augmented, rref_matrix, x

    @staticmethod
    def compute_rref(matrix):
        """Compute the Reduced Row Echelon Form (RREF)"""
        matrix = matrix.astype(float)
        rows, cols = matrix.shape
        lead = 0

        for r in range(rows):
            if lead >= cols:
                break

            i = r
            while matrix[i][lead] == 0:
                i += 1
                if i == rows:
                    i = r
                    lead += 1
                    if lead == cols:
                        return matrix

            # Swap rows
            if i != r:
                matrix[r], matrix[i] = matrix[i].copy(), matrix[r].copy()

            # Normalize the pivot
            div = matrix[r][lead]
            if div != 0:
                matrix[r] = matrix[r] / div

            # Eliminate
            for i in range(rows):
                if i != r:
                    matrix[i] = matrix[i] - matrix[i][lead] * matrix[r]

            lead += 1

        return matrix
