from textual.widgets import Static
from textual.app import ComposeResult
from quandary.ui.widgets.ResponsePanel import ResponsePanel

class ResponseTab(Static):
    """the response tab of the main navigation window"""

    DEFAULT_CSS = """
    ResponseTab {}
    """

    def compose(self) -> ComposeResult:
        yield ResponsePanel()