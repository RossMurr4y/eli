from textual.app import ComposeResult
from textual.message import Message
from textual.reactive import reactive
from textual.widgets import Static, Switch
from textual.containers import Horizontal


class SwitchSetting(Static):
    """A binary configuration setting, exposed as a switch with a descriptive label"""

    id = ""
    enabled = reactive(True)
    label = "label_missing"

    class Changed(Message):
        """A message that is sent when a SwitchSetting is toggled"""

        def __init__(self, id: str, label: str, enabled: bool) -> None:
            super().__init__()
            self.id = id
            self.label = label
            self.enabled = enabled

    def __init__(self, id: str, label: str, enabled: bool) -> None:
        self.id = id
        self.enabled = enabled
        self.label = label
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Horizontal(
            Static(self.label, classes="label"),
            Switch(value=self.enabled),
            classes="container",
        )

    def on_switch_changed(self, event: Switch.Changed):
        # disable the bubbling of the initial Switch.Changed event
        event.stop()
        # update the widget state based on the event value
        self.enabled = event.value
        # bubble a message to the parent
        self.post_message(
            self.Changed(id=self.id, label=self.label, enabled=self.enabled)
        )
