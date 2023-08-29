"""

Configuration options for quandary
"""

from enum import Enum

class InvalidOptionTypeError(Exception):
    pass

class OptionType(Enum):
    DEBUG = 'Debug'

class ProfileOption():
    def __init__(self, name: OptionType, value: any):
        """A profile option is a configuration setting that can be set within a profile."""
        self.name = name
        self.value = value

    def __str__(self) -> str:
        return f"ProfileOption(name={self.name}, value={self.value})"
