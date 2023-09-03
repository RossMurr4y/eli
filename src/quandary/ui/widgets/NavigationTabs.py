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
from ...app.logging import QuandaryLog, QuandaryLogType


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
        debug_panel.append(str(QuandaryLog(QuandaryLogType.DEBUG, event.input.value)))
        #debug_panel.append(event.input.value)
        # update the response panel with submitted question
        # prepend it with some markdown styles to differentiate
        # q's from a's
        response_panel.append_on_new_line("💡\n" + event.input.value + "\n💡")
        # submit prompt
        self.submit_question(event.input.value)
        # clear input
        self.clear_input()
        # update the debug pane with answer
        debug_panel.append(str(QuandaryLog(QuandaryLogType.DEBUG, str(self.mode.response))))
        #debug_panel.append(str(self.mode.response))
        # display answer
        response_panel.append_on_new_line("> 🗣️ " + str(self.mode.response.value))
        response_panel.append_line_rule()

    def clear_input(self) -> None:
        """resets the input field"""
        self.query_one("#text_input_field", Input).value = ""

    def submit_question(self, question) -> None:
        """submits a question to quandary using the currently selected mode"""
        # if cls is enabled, clear screen, then submit question otherwise
        # just submit question.
        settings = self.query_one(SettingsTab)
        response = self.query_one(ResponsePanel)
        if settings.cls_on_submit:
            response.clear()
        self.mode.question = question
        self.mode.response = self.mode.run()

    def on_switch_setting_changed(self, event: SwitchSetting.Changed) -> None:
        """when a SwitchSetting is toggled, log that to the debug pane."""
        debug_panel = self.query_one(DebugPanel)
        debug_panel.append(str(QuandaryLog(QuandaryLogType.DEBUG, [{"id": event.id, "enabled": event.enabled}])))
        #debug_panel.append([{"id": event.id, "enabled": event.enabled}])
        # run the handler for the toggled SwitchSetting
        self.process_setting_event(event)

    def on_select_changed(self, event: Select.Changed) -> None:
        """sets the current profile when a new one has been selected"""
        event.stop()
        debug_panel = self.query_one(DebugPanel)
        input_panel = self.query_one(InputPanel)
        profile = input_panel.profiles.registered_profiles[event.value]
        # only write a debug message if an actual selection
        # was made, as opposed to selecting the prompt
        if isinstance(event.value, int):
            debug_panel.append(str(QuandaryLog(QuandaryLogType.DEBUG, f"Profile updated: {str(profile)}")))

    def process_setting_event(self, event: SwitchSetting.Changed) -> None:
        """routes unique SwitchSetting.Changed events to their handlers"""
        match event.id:
            case "setting_doc_mode":
                self.set_mode(event.enabled)
            case "qol_mode_toggle":
                self.set_mode(event.enabled)
            case "setting_cls_on_submit":
                settings = self.query_one(SettingsTab)
                settings.cls_on_submit = event.enabled
            case _:
                self.set_mode(event.enabled)

    def set_mode(self, enabled) -> None:
        """sets the runtime mode of the response pane."""
        debug_panel = self.query_one(DebugPanel)
        if enabled:
            self.mode = ModeLlamaIndex()
        else:
            self.mode = ModeLangChain()
        debug_panel.append(str(QuandaryLog(QuandaryLogType.DEBUG, [
                "Runtime mode has been changed",
                f"mode updated to: {self.mode.__class__.__name__}",
            ])))
