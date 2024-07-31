from textual.app import ComposeResult
from textual.widgets import Input, Static, Select
from textual.containers import Horizontal
from textual.reactive import reactive
from ..widgets import SwitchSetting
from ...app.profiles import Profiles


class InputPanel(Static):
    """The user input text panel for submitting new questions."""

    profiles = Profiles()
    active_profile_selection = reactive(profiles.DEFAULT_PROFILE_SELECTION)

    def compose(self) -> ComposeResult:
        profile_selection = self.profiles.profile_selection
        with Horizontal():
            yield Select(
                profile_selection,
                prompt=self.profiles.DEFAULT_PROFILE_SELECTION[0],
                id="select_profile",
            )
            yield Input(
                id="text_input_field", placeholder="What do you want to know?"
            )
            yield SwitchSetting(id="qol_mode_toggle", label="", enabled=True)

    def on_select_changed(self, event: Select.Changed) -> None:
        """set the selected profile as active and evaluate its options"""
        if isinstance(event.value, int):
            # set the currently active profile to the newly selected one
            self.active_profile_selection = self.profiles.profile_selection[
                event.value
            ]
            # retrieve the profile object
            profile = self.profiles.registered_profiles[event.value]
            # process any profile-specific options
            profile.process_profile_options()
