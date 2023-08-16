from textual.app import ComposeResult
from textual.message import Message
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Static, Switch
from textual.containers import Horizontal


class SwitchSetting(Widget):
    """A binary configuration setting, exposed as a switch with a descriptive label"""

    DEFAULT_CSS = """
    SwitchSetting {
        width: auto;
        height: auto;
        border: heavy $secondary;
    }

    SwitchSetting > Switch {
        height: auto;
        width: auto;
    }

    .container {
        height: auto;
        width: auto;
    }

    .label {
        height: 3;
        content-align: center middle;
        width: auto;
    }
    """
    description = "default"
    enabled = reactive(True)

    def __init__(self, description: str, enabled: bool) -> None:
        self.enabled = enabled
        self.description = description
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Horizontal(
            Static(self.description, classes="label"),
            Switch(value=self.enabled),
            classes="container"
        )

    class SwitchChanged(Message):
        """A message that is sent when the switch is toggled"""

        def __init__(self, enabled: bool) -> None:
            super().__init__()
            self.enabled = enabled