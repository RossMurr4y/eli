from textual.widgets import TabbedContent, Input, Select
from textual.app import ComposeResult
from textual.reactive import reactive
from ..widgets import (
    ResponseTab,
    DebugTab,
    SettingsTab,
    InputPanel,
    ResponsePanel,
    DebugPanel,
    SwitchSetting,
)
from ...app.modelangchain import ModeLangChain, ModeLlamaIndex


class NavigationTabs(TabbedContent):
    """the navigation tabs on the main screen"""

    input_text = reactive("")
    mode = reactive(ModeLangChain())

    def compose(self) -> ComposeResult:
        with TabbedContent("Response", "Debug", "Settings"):
            yield ResponseTab()
            yield DebugTab()
            yield SettingsTab()

    def on_input_changed(self, event: Input.Changed) -> None:
        self.input_text = event.input.value

    def on_input_submitted(self, event: Input.Submitted) -> None:
        response_panel = self.query_one(ResponsePanel)
        debug_panel = self.query_one(DebugPanel)
        # update the debug pane with new prompt
        debug_panel.append(event.input.value)
        # update the response panel with submitted question
        # prepend it with some markdown styles to differentiate
        # q's from a's
        response_panel.append_on_new_line("#### " + event.input.value)
        # submit prompt
        self.submit_question(event.input.value)
        # clear input
        self.clear_input()
        # update the debug pane with answer
        debug_panel.append(str(self.mode.response))
        # display answer
        response_panel.append_on_new_line("> " + self.mode.response.value)

    def clear_input(self) -> None:
        """resets the input field"""
        self.query_one("#text_input_field", Input).value = ""

    def submit_question(self, question) -> None:
        """submits a question to quandary using the currently selected mode"""
        self.mode.question = question
        self.mode.response = self.mode.run()

    def on_switch_setting_changed(self, event: SwitchSetting.Changed) -> None:
        """when a SwitchSetting is toggled, log that to the debug pane."""
        debug_panel = self.query_one(DebugPanel)
        debug_panel.append([{"id": event.id, "enabled": event.enabled}])
        # run the handler for the toggled SwitchSetting
        self.process_setting_event(event)

    def on_select_changed(self, event: Select.Changed) -> None:
        """sets the current profile when a new one has been selected"""
        event.stop()
        debug_panel = self.query_one(DebugPanel)
        input_panel = self.query_one(InputPanel)
        profile = self.query_one(InputPanel).get_current_profile()
        # output a log message to the debug panel
        debug_panel.append([f"Switched to profile: {profile.name}"])

    def process_setting_event(self, event: SwitchSetting.Changed) -> None:
        """routes unique SwitchSetting.Changed events to their handlers"""
        match event.id:
            case "setting_doc_mode":
                self.set_mode(event.enabled)
            case "qol_mode_toggle":
                self.set_mode(event.enabled)
            case _:
                self.set_mode(event.enabled)

    def set_mode(self, enabled) -> None:
        """sets the runtime mode of the response pane."""
        debug_panel = self.query_one(DebugPanel)
        if enabled:
            self.mode = ModeLlamaIndex()
        else:
            self.mode = ModeLangChain()
        debug_panel.append(
            [
                "Runtime mode has been changed",
                f"mode updated to: {self.mode.__class__.__name__}",
            ]
        )
