from textual.app import ComposeResult
from textual.widgets import Static, Pretty
from datetime import datetime

class DebugPanel(Static):
    """The debug output panel on the debug tab of the main navigation"""

    DEFAULT_CSS = """
    DebugPanel {}
    """

    id = ""
    output = [{ "DebugInitialised": f"{datetime.now()}" }]

    def compose(self) -> ComposeResult:
        yield Pretty(self.output, id="debug_panel_output")

    def clear(self) -> None:
        """clears the debug output panel of content."""
        self.query_one("#debug_panel_output").update("")

    def append(self, content: list) -> None:
        """appends an object to the end of the debug output content."""
        self.output.append(content)
        self.query_one("#debug_panel_output").update(self.output)