from textual.app import ComposeResult
from textual.containers import ScrollableContainer, VerticalScroll, Container
from textual.widgets import Input, Static, Markdown, TabbedContent, Placeholder, Header, Footer, Pretty
from textual.reactive import reactive
from textual.screen import Screen
from datetime import datetime

from quandary.app.utils import run_quandary, run_lang_quandary
from quandary.ui.widgets.SettingsTab import SettingsTab
from quandary.ui.widgets.SwitchSetting import SwitchSetting
from quandary.ui.widgets.DebugTab import DebugTab, DebugPanel
from quandary.ui.widgets.ResponsePanel import ResponsePanel

class TabbedNavigation(TabbedContent):
    """The navigation pane"""
    def compose(self) -> ComposeResult:
        with TabbedContent("Response", "Debug", "Settings"):
            yield ResponsePanel()
            yield DebugTab()
            yield SettingsTab()

    def on_switch_setting_changed(self, event: SwitchSetting.Changed) -> None:
        """when a SwitchSetting is toggled, log that to the debug pane."""
        debug_panel = self.query_one(DebugPanel)
        output = [{
            "id": event.id,
            "enabled": event.enabled
        }]
        debug_panel.append(output)

class InputPane(Static):
    """A widget to accept and send input"""
    DEFAULT_CSS = """
    InputPane {
        height: 1fr;
        width: 1fr;
    }
    """
    def compose(self) -> ComposeResult:
        """child widgets of an InputPane"""
        yield Input(id="text_input_field", placeholder="What do you want to know?")

class BorderTop(Static):
    """A border for the top of the application."""
    DEFAULT_CSS = """
    BorderTop {
        height: 1;
        dock: top;
    }
    """
    def compose(self) -> ComposeResult:
        yield Header()

class BorderBottom(Static):
    """A border for the bottom of the application."""
    DEFAULT_CSS = """
    BorderBottom {
        height: 1;
        dock: bottom;
    }
    """
    def compose(self) -> ComposeResult:
        yield Footer()

class ScreenBody(Static):
    """The body content for the main screen."""
    DEFAULT_CSS = """
    ScreenBody {
        width: 1fr;
        height: 1fr;
        border: solid white;
        padding: 1;
    }

    #screen_body_tab_nav {
        dock: top;
        height: 1fr;
    }

    #screen_body_top_v_scroll {
        dock: top;
        height: 1fr;
    }

    #screen_body_bottom_v_scroll {
        dock: bottom;
        height: 3;
    }

    #screen_body_input_pane {
        dock: top;
    }
    """

    input_text = reactive("")
    def on_input_changed(self, event: Input.Changed) -> None:
        self.input_text = event.input.value

    def on_input_submitted(self, event: Input.Submitted) -> None:
        input_pane = self.query_one(InputPane)
        response_panel = self.query_one(ResponsePanel)
        debug_panel = self.query_one(DebugPanel)
        response_panel.clear()
        # update the debug pane with new prompt
        debug_panel.append(event.input)
        # submit prompt
        answer = self.submit_question(event.input.value)
        # clear input
        self.clear_input()
        # update the debug pane with answer
        debug_panel.append(answer)
        # display answer
        response_panel.update(answer.response)

    def clear_input(self) -> None:
        """resets the input field"""
        self.query_one("#text_input_field", Input).value = ""

    def submit_question(self, question):
        """submits a question to quandary"""
        answer = run_lang_quandary(question)
        return answer

    def compose(self) -> ComposeResult:
        yield Container(
            VerticalScroll(
                NavigationTabs(id="screen_body_tab_nav"),
                id="screen_body_top_v_scroll"),
            VerticalScroll(
                InputPanel(id="screen_body_input_pane"),
                id="screen_body_bottom_v_scroll"),
            id="screen_body_outer_container")

        
class MainScreen(Screen):
    """The primary display screen for quandary."""
    def compose(self) -> ComposeResult:
        yield BorderTop()
        yield ScreenBody()
        yield BorderBottom()
