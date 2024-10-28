# utils/config.py

class Config:
    # Problem generation configuration
    NUM_PROBLEMS = 10
    NUM_RANGE = [-10, 10]
    PROBLEM_LENGTH = 3

    # Gaussian elimination specific range (keep small to ensure reasonable problems)
    GAUSSIAN_RANGE = [-5, 5]

    # Output file configuration
    OUTPUT_FILE = 'exercise.qmd'

    # LaTeX related configuration
    #MATRIX_ENV = 'bmatrix'  # Options: bmatrix, pmatrix, vmatrix, etc.