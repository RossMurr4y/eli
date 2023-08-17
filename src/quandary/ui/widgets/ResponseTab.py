from textual.widgets import Static
from textual.app import ComposeResult
from textual.containers import Vertical
from quandary.ui.widgets.ResponsePanel import ResponsePanel
from quandary.ui.widgets.InputPanel import InputPanel

class ResponseTab(Static):
    """the response tab of the main navigation window"""

    def compose(self) -> ComposeResult:
        with Vertical():
            yield ResponsePanel()
            yield InputPanel()