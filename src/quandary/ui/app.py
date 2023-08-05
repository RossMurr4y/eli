from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
from quandary.ui.components import QandAPane

class TerminalInterface(App):
    """A Terminal User Interface (TUI) for quandary."""
    CSS_PATH = "terminalinterface.css"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode.")]

    def compose(self) -> ComposeResult:
        """Compose the child widgets for the ui"""
        yield Header()
        yield QandAPane()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """Toggle dark mode"""
        self.dark = not self.dark