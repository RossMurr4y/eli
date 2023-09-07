from textual.app import ComposeResult
from textual.reactive import reactive
from textual.widgets import Static, Switch
from textual.containers import Horizontal
from textual.widgets import Static, RichLog
from datetime import datetime

class Console(Static):
    """a debug console widget"""

    id = ""

    def __init__(self, id: str) -> None:
        self.id = id
        super().__init__()

    def on_mount(self) -> None:
        self.log(f"initialsed.")

    def compose(self) -> ComposeResult:
        yield RichLog(highlight=True, markup=True, id="console")

    def clear(self) -> None:
        """clears the console"""
        self.query_one(RichLog).clear()

    def log(self, content: str) -> None:
        """appends new content to the console"""
        self.query_one(RichLog).write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {content}")