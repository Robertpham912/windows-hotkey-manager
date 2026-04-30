import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow
from hotkey_manager import HotkeyManager
from config import ConfigManager

def main():
    # Initialize Qt Application
    app = QApplication(sys.argv)
    
    # Initialize config manager
    config_manager = ConfigManager('hotkeys.json')
    
    # Initialize hotkey manager
    hotkey_manager = HotkeyManager()
    hotkey_manager.start()
    
    # Create and show main window
    main_window = MainWindow()
    main_window.show()
    
    # Run application
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
