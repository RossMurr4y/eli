from textual.app import ComposeResult
from textual.widgets import Static, Placeholder
from textual.containers import Vertical

from .console import Console

class Debug(Static):
    """the debug tab of the primary ui screen"""
    
    def compose(self) -> ComposeResult:
        with Vertical():
            yield Console(
                id="debug_console"
            )