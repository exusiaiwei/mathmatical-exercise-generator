# This file will generate math problems for exercises, it can generate problems and answers in latex format, and save them into a markdown file.
# The problems will be generated in a random order, and the answers will be placed at the end of the file.

import random
import os
import sys
import re
import numpy as np

# Define the number of problems to generate
num_problems = 10

# Define the range of numbers to generate
num_range = [-10, 10]

# Define the length of the problems
problem_length = 3

a = np.array([random.randint(num_range[0], num_range[1]) for i in range(problem_length)])
b = np.array([random.randint(num_range[0], num_range[1]) for i in range(problem_length)])
print(a + b)

c = np.matrix([a, b])
print(c)
