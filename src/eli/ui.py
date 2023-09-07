from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

class Ui(App):
    """User Interface for Eli"""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    """keybindings for the UI"""

    def compose(self) -> ComposeResult:
        yield Header();
        yield Footer(); 