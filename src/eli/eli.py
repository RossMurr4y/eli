"""

The base class for the Eli application.
"""

from pathlib import Path
from textual import on
from textual.reactive import reactive
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Select, RichLog
from pathlib import Path

from config import Config
from profiles import _Profiles
from ui.screen import PrimaryScreen


class Eli(App):

    config = reactive({})
    profiles = reactive({})
    debug = reactive(False)
    cls_on_submit = reactive(True)
    model = reactive('')
    
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    """keybindings for the UI"""

    CSS_PATH = "ui/terminalinterface.css"

    def compose(self) -> ComposeResult:
        yield Header()
        yield PrimaryScreen()
        yield Footer()

    def on_mount(self):
        self.config = Config.from_file(path=Path.home().joinpath(Path.home(), ".eli.yml"))
        self.profiles = _Profiles(self.config.profiles).loaded

    def watch_profiles(self, new_profiles) -> None:
        """sets the options on the select widget when profiles change"""
        selection = []
        for profile in new_profiles.values():
            selection.append((profile.name, profile))
        self.query_one("#qanda_input_select", Select).set_options(selection)

    @on(Select.Changed, "#qanda_input_select")
    def handle_profile_updated(self, event: Select.Changed) -> None:
        """updates active settings to match selected profile"""
        profile_settings = event.value
        self.debug = profile_settings.debug
        self.cls_on_submit = profile_settings.cls_on_submit
        self.model = profile_settings.model
        self.query_one("#debug_console").log(f"Profile changed to {profile_settings.name}.")

