from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Placeholder

class SettingsTab(Widget):
    """the settings tab of the main navigation window."""
    DEFAULT_CSS = """
    SettingsTab {
        layout: vertical;
        width: auto;
        height: auto;
    }
    SettingsTab > Label {
        text-align: center;
        width: 100%;
    }
    """

    def compose(self) -> ComposeResult:
        yield Placeholder()