from textual.app import ComposeResult
from textual.widgets import Input, Static, Select
from textual.containers import Horizontal
from textual.reactive import reactive
from ..widgets import SwitchSetting
from ...app.profiles import Profile

class InputPanel(Static):
    """The user input text panel for submitting new questions."""

    PROFILES = [
        Profile(name="Default", debug=False),
        Profile(name="Debugger", debug=True),
        Profile(name="Flibberdy", debug=False),
    ]

    current_profile = reactive(("Default", 0))

    def compose(self) -> ComposeResult:
        opts = Profile.get_profile_options(self.PROFILES)
        with Horizontal():
            yield Select(opts, prompt="flibs", id="select_profile")
            yield Input(
                id="text_input_field", placeholder="What do you want to know?"
            )
            yield SwitchSetting(id="qol_mode_toggle", label="", enabled=True)

    def set_profile(self, profile: Profile) -> None:
        self.current_profile = profile

    def on_select_changed(self, event: Select.Changed) -> None:
        """update the current profile when a new one is selected"""
        self.current_profile = event.value

    def get_current_profile(self) -> Profile:
        """retrieves the current profile object"""
        return self.PROFILES[self.current_profile]