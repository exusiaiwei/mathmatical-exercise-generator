def save_problems_by_type(filename, problems_by_type, answers_by_type):
    with open(filename, 'a') as file:
        file.write("---\ntitle: Linear Algebra Exercises\nformat:\n  pdf:\n    documentclass: article\n---\n\n")
        file.write("# Exercise\n\n")
        for problem_type, problems in problems_by_type.items():
            file.write(f"## {problem_type}\n\n")
            for operation, problem_list in problems.items():
                file.write(f"### {operation}\n\n")
                for i, problem in enumerate(problem_list):
                    file.write(f"{i+1}. {problem}\n\n")

        file.write("\n# Answer\n\n")
        for problem_type, answers in answers_by_type.items():
            file.write(f"## {problem_type}\n\n")
            for operation, answer_list in answers.items():
                file.write(f"### {operation}\n\n")
                for i in range(0, len(answer_list), 5):
                    file.write(' '.join(answer_list[i:i+5]) + '\n\n')
