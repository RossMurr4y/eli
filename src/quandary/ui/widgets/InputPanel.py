from textual.app import ComposeResult
from textual.widgets import Input, Static, Select
from textual.containers import Horizontal
from textual.reactive import reactive
from ..widgets import SwitchSetting

class InputPanel(Static):
    """The user input text panel for submitting new questions."""

    PROFILES = [
       ( "one", 1),
        ("two", 2),
        ("three", 3),
    ]
    current_profile = reactive("two")

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Select(self.PROFILES, prompt=self.current_profile, id="select_profile")
            yield Input(
                id="text_input_field", placeholder="What do you want to know?"
            )
            yield SwitchSetting(id="qol_mode_toggle", label="", enabled=True)
