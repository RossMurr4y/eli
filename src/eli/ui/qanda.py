from textual.app import ComposeResult
from textual.reactive import reactive
from textual.widgets import Static, MarkdownViewer, Markdown, Select, Input
from textual.containers import Vertical
from textual.widgets import Static, RichLog
from datetime import datetime

from .input import QandaInput

class Qanda(Static):
    """A Q-and-A widget"""

    id = ""
    content = ""

    def __init__(self, id: str, content: str = "# Home") -> None:
        self.id = id
        self.content = content
        super().__init__()

    def compose(self) -> ComposeResult:
        with Vertical(classes="container"):
            yield MarkdownViewer(self.content, show_table_of_contents=False)
            yield QandaInput()

    def clear(self) -> None:
        """clears the qanda markdown content"""
        self.content = ""
        self.query_one(MarkdownViewer).update(self.content)

    def update(self, content: str) -> None:
        """updates the qanda markdown content"""
        self.query_one(MarkdownViewer).update(content)