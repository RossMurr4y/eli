from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

from .screen import PrimaryScreen


class Ui(App):
    """User Interface for Eli"""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    """keybindings for the UI"""

    CSS_PATH = "terminalinterface.css"

    def compose(self) -> ComposeResult:
        yield Header()
        yield PrimaryScreen()
        yield Footer()
