"""

An Eli profile used to configure Eli behaviour for a specific use-case.
"""

from configurable import Configurable


class NoProfile(Exception):
    """A profile was not found."""


class NoProfileSetting(Exception):
    """A profile setting was not found."""


class ProfileAlreadyExists(Exception):
    """A profile already exists with that name."""


class Profile(Configurable):
    """The base class for a Profile."""

    def __init__(
        self,
        name: str,
        debug: bool,
        cls_on_submit: bool,
        model: any,
    ):
        self.name = name
        self.debug = debug
        self.cls_on_submit = cls_on_submit
        self.model = model

    def new(name, debug, cls_on_submit, model):
        return Profile(
            name=name, debug=debug, cls_on_submit=cls_on_submit, model=model
        )


class _Profiles(Configurable):
    """manage a collection of profiles."""

    _DEFAULT_PROFILES = [
        Profile(name="Eli", debug=False, cls_on_submit=True, model=""),
        Profile(name="Debugger", debug=True, cls_on_submit=True, model=""),
    ]

    def __init__(self, profiles):
        self.loaded = {}
        self.load(self._DEFAULT_PROFILES)
        self.load(profiles)

    def load(self, profiles: [Profile]):
        try:
            for profile in profiles:
                name = profile.name
                self.loaded.update({name: profile})
        except:
            raise ProfileAlreadyExists(
                f"A profile called {profile.name} already exists."
            )

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
            raise NoProfileSetting(
                f"Profile {name} does not have the setting: {setting}"
            )
