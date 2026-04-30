import json
import os
from models import Hotkey

class ConfigManager:
    def __init__(self, file_path='hotkeys.json'):
        self.file_path = file_path

    def save_config(self, hotkeys):
        """Lưu danh sách đối tượng Hotkey vào JSON."""
        data = [hk.to_dict() for hk in hotkeys]
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump({"hotkeys": data}, f, indent=4)

    def load_config(self):
        """Tải dữ liệu và chuyển thành danh sách đối tượng Hotkey."""
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [Hotkey.from_dict(item) for item in data.get("hotkeys", [])]
        except (json.JSONDecodeError, FileNotFoundError):
            return []
