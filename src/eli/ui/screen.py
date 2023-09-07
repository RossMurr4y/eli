from textual.app import ComposeResult
from textual.widgets import Static, TabbedContent, Placeholder

from .home import Home
from .debug import Debug
from .settings import Settings


class PrimaryScreen(Static):
    """The primary textualise screen"""

    def compose(self) -> ComposeResult:
        with TabbedContent("home", "debug", "settings"):
            yield Home()
            yield Debug()
            yield Settings()
