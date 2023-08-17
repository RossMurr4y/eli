from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Static
from quandary.ui.widgets.SwitchSetting import SwitchSetting

class SettingsTab(Static):
    """the settings tab of the main navigation window."""

    def compose(self) -> ComposeResult:
        yield Horizontal(
            SwitchSetting(id="setting_doc_mode", enabled=True, label="Document Mode:      "),
            classes="container"
        )