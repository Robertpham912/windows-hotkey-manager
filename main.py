import sys
import ctypes  # Thư viện để kiểm tra quyền Admin
from PyQt5.QtWidgets import QApplication, QMessageBox
from ui.main_window import MainWindow
from hotkey_manager import HotkeyManager
from config import ConfigManager

def is_admin():
    """Kiểm tra xem ứng dụng có đang chạy với quyền Administrator không."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def main():
    # Bước 1: Kiểm tra quyền truy cập hệ thống
    if not is_admin():
        # Nếu không có quyền, yêu cầu Windows chạy lại với quyền Admin
        # 'runas' sẽ kích hoạt hộp thoại xin quyền (UAC)
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

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
