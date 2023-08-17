from textual.widgets import TabbedContent, Input
from textual.app import ComposeResult
from textual.reactive import reactive
from quandary.ui.widgets.SwitchSetting import SwitchSetting
from quandary.ui.widgets.ResponsePanel import ResponsePanel
from quandary.ui.widgets.ResponseTab import ResponseTab
from quandary.ui.widgets.DebugTab import DebugTab, DebugPanel
from quandary.ui.widgets.InputPanel import InputPanel
from quandary.ui.widgets.SettingsTab import SettingsTab
from quandary.app.utils import run_llama_index_quandary, run_lang_quandary


class NavigationTabs(TabbedContent):
    """the navigation tabs on the main screen"""

    input_text = reactive("")
    mode_handler = reactive("run_lang_quandary")

    def compose(self) -> ComposeResult:
        with TabbedContent("Response", "Debug", "Settings"):
            yield ResponseTab()
            yield DebugTab()
            yield SettingsTab()

    def on_input_changed(self, event: Input.Changed) -> None:
        self.input_text = event.input.value

    def on_input_submitted(self, event: Input.Submitted) -> None:
        input_pane = self.query_one(InputPanel)
        response_panel = self.query_one(ResponsePanel)
        debug_panel = self.query_one(DebugPanel)
        # update the debug pane with new prompt
        debug_panel.append(event.input)
        # update the response panel with submitted question
        # prepend it with some markdown styles to differentiate
        # q's from a's
        response_panel.append_on_new_line("#### " + event.input.value)
        # submit prompt
        answer = self.submit_question(event.input.value)
        # clear input
        self.clear_input()
        # update the debug pane with answer
        debug_panel.append(answer)
        # display answer
        response_panel.append_on_new_line("> " + answer.response)

    def clear_input(self) -> None:
        """resets the input field"""
        self.query_one("#text_input_field", Input).value = ""

    def submit_question(self, question):
        """submits a question to quandary"""
        indirect_function = globals()[self.mode_handler]
        answer = indirect_function(question)
        return answer

    def on_switch_setting_changed(self, event: SwitchSetting.Changed) -> None:
        """when a SwitchSetting is toggled, log that to the debug pane."""
        debug_panel = self.query_one(DebugPanel)
        debug_panel.append([{
            "id": event.id,
            "enabled": event.enabled
        }])
        # run the handler for the toggled SwitchSetting
        self.process_setting_event(event)

    def process_setting_event(self, event: SwitchSetting.Changed) -> None:
        """routes unique SwitchSetting.Changed events to their handlers"""
        match event.id:
            case "setting_doc_mode":
                self.set_mode_handler(event.enabled)
            case _:
                self.set_mode_handler(run_lang_quandary)

    def set_mode_handler(self, enabled) -> None:
        """sets the runtime mode of the response pane."""
        debug_panel = self.query_one(DebugPanel)
        if enabled:
            self.mode_handler = "run_llama_index_quandary"
        else:
            self.mode_handler = "run_lang_quandary"
        debug_panel.append([
            "Runtime mode has been changed", 
            f"mode updated to: {self.mode_handler}"
        ])
        