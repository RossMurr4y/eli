from quandary.ui.app import TerminalInterface

def start_tui():
    app = TerminalInterface()
    app.run()

if __name__ == '__main__':
    start_tui()