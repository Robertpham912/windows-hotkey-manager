from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QListWidget, QLabel, QPushButton
from ui.styles import main_window_style

class MainWindow(QMainWindow):
    def __init__(self, config_manager, hotkey_manager):
        super().__init__()
        self.config = config_manager
        self.hkm = hotkey_manager
        self.setWindowTitle("Windows Hotkey Manager")
        self.resize(600, 400)
        self.setStyleSheet(main_window_style)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        self.label = QLabel("Danh sách phím tắt hiện có:")
        layout.addWidget(self.label)

        self.list_widget = QListWidget()
        self.refresh_list()
        layout.addWidget(self.list_widget)

        self.btn_add = QPushButton("➕ New Hotkey")
        # Kết nối nút bấm với chức năng mở cửa sổ tạo (cần import CreateHotkeyWindow)
        layout.addWidget(self.btn_add)

        central_widget.setLayout(layout)

    def refresh_list(self):
        self.list_widget.clear()
        hotkeys = self.config.load_config()
        for hk in hotkeys:
            self.list_widget.addItem(f"{hk.name}: {hk.keys} -> {hk.action}")
