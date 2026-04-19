import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QListWidget, QLabel

class HotkeyManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hotkey Manager")
        self.setGeometry(100, 100, 600, 400)

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        label = QLabel("List of Hotkeys:")
        layout.addWidget(label)

        self.hotkey_list = QListWidget()
        # Example hotkeys
        hotkeys = ["Ctrl+C - Copy", "Ctrl+V - Paste", "Alt+Tab - Switch Apps"]
        self.hotkey_list.addItems(hotkeys)
        
        layout.addWidget(self.hotkey_list)
        central_widget.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = HotkeyManager()
    mainWin.show()
    sys.exit(app.exec_())
