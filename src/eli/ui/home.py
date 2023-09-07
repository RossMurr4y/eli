from textual.app import ComposeResult
from textual.widgets import Static, Placeholder
from textual.containers import Vertical

from .qanda import Qanda

class Home(Static):
    """the home tab of the primary ui screen"""
    
    def compose(self) -> ComposeResult:
        with Vertical():
            yield Qanda(
                id="home_qanda"
            )