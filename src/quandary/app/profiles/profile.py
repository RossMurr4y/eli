"""

A profile is a predefined combination of user settings that configures quandary and quandary extensions.
"""

from abc import ABCMeta, abstractmethod
from os import environ

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
        #todo: load the default profile? or
        #todo: retrieve the profile from its definition

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
        # for every profile in registered_profiles, loop over them and add to profile_options
        # which is used to populate the profile selector dropdown
        self.data = list(data)
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
        i = len(self.registered_profiles) - 1
        for p in self.registered_profiles:
            self.profile_selection.append((p.name, i))
            i += 1