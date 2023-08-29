"""

A profile is a predefined combination of user settings that configures quandary and quandary extensions.
"""
from os import environ
from pathlib import Path
import yaml

from ..options import ProfileOption, OptionType, InvalidOptionTypeError

class Profile():

    name = ""
    options = []

    def __init__(self, name: str, options: list = ()):
        self.name = name
        self.options = options

    def __str__(self) -> str:
        str_options = []
        for o in self.options:
            str_options.append(str(o))
        return f"Profile(name={self.name}, options={str(str_options)})"

    def process_profile_options(self):
        """loop over a profile options, raising events/messages as necessary"""
        for option in self.options:
            try:
                match option.name:
                    case OptionType.DEBUG:
                        # set profiles debug mode
                        environ['QNDY_DEBUG'] = option.value in ["True", "1", "true"]
                        pass
                    case _:
                        # do nothing
                        raise InvalidOptionTypeError("A profile contains an invalid option type.")
            except InvalidOptionTypeError as e:
                print("InvalidOptionTypeError: ", e)

class Profiles():

    DEFAULT_PROFILE_NAME = "default"
    DEFAULT_PROFILE_SELECTION = (DEFAULT_PROFILE_NAME, 0)

    registered_profiles = [
        # default Profile list that is always present.
        Profile(DEFAULT_PROFILE_NAME, [])
    ]
    # profile selection is a list of tuples of the profile name, and its display sequence
    # as an integer.
    profile_selection = []

    def __init__(self, *data):
        home_dir = Path.home()
        quandary_config_path = Path.joinpath(home_dir, ".quandary.yml")
        # for every profile in registered_profiles, loop over them and add to profile_options
        # which is used to populate the profile selector dropdown
        self.data = list(data)
        self.load_from_file(quandary_config_path)
        self.calculate_selection()

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)

    def add(self, profile: Profile):
        """add a new profile to the profiles available for selection"""
        i = len(self.registered_profiles) - 1
        self.registered_profiles.append(profile)
        self.calculate_selection()

    def calculate_selection(self):
        """(re)calculates the selection of profiles (used for populating the profile selector)"""
        i = 0
        self.profile_selection = []
        for p in self.registered_profiles:
            self.profile_selection.append((p.name, i))
            i += 1

    def load_from_file(self, path: str):
        """loads profile configuration from a quandary configuration file"""
        with open(path, "r") as file:
            config = yaml.safe_load(file)
            profiles = config['profiles']
            for profile in profiles:
                profile_options = []
                for option in profile['options']:
                    profile_options.append(ProfileOption(name = option['name'], value = option['value']))
                self.add(
                    Profile(
                        name = profile['name'],
                        options = profile_options,
                    )
                )
        # recalculate the selection list when done
        self.calculate_selection()