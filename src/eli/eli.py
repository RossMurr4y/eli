"""

The base class for the Eli application.
"""

from pathlib import Path
from profile import _Profiles

class Eli():

    def __init__(
        self,
        profile_path: str = Path.home().joinpath(Path.home(), ".eli.yml")
    ):
        """create an instance of Eli
        
        Args:
            profile_path: Path to a Eli profile. Defaults to ~/.eli.yml
        
        """

        profiles_from_file = {}
        self.profiles = _Profiles(profiles_from_file)

    def run(self):
        # todo: actually do sometihng
        print(self.profiles.get_profile('Eli'))