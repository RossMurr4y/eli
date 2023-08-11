from textual.app import ComposeResult
from textual.containers import ScrollableContainer, VerticalScroll, Container
from textual.widgets import Input, Static, Markdown, TabbedContent, Placeholder, Header, Footer
from textual.reactive import reactive
from textual.screen import Screen

from quandary.app.utils import run_quandary, run_lang_quandary

class ResponsePane(Static):
    """A widget to view results."""
        
    def compose(self) -> ComposeResult:
        """child widgets of a ResponsePane"""
        MARKDOWN = """
# Default Markdown Doc
"""
        yield Markdown(MARKDOWN)

    def clear_markdown(self) -> None:
        """clears the markdown window"""
        self.query_one(Markdown).update("")

    def update_markdown(self, content) -> None:
        """updates the markdown window content"""
        self.query_one(Markdown).update(content)

class QandAPane(Static):
    """A panel for submitting questions and reading answers"""

    def compose(self) -> ComposeResult:
        yield ScrollableContainer(ResponsePane(), InputPane())

    #def on_input_submitted(self, event: Input.Submitted) -> None:
    #    input_pane = self.query_one(InputPane)
    #    response_pane = self.query_one(ResponsePane)
    #    response_pane.clear_markdown()
    #    # submit prompt
    #    answer = input_pane.submit_question(event.input.value).response
    #    # clear input
    #    self.query_one(InputPane).clear_input()
    #    # display answer
    #    response_pane.update_markdown(answer)


# rewrite starts here

class TabbedNavigation(TabbedContent):
    """The navigation pane"""
    def compose(self) -> ComposeResult:
        with TabbedContent("Response", "Debug", "Settings"):
            yield ResponsePane()
            yield Placeholder()
            yield Placeholder()

class InputPane(Static):
    """A widget to accept and send input"""
    DEFAULT_CSS = """
    InputPane {
        height: 1fr;
        width: 1fr;
    }
    """
    input_text = reactive("")
    def compose(self) -> ComposeResult:
        """child widgets of an InputPane"""
        yield Input(id="text_input_field", placeholder="What do you want to know?")

    #def on_input_changed(self, event: Input.Changed) -> None:
    #    self.input_text = event.input.value

    #def clear_input(self) -> None:
    #    """Updates the input field"""
    #    self.query_one(Input).value = ""

    #def submit_question(self, question):
    #    """submits a question to quandary"""
    #    answer = run_lang_quandary(question)
    #    return answer

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
        response_pane = self.query_one(ResponsePane)
        response_pane.clear_markdown()
        # submit prompt
        answer = self.submit_question(event.input.value).response
        # clear input
        self.clear_input()
        # display answer
        response_pane.update_markdown(answer)

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
                TabbedNavigation(id="screen_body_tab_nav"),
                id="screen_body_top_v_scroll"),
            VerticalScroll(
                InputPane(id="screen_body_input_pane"),
                id="screen_body_bottom_v_scroll"),
            id="screen_body_outer_container")

        
class MainScreen(Screen):
    """The primary display screen for quandary."""
    def compose(self) -> ComposeResult:
        yield BorderTop()
        yield ScreenBody()
        yield BorderBottom()
