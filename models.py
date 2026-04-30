class Hotkey:
    """
    Lớp dùng để định nghĩa một phím tắt trong hệ thống.
    """
    def __init__(self, name, keys, action):
        self.name = name    # Tên gợi nhớ (ví dụ: 'Mở Notepad')
        self.keys = keys    # Tổ hợp phím (ví dụ: 'ctrl+alt+n')
        self.action = action # Hành động (ví dụ: đường dẫn ứng dụng hoặc lệnh)

    def to_dict(self):
        """
        Chuyển đổi đối tượng Hotkey thành một Dictionary.
        Mục đích: Để có thể lưu trực tiếp vào file JSON thông qua ConfigManager.
        """
        return {
            "name": self.name,
            "keys": self.keys,
            "action": self.action
        }

    @classmethod
    def from_dict(cls, data):
        """
        Tạo lại một đối tượng Hotkey từ dữ liệu Dictionary (đọc từ file JSON).
        """
        return cls(
            name=data.get("name"),
            keys=data.get("keys"),
            action=data.get("action")
        )

    def __repr__(self):
        # Giúp việc in đối tượng ra màn hình để debug dễ nhìn hơn
        return f"Hotkey(name='{self.name}', keys='{self.keys}', action='{self.action}')"
