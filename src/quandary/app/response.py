"""

A response is a base class (interface) for any construct that is returned from an LLM.
"""

from abc import ABCMeta, abstractmethod


class ResponseInterface(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass) -> bool:
        return (
            hasattr(subclass, "value")
            and callable(subclass.value)
            or NotImplemented
        )

    def __str__(self) -> str:
        """allow serialisation to string"""
        return f"{self.__class__.__name__}: {self.value}"

    @property
    @abstractmethod
    def value(self):
        """A response value / content."""
        raise NotImplementedError
