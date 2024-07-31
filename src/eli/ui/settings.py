from textual.app import ComposeResult
from textual.widgets import Static, Placeholder
from textual.containers import Vertical

from .switch import SwitchSetting


class Settings(Static):
    """the settings tab of the primary ui screen"""

    def compose(self) -> ComposeResult:
        with Vertical(classes="container"):
            yield SwitchSetting(
                id="setting_model", enabled=True, label="Model:             "
            )
            yield SwitchSetting(
                id="setting_cls_on_submit",
                enabled=True,
                label="Refresh on Submit: ",
            )
