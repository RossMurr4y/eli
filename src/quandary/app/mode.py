"""

A mode is a base class (interface) for any construct that interacts with an LLM.
"""

from abc import ABCMeta, abstractmethod
from .response import ResponseInterface

class ModeInterface(metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, 'run') and
            callable(subclass.run) and
            hasattr(subclass, 'question') and
            callable(subclass.question) or
            NotImplemented)
    
    @property
    @abstractmethod
    def question(self):
        raise NotImplementedError
    
    @property
    @abstractmethod
    def response(self):
        raise NotImplementedError
    
    @abstractmethod
    def __init__(self):
        """Initialise the mode configuration and settings"""
        raise NotImplementedError

    def __str__(self) -> str:
        """allow serialisation to string"""
        return f"{self.__class__.__name__}: {self.__dict__}"

    @abstractmethod
    def run(self) -> ResponseInterface:
        """run the mode."""
        raise NotImplementedError