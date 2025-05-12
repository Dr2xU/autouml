import ast
import os
from autouml.parsers.parser_interface import ParserInterface
from autouml.uml.models import UMLClass, UMLMethod, UMLAttribute
from typing import List

class PythonParser(ParserInterface):
    def parse(self, path: str) -> List[UMLClass]:
        uml_classes = []

        for dirpath, _, filenames in os.walk(path):
            for file in filenames:
                if file.endswith('.py'):
                    full_path = os.path.join(dirpath, file)
                    with open(full_path, 'r', encoding='utf-8') as f:
                        try:
                            node = ast.parse(f.read(), filename=full_path)
                            uml_classes.extend(self._extract_classes(node))
                        except SyntaxError as e:
                            print(f"⚠️  Skipping file with syntax error: {full_path} ({e})")

        return uml_classes

    def _extract_classes(self, node: ast.AST) -> List[UMLClass]:
        classes = []

        for n in ast.walk(node):
            if isinstance(n, ast.ClassDef):
                methods = []
                attrs = []
                bases = [b.id for b in n.bases if isinstance(b, ast.Name)]
                
                for body_item in n.body:
                    if isinstance(body_item, ast.FunctionDef):
                        methods.append(UMLMethod(body_item.name))
                    elif isinstance(body_item, ast.Assign):
                        for t in body_item.targets:
                            if isinstance(t, ast.Name):
                                attrs.append(UMLAttribute(t.id))

                classes.append(UMLClass(name=n.name, attributes=attrs, methods=methods, parents=bases))

        return classes
