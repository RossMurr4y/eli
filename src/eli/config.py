"""

Configuration object for an Eli instance.
"""

from pathlib import Path
import yaml

from configurable import Configurable
from profile import Profile

class ConfigInvalidYaml(Exception):
    """Eli configuration is not valid YAML."""

class ConfigMissingMandatory(Exception):
    """Eli configuration is missing mandatory attributes."""

class ConfigFileNotFound(Exception):
    """Eli configuration file is inaccesible or does not exist."""

class Config(Configurable):
    """The base class for an Eli configuration."""

    name = ""
    profiles: [Profile] = []

    def __init__(
        self,
        name: str = "Eli",
        profiles: [Profile] = []
    ):
        self.name = name
        self.profiles = []
        for profile in profiles:
            self.profiles.append(Profile(**profile))

    def get_profiles(self):
        return self.profiles

    def from_file(path: Path):
        try:
            with open(path, "r") as file:
                cfg = yaml.safe_load(file)
                config = Config(name=cfg["name"], profiles=cfg["profiles"])
                return config
        except:
            raise ConfigFileNotFound(f"Config file not found at path: {str(path)}")


