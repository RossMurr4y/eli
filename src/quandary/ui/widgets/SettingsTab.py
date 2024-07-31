from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widgets import Static
from textual.reactive import reactive
from ..widgets import SwitchSetting


class SettingsTab(Static):
    """the settings tab of the main navigation window."""

    """controls if the response pane should refresh for each question"""
    cls_on_submit = reactive(True)

    def compose(self) -> ComposeResult:
        yield Vertical(
            SwitchSetting(
                id="setting_doc_mode",
                enabled=True,
                label="Document Mode:      ",
            ),
            SwitchSetting(
                id="setting_cls_on_submit",
                enabled=True,
                label="Refresh on Submit:  ",
            ),
            classes="container",
        )
