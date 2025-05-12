from typing import List

class UMLClass:
    def __init__(self, name: str, attributes: List['UMLAttribute'] = None,
                 methods: List['UMLMethod'] = None, parents: List[str] = None):
        self.name = name
        self.attributes = attributes or []
        self.methods = methods or []
        self.parents = parents or []

class UMLMethod:
    def __init__(self, name: str):
        self.name = name

class UMLAttribute:
    def __init__(self, name: str):
        self.name = name
