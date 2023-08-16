from textual.app import ComposeResult
from textual.widgets import Static, Markdown

class ResponsePanel(Static):
    """the output panel of the response tab of the main navigation window"""

    DEFAULT_CSS = """
    ResponsePanel {}
    """

    content = ""

    def compose(self) -> ComposeResult:
        yield Markdown(self.content)

    def clear(self) -> None:
        """clears content from the response panel"""
        self.query_one(Markdown).update("")
                                        
    def update(self, content) -> None:
        """updates the response panel with new markdown content"""
        self.query_one(Markdown).update(content)

