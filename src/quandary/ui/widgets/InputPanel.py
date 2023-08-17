from textual.app import ComposeResult
from textual.widgets import Input, Static


class InputPanel(Static):
    """The user input text panel for submitting new questions."""

    def compose(self) -> ComposeResult:
        yield Input(id="text_input_field", placeholder="What do you want to know?")
