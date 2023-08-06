from textual.app import ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Input, Static, Markdown
from textual.reactive import reactive

from quandary.app.utils import run_quandary

class InputPane(Static):

    input_text = reactive("")

    """A widget to accept and send input"""
    def compose(self) -> ComposeResult:
        """child widgets of an InputPane"""
        yield Input(placeholder="What do you want to know?")

    def on_input_changed(self, event: Input.Changed) -> None:
        self.input_text = event.input.value

    def clear_input(self) -> None:
        """Updates the input field"""
        self.query_one(Input).value = ""

    def submit_question(self, question):
        """submits a question to quandary"""
        answer = run_quandary(question)
        return answer

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

    def on_input_submitted(self, event: Input.Submitted) -> None:
        input_pane = self.query_one(InputPane)
        response_pane = self.query_one(ResponsePane)
        response_pane.clear_markdown()
        # submit prompt
        answer = input_pane.submit_question(event.input.value).response
        # clear input
        self.query_one(InputPane).clear_input()
        # display answer
        response_pane.update_markdown(answer)
