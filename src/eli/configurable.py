"""

A base Eli class for user-input-configurable object classes, such as config files and profiles.
"""

from abc import ABCMeta, abstractmethod


class Configurable(metaclass=ABCMeta):
    """Configurable-based classes are intended to be user configurable."""

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            callable(subclass.__init__)
            and callable(subclass.__repr__)
            or NotImplemented
        )

    @abstractmethod
    def __init__(self, *args, **kwargs):
        NotImplementedError

    def __repr__(self, **kwargs):
        """Ensures the configurable can easily be printed"""
        attributes = ", ".join(
            f"{key}={value!r}" for key, value in vars(self).items()
        )
        return f"{self.__class__.__name__}({attributes})"
