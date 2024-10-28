import os
import shutil
from datetime import datetime
from string import Template

class ExerciseFileHandler:
    def __init__(self, template_dir="templates", output_dir="output"):
        self.template_dir = template_dir
        self.output_dir = output_dir
        self.exercise_count = self._get_exercise_count()

    def _get_exercise_count(self):
        """Get current exercise count from outputs"""
        if not os.path.exists(self.output_dir):
            return 1
        exercises = [f for f in os.listdir(self.output_dir) if f.startswith("exercise_")]
        return len(exercises) + 1

    def prepare_exercise_file(self, problems_content, num_problems):
        """Prepare exercise file from template"""
        # Create output directory if not exists
        os.makedirs(self.output_dir, exist_ok=True)

        # Copy template files
        template_qmd = os.path.join(self.template_dir, "exercise_template.qmd")
        template_bib = os.path.join(self.template_dir, "refs.bib")

        output_name = f"exercise_{self.exercise_count:03d}"
        output_qmd = os.path.join(self.output_dir, f"{output_name}.qmd")
        output_bib = os.path.join(self.output_dir, "refs.bib")

        shutil.copy2(template_bib, output_bib)

        # Read and fill template
        with open(template_qmd, 'r') as f:
            template = Template(f.read())

        content = template.substitute(
            exercise_number=self.exercise_count,
            date=datetime.now().strftime("%Y-%m-%d"),
            num_problems=num_problems,
            content=problems_content
        )

        # Write output file
        with open(output_qmd, 'w') as f:
            f.write(content)

        return output_name
