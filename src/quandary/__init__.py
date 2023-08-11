from quandary.ui.app import TerminalInterface, Quandary

def start_tui():
    app = Quandary()
    app.run()

if __name__ == '__main__':
    start_tui()