from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Static
from quandary.ui.widgets.SwitchSetting import SwitchSetting

class SettingsTab(Static):
    """the settings tab of the main navigation window."""

    DEFAULT_CSS = """
    SettingsTab {
        width: 1fr;
        height: auto;
        border: heavy $primary;
    }
    """

    def compose(self) -> ComposeResult:
        yield Horizontal(
            SwitchSetting(enabled=True, label="Document Mode:      "),
            classes="container"
        )