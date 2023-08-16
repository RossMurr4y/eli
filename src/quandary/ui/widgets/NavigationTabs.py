from textual.widgets import TabbedContent
from textual.app import ComposeResult
from quandary.ui.widgets.SwitchSetting import SwitchSetting
from quandary.ui.widgets.ResponsePanel import ResponsePanel
from quandary.ui.widgets.DebugTab import DebugTab, DebugPanel
from quandary.ui.widgets.SettingsTab import SettingsTab

class NavigationTabs(TabbedContent):
    """the navigation tabs on the main screen"""
    def compose(self) -> ComposeResult:
        with TabbedContent("Response", "Debug", "Settings"):
            yield ResponsePanel()
            yield DebugTab()
            yield SettingsTab()

    def on_switch_setting_changed(self, event: SwitchSetting.Changed) -> None:
        """when a SwitchSetting is toggled, log that to the debug pane."""
        debug_panel = self.query_one(DebugPanel)
        output = [{
            "id": event.id,
            "enabled": event.enabled
        }]
        debug_panel.append(output)