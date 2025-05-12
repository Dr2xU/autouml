from autouml.cli.arguments import parse_arguments
from autouml.core.runner import run_autouml

def main():
    project_path, output_path = parse_arguments()

    print(f"📂 Parsing directory: {project_path}")
    print(f"🖼️  Output diagram: {output_path}")

    run_autouml(project_path, output_path)
