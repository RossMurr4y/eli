"""

The base class for the Eli application.
"""

from pathlib import Path

from profile import _Profiles
from config import Config
from configurable import Configurable

class Eli(Configurable):

    def __init__(
        self,
        profile_path: Path = Path.home().joinpath(Path.home(), ".eli.yml")
    ):
        """create an instance of Eli
        
        Args:
            profile_path: Path to a Eli profile. Defaults to ~/.eli.yml
        """

        config = Config.from_file(path=profile_path)
        self.profiles = _Profiles(config.profiles)

    def run(self):
        # todo: actually do sometihng
        pass