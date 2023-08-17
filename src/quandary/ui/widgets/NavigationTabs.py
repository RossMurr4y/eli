from textual.widgets import TabbedContent, Input
from textual.app import ComposeResult
from textual.reactive import reactive
from quandary.ui.widgets.SwitchSetting import SwitchSetting
from quandary.ui.widgets.ResponsePanel import ResponsePanel
from quandary.ui.widgets.ResponseTab import ResponseTab
from quandary.ui.widgets.DebugTab import DebugTab, DebugPanel
from quandary.ui.widgets.InputPanel import InputPanel
from quandary.ui.widgets.SettingsTab import SettingsTab
from quandary.app.utils import run_quandary, run_lang_quandary


class NavigationTabs(TabbedContent):
    """the navigation tabs on the main screen"""

    input_text = reactive("")

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

    def on_switch_setting_changed(self, event: SwitchSetting.Changed) -> None:
        """when a SwitchSetting is toggled, log that to the debug pane."""
        debug_panel = self.query_one(DebugPanel)
        output = [{
            "id": event.id,
            "enabled": event.enabled
        }]
        debug_panel.append(output)