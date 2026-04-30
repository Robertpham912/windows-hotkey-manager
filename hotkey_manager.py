from pynput import keyboard
import subprocess

class HotkeyManager:
    def __init__(self):
        self.hotkeys_map = {}
        self.listener = None

    def format_key_for_pynput(self, keys_str):
        """Chuyển đổi 'Ctrl+Alt+S' thành '<ctrl>+<alt>+s'."""
        parts = keys_str.lower().split('+')
        formatted = []
        for p in parts:
            p = p.strip()
            if p in ['ctrl', 'alt', 'shift', 'win']:
                formatted.append(f'<{p}>')
            else:
                formatted.append(p)
        return "+".join(formatted)

    def execute_action(self, action):
        try:
            subprocess.Popen(action, shell=True)
        except Exception as e:
            print(f"Lỗi thực thi lệnh {action}: {e}")

    def update_hotkeys(self, hotkey_list):
        """Nhận danh sách đối tượng Hotkey và chuẩn bị listener."""
        self.hotkeys_map = {}
        for hk in hotkey_list:
            pynput_key = self.format_key_for_pynput(hk.keys)
            # Dùng lambda với tham số mặc định để tránh lỗi lặp biến
            self.hotkeys_map[pynput_key] = lambda a=hk.action: self.execute_action(a)

    def start(self):
        if self.listener: self.listener.stop()
        self.listener = keyboard.GlobalHotkeys(self.hotkeys_map)
        self.listener.start()

    def stop(self):
        if self.listener: self.listener.stop()
