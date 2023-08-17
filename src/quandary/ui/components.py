from textual.app import ComposeResult
from textual.containers import VerticalScroll, Container
from textual.widgets import Static, Header, Footer
from textual.screen import Screen
from quandary.ui.widgets.NavigationTabs import NavigationTabs
from quandary.ui.widgets.InputPanel import InputPanel

class BorderTop(Static):
    """A border for the top of the application."""
    def compose(self) -> ComposeResult:
        yield Header()

class BorderBottom(Static):
    """A border for the bottom of the application."""
    def compose(self) -> ComposeResult:
        yield Footer()

class ScreenBody(Static):
    """The body content for the main screen."""

    def compose(self) -> ComposeResult:
        yield Container(
            VerticalScroll(
                NavigationTabs(id="screen_body_tab_nav"),
                id="screen_body_top_v_scroll"),
            id="screen_body_outer_container")

        
class MainScreen(Screen):
    """The primary display screen for quandary."""
    def compose(self) -> ComposeResult:
        yield BorderTop()
        yield ScreenBody()
        yield BorderBottom()
