from textual.app import ComposeResult
from textual.reactive import reactive
from textual.widgets import Static, MarkdownViewer, Markdown, Select, Input
from textual.containers import Horizontal
from textual.widgets import Static, RichLog
from datetime import datetime

from .switch import SwitchSetting


class QandaInput(Static):
    """A text input widget for the qanda widget"""

    def compose(self) -> ComposeResult:
        with Horizontal(classes="container"):
            yield Select(
                [], prompt="Select a Profile", id="qanda_input_select"
            )
            yield Input(
                placeholder="What do you want to know?", id="qanda_input_input"
            )
            yield SwitchSetting(
                label="", enabled=True, id="qanda_input_switch_setting"
            )
