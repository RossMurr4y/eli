from textual.app import ComposeResult
from textual.widgets import Static, RichLog
from datetime import datetime


class DebugPanel(Static):
    """The debug output panel on the debug tab of the main navigation"""

    id = ""
    output = [{"DebugInitialised": f"{datetime.now()}"}]

    def compose(self) -> ComposeResult:
        yield RichLog(highlight=True, markup=True, id="debug_panel_output")

    def clear(self) -> None:
        """clears the debug output panel of content."""
        self.query_one("#debug_panel_output").clear()

    def append(self, content) -> None:
        """appends an object to the end of the debug output content."""
        self.query_one("#debug_panel_output").write(content)
