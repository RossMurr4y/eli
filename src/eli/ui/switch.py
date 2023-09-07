from textual.app import ComposeResult
from textual.reactive import reactive
from textual.widgets import Static, Switch
from textual.containers import Horizontal


class SwitchSetting(Static):
    """a binary configuration setting exposed as a switch with a descriptive label"""

    id = ""
    enabled = True
    label = ""

    def __init__(self, id: str, label: str, enabled: bool) -> None:
        self.id = id
        self.label = label
        self.enabled = enabled
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Horizontal(
            Static(self.label, classes="label"),
            Switch(value=self.enabled),
            classes="container",
        )
