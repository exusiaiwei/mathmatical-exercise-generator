import os
from datetime import datetime
from string import Template
from formatters.file_formatter import save_problems_by_type


class ExerciseFileHandler:
    def __init__(self, template_dir="templates", output_dir="output"):
        self.template_dir = template_dir
        self.output_dir = output_dir
        self.exercise_count = self._get_exercise_count()

    def _get_exercise_count(self):
        """Get next exercise number by finding the max current number"""
        if not os.path.exists(self.output_dir):
            return 1

        exercises = [
            f for f in os.listdir(self.output_dir)
            if f.startswith("exercise_")
        ]
        if not exercises:
            return 1

        # Extract numbers from filenames and find max
        numbers = []
        for exercise in exercises:
            try:
                # 从 'exercise_001.qmd' 提取数字部分
                num = int(exercise.split('_')[1].split('.')[0])
                numbers.append(num)
            except (IndexError, ValueError):
                continue

        return max(numbers) + 1 if numbers else 1

    def _get_template_path(self, exercise_type):
        """根据练习类型返回对应的模板路径"""
        if "Calculus" in exercise_type:
            return os.path.join(
                self.template_dir,
                "calculus_exercise_template.qmd"
            )
        return os.path.join(
            self.template_dir,
            "exercise_template.qmd"
        )

    def prepare_exercise_file(self, problems_by_type, answers_by_type, num_problems):
        os.makedirs(self.output_dir, exist_ok=True)

        # 根据第一个练习类型确定使用哪个模板
        exercise_type = next(iter(problems_by_type.keys()))
        template_qmd = self._get_template_path(exercise_type)

        output_name = f"exercise_{self.exercise_count:03d}"
        output_qmd = os.path.join(
            self.output_dir,
            f"{output_name}.qmd"
        )

        # 使用 file_formatter 中的函数生成内容
        formatted_content = save_problems_by_type(
            problems_by_type, answers_by_type)

        with open(template_qmd, 'r', encoding='utf-8') as f:
            template = Template(f.read())

        # 对于微积分模板需要额外的变量
        if "Calculus" in exercise_type:
            # 确保formatted_content是字典类型
            if isinstance(formatted_content, dict):
                limit = formatted_content.get("Limit", "")
                derivative = formatted_content.get("Derivative", "")
                integral = formatted_content.get("Integral", "")
                partial = formatted_content.get("Partial Derivative", "")

                final_content = template.substitute(
                    exercise_number=self.exercise_count,
                    date=datetime.now().strftime("%Y-%m-%d"),
                    num_problems=num_problems,
                    limit_problems=limit,
                    derivative_problems=derivative,
                    integral_problems=integral,
                    partial_derivative_problems=partial
                )
            else:
                final_content = template.substitute(
                    exercise_number=self.exercise_count,
                    date=datetime.now().strftime("%Y-%m-%d"),
                    num_problems=num_problems,
                    content=formatted_content
                )
        else:
            final_content = template.substitute(
                exercise_number=self.exercise_count,
                date=datetime.now().strftime("%Y-%m-%d"),
                num_problems=num_problems,
                content=formatted_content
            )

        with open(output_qmd, 'w', encoding='utf-8') as f:
            f.write(final_content)

        return output_name
