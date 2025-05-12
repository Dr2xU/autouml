from abc import ABC, abstractmethod
from typing import List
from autouml.uml.models import UMLClass

class ParserInterface(ABC):
    @abstractmethod
    def parse(self, path: str) -> List[UMLClass]:
        """
        Parse the given path and return a list of UMLClass instances
        representing the structure of the codebase.
        """
        pass
