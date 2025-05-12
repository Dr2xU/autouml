import subprocess
import tempfile
import requests
import os
from typing import List
from autouml.uml.models import UMLClass

class PlantUMLGenerator:
    def generate(self, uml_classes: List[UMLClass], output_file: str):
        uml = ['@startuml']

        for cls in uml_classes:
            parent_part = ' extends ' + ', '.join(cls.parents) if cls.parents else ''
            uml.append(f'class {cls.name}{parent_part} {{')
            for attr in cls.attributes:
                uml.append(f'  - {attr.name}')
            for method in cls.methods:
                uml.append(f'  + {method.name}()')
            uml.append('}')

        uml.append('@enduml')

        self._render_plantuml('\n'.join(uml), output_file)

    def _render_plantuml(self, uml_code: str, output_file: str):
        plantuml_jar = os.getenv('PLANTUML_JAR')

        if plantuml_jar and os.path.isfile(plantuml_jar):
            with tempfile.NamedTemporaryFile('w+', suffix='.txt', delete=False) as uml_file:
                uml_file.write(uml_code)
                uml_file_path = uml_file.name

            subprocess.run(['java', '-jar', plantuml_jar, '-tpng', uml_file_path])
            os.rename(uml_file_path.replace('.txt', '.png'), output_file)
        else:
            print("🌐 Using online PlantUML server")
            url = 'http://www.plantuml.com/plantuml/png'
            response = requests.post(url, data=uml_code.encode('utf-8'), headers={'Content-Type': 'text/plain'})
            with open(output_file, 'wb') as f:
                f.write(response.content)
