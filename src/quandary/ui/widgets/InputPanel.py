from textual.app import ComposeResult
from textual.widgets import Input, Static
from textual.containers import Horizontal
from ..widgets import SwitchSetting

class InputPanel(Static):
    """The user input text panel for submitting new questions."""

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Input(
                id="text_input_field", placeholder="What do you want to know?"
            )
            yield SwitchSetting(id="qol_mode_toggle", label="", enabled=True)
