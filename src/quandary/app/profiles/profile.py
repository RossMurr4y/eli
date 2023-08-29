"""

A profile is a predefined combination of user settings that configures quandary and quandary extensions.
"""
from os import environ
from pathlib import Path
import yaml


class ProfileOption():
    """A profile option is a configuration setting that can be set within a profile."""

    name: str
    value: any

    def __init__(self, name: str, value: any):
        self.name = name
        self.value = value

class Profile():

    name = ""
    options = [
            # the default options inherrited by every profile
            ProfileOption(
                name='DebugEnabled',
                value=environ.get("QNDY_DEBUG", "False") in ["True", "1", "true"]
            )
        ]

    def __init__(self, name: str, options: list = ()):
        self.name = name
        if len(options) > 0:
            self.options.append(options)

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