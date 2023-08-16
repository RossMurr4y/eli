from textual.app import App
from quandary.ui.components import MainScreen



class Quandary(App):
    """The Quandary application's terminal user interface (TUI)"""
    CSS_PATH = "terminalinterface.css"
    #BINDINGS = [()]

    def on_mount(self) -> None:
        self.push_screen(MainScreen())