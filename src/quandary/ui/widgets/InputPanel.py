from textual.app import ComposeResult
from textual.widgets import Input, Static, Select
from textual.containers import Horizontal
from textual.reactive import reactive
from ..widgets import SwitchSetting
from ...app.profiles import Profile, Profiles, ProfileOption

class InputPanel(Static):
    """The user input text panel for submitting new questions."""

    profiles = Profiles()
    #profiles.add(Profile("Debugger", []))
    #profiles.add(Profile("Flibberdy", []))

    active_profile_selection = reactive(profiles.DEFAULT_PROFILE_SELECTION)

    def compose(self) -> ComposeResult:
        profile_selection = self.profiles.profile_selection
        with Horizontal():
            yield Select(profile_selection, prompt=self.profiles.DEFAULT_PROFILE_SELECTION[0], id="select_profile")
            yield Input(
                id="text_input_field", placeholder="What do you want to know?"
            )
            yield SwitchSetting(id="qol_mode_toggle", label="", enabled=True)

    def on_select_changed(self, event: Select.Changed) -> None:
        """set the selected profile as active"""
        if isinstance(event.value, int):
            self.active_profile_selection = self.profiles.profile_selection[event.value]