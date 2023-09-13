from configurable import Configurable
from profile import Profile

class NoProfile(Exception):
    """A profile was not found."""

class NoProfileSetting(Exception):
    """A profile setting was not found."""

class ProfileAlreadyExists(Exception):
    """A profile already exists with that name."""

class _Profiles(Configurable):
    """manage a collection of profiles."""

    _DEFAULT_PROFILES = [
        Profile(name="Eli", debug=False, cls_on_submit=True, model="", incl_docs=False),
        Profile(name="Debugger", debug=True, cls_on_submit=True, model="", incl_docs=False),
    ]

    loaded = {}
    active_profile = {}

    def __init__(self, profiles):
        self.loaded = {}
        self.load(self._DEFAULT_PROFILES)
        self.load(profiles)
        self.active_profile = self.loaded['Eli']

    def load(self, profiles: [Profile]):
        try:
            for profile in profiles:
                name = profile.name
                self.loaded.update({name: profile})
        except:
            raise self.ProfileAlreadyExists(
                f"A profile called {profile.name} already exists."
            )

    def get_profile(self, name: str):
        try:
            return self.loaded[name]
        except:
            raise self.NoProfile(f"Profile not found: {name}.")

    def get_profile_setting(self, name: str, setting: str):
        profile = self.get_profile(name)
        try:
            return profile[setting]
        except:
            raise self.NoProfileSetting(
                f"Profile {name} does not have the setting: {setting}"
            )