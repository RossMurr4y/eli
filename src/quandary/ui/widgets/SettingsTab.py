from textual.app import ComposeResult
from textual.widget import Widget
from textual.containers import Horizontal

from quandary.ui.widgets.SwitchSetting import SwitchSetting

class SettingsTab(Widget):
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
            SwitchSetting(enabled=True, description="Document Mode:      "),
            classes="container"
        )