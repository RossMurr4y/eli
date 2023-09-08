"""

The base class for the Eli application.
"""

from pathlib import Path
from textual.reactive import reactive
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Select
from pathlib import Path

from configurable import Configurable
from profile import Profile
from config import Config
from config import Config
from ui.screen import PrimaryScreen


class Eli(App):

    config = reactive({})
    profiles = reactive({})

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    """keybindings for the UI"""

    CSS_PATH = "ui/terminalinterface.css"

    def compose(self) -> ComposeResult:
        yield Header()
        yield PrimaryScreen()
        yield Footer()

    def on_mount(self):
        self.config = Config.from_file(path=Path.home().joinpath(Path.home(), ".eli.yml"))
        self.profiles = _Profiles(self.config.profiles).loaded

    def watch_profiles(self, new_profiles) -> None:
        """sets the options on the select widget when profiles change"""
        selection = []
        for profile in new_profiles.values():
            selection.append((profile.name, profile))
        self.query_one("#qanda_input_select", Select).set_options(selection)

class NoProfile(Exception):
    """A profile was not found."""

class NoProfileSetting(Exception):
    """A profile setting was not found."""

class ProfileAlreadyExists(Exception):
    """A profile already exists with that name."""

class _Profiles(Configurable):
    """manage a collection of profiles."""

    _DEFAULT_PROFILES = [
        Profile(name="Eli", debug=False, cls_on_submit=True, model=""),
        Profile(name="Debugger", debug=True, cls_on_submit=True, model=""),
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