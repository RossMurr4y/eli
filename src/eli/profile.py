"""

An Eli profile.
"""

import json

class NoProfile(Exception):
    """A profile was not found."""

class NoProfileSetting(Exception):
    """A profile setting was not found."""

class ProfileAlreadyExists(Exception):
    """A profile already exists with that name."""

class Profile():
    """The base class for a Profile."""

    def __init__(
        self,
        name: str,
        debug: bool,
        cls_on_submit: bool,
        model: any
    ):
        self.name = name
        self.debug = debug
        self.cls_on_submit = cls_on_submit
        self.model = model

    def __repr__(self):
        return f"Profile(name: {self.name}, debug: {self.debug}, cls_on_submit: {self.cls_on_submit}, model: {self.model})"

class _Profiles:
    """manage a configuration of profiles."""

    _DEFAULT_PROFILES = [
        Profile(name="Eli", debug=False, cls_on_submit=True, model=""),
        Profile(name="Debugger", debug=True, cls_on_submit=True, model=""),
    ]
    
    def __init__(self, profiles):
        self.loaded = {}
        for _default_profile in self._DEFAULT_PROFILES:
            self.load_profile(_default_profile)
        for profile in profiles:
            self.load_profile(profile)

    def load_profile(self, profile: Profile):
        try:
            return self.loaded.update({profile.name: profile})
        except:
            raise ProfileAlreadyExists(f"A profile called {profile.name} already exists.")

    def get_profile(self, name: str):
        try:
            return self.loaded[name]
        except:
            raise NoProfile(f"Profile not found: {name}.")

    def get_profile_setting(self, name: str, setting: str):
        profile = self.get_profile(name)
        try:
            return profile[setting]
        except:
            raise NoProfileSetting(f"Profile {name} does not have the setting: {setting}")