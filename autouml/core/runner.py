from autouml.parsers.python_parser import PythonParser
from autouml.uml.generator import PlantUMLGenerator

def run_autouml(project_path: str, output_path: str):
    parser = PythonParser()
    uml_classes = parser.parse(project_path)

    generator = PlantUMLGenerator()
    generator.generate(uml_classes, output_path)
