from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Input, Static, Header, Footer, Markdown
from textual.reactive import reactive
from llama_index import VectorStoreIndex, SimpleDirectoryReader, download_loader, StorageContext, load_index_from_storage
from dotenv import load_dotenv
import openai
import os
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

class TerminalInterface(App):
    """A Terminal User Interface (TUI) for quandary."""
    CSS_PATH = "terminalinterface.css"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode.")]

    def compose(self) -> ComposeResult:
        """Compose the child widgets for the ui"""
        yield Header()
        yield QandAPane()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """Toggle dark mode"""
        self.dark = not self.dark

def run_quandary(question):

    # Run
    load_dotenv()

    # Constants
    OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
    QNDY_DOCS_PATH = os.environ['QNDY_DOCS_PATH']
    QNDY_INDEX_PATH = os.environ['QNDY_INDEX_PATH']
    openai.api_key = OPENAI_API_KEY

    reader = download_loader('ObsidianReader')
    documents = reader(QNDY_DOCS_PATH).load_data()

    if os.path.exists(QNDY_INDEX_PATH):
        # index already exists, so load it in
        storage_context = StorageContext.from_defaults(persist_dir=QNDY_INDEX_PATH)
        index = load_index_from_storage(storage_context)
    else:
        # create index and persist it
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist()

    query_engine = index.as_query_engine()

    response = query_engine.query(question)
    return response

def start_tui():
    app = TerminalInterface()
    app.run()