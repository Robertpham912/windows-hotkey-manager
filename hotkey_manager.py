from pynput import keyboard
import subprocess

class HotkeyManager:
    def __init__(self):
        # Danh sách lưu trữ các phím tắt đang hoạt động
        self.hotkeys_map = {}
        self.listener = None

    def execute_command(self, command):
        """Hàm thực hiện lệnh mở ứng dụng"""
        try:
            print(f"Thực hiện lệnh: {command}")
            subprocess.Popen(command, shell=True)
        except Exception as e:
            print(f"Lỗi khi thực hiện: {e}")

    def setup_hotkeys(self, hotkey_list):
        """
        Nhận danh sách phím tắt từ ConfigManager và chuẩn bị định dạng
        hotkey_list: danh sách các dictionary [{'keys': 'ctrl+alt+n', 'command': 'notepad.exe'}, ...]
        """
        self.hotkeys_map = {}
        for item in hotkey_list:
            # Định dạng của pynput cho tổ hợp phím là '<ctrl>+<alt>+n'
            # Chúng ta sẽ chuyển đổi từ 'ctrl+alt+n' sang định dạng chuẩn
            formatted_keys = item['keys'].replace('ctrl', '<ctrl>').replace('alt', '<alt>').replace('shift', '<shift>')
            
            # Gán tổ hợp phím với hàm thực thi
            self.hotkeys_map[formatted_keys] = lambda cmd=item['command']: self.execute_command(cmd)

    def start(self):
        """Bắt đầu lắng nghe phím tắt toàn cục"""
        if self.listener:
            self.listener.stop()
            
        # Khởi tạo GlobalHotkeys với danh sách đã chuẩn bị
        self.listener = keyboard.GlobalHotkeys(self.hotkeys_map)
        self.listener.start()
        print("Trình quản lý phím tắt (pynput) đã bắt đầu.")

    def stop(self):
        """Dừng lắng nghe"""
        if self.listener:
            self.listener.stop()
            print("Đã dừng lắng nghe phím tắt.")
