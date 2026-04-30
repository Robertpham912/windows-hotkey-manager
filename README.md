# ⌨️ Windows Hotkey Manager

Một ứng dụng quản lý phím tắt Windows mạnh mẽ để tạo các phím tắt tùy chỉnh cho việc khởi chạy ứng dụng và thực thi các hành động.

## 🎯 Tính Năng

- ✅ Tạo phím tắt tùy chỉnh với bất kỳ tổ hợp phím nào (Ctrl, Shift, Alt, Win)
- ✅ Khởi chạy ứng dụng bằng phím tắt tùy chỉnh
- ✅ Thực thi lệnh hệ thống và các hành động
- ✅ Lưu và tải cấu hình phím tắt
- ✅ Giao diện GUI đẹp mắt với PyQt5
- ✅ Giám sát phím tắt theo thời gian thực
- ✅ Tổ chức phím tắt theo danh mục

## 📋 Cấu Trúc Dự Án

```
windows-hotkey-manager/
├── main.py                 # Điểm vào chính của ứng dụng
├── requirements.txt        # Các dependencies Python
├── config.py              # Trình quản lý cấu hình (lưu/tải JSON)
├── models.py              # Mô hình dữ liệu Hotkey
├── hotkey_manager.py      # Phát hiện và thực thi phím tắt
├── ui/
│   ├── __init__.py        # Khởi tạo gói UI
│   ├── main_window.py     # Cửa sổ chính với danh sách phím tắt
│   ├── create_hotkey.py   # Dialog tạo phím tắt mới
│   └── styles.py          # Định dạng PyQt5
└── README.md              # Tệp này
```

## 🚀 Cài Đặt

### Yêu Cầu Hệ Thống
- Python 3.8 trở lên
- pip (Trình quản lý gói Python)

### Phương Pháp 1: Cài từ File ZIP (Dễ Nhất)

1. **Tải file ZIP**
   - Vào trang GitHub: https://github.com/Robertpham912/windows-hotkey-manager
   - Click nút **"Code"** → **"Download ZIP"**
   - Giải nén file ZIP vào thư mục bất kỳ

2. **Mở Command Prompt (CMD) hoặc PowerShell**
   ```bash
   cd C:\đường\dẫn\đến\windows-hotkey-manager
   ```

3. **Cài đặt các dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Chạy ứng dụng**
   ```bash
   python main.py
   ```

### Phương Pháp 2: Dùng Git (Nếu Có Git)

1. **Clone repository**
   ```bash
   git clone https://github.com/Robertpham912/windows-hotkey-manager.git
   cd windows-hotkey-manager
   ```

2. **Cài đặt các dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Chạy ứng dụng**
   ```bash
   python main.py
   ```

### Phương Pháp 3: Tạo Virtual Environment (Khuyến Nghị)

```bash
# Tạo virtual environment
python -m venv venv

# Kích hoạt (trên Windows)
venv\Scripts\activate

# Cài đặt dependencies
pip install -r requirements.txt

# Chạy ứng dụng
python main.py
```

## 🎮 Cách Sử Dụng

### Chạy ứng dụng
```bash
python main.py
```

### Tạo phím tắt mới
1. Click nút **"➕ Phím Tắt Mới"**
2. Nhập tên phím tắt (ví dụ: "Mở Spotify")
3. Chọn tổ hợp phím (modifiers + phím)
4. Chọn hành động hoặc ứng dụng
5. Click **"💾 Lưu Phím Tắt"**

### Quản lý phím tắt
- **Xem**: Tất cả phím tắt hiển thị trong danh sách chính
- **Sửa**: Chọn và click **"✏️ Sửa"**
- **Xóa**: Chọn và click **"🗑️ Xóa"**
- **Tìm kiếm**: Sử dụng thanh tìm kiếm để tìm phím tắt

## 📁 Cấu Hình

Phím tắt được lưu trong `hotkeys.json`:
```json
{
  "hotkeys": [
    {
      "name": "Mở Spotify",
      "keys": "Ctrl+Alt+S",
      "action": "spotify.exe"
    }
  ]
}
```

## 🔧 Phát Triển

### Mô Tả Các Tệp

- **main.py**: Khởi tạo ứng dụng PyQt5 và bắt đầu quản lý phím tắt
- **config.py**: Xử lý lưu trữ cấu hình dựa trên JSON
- **models.py**: Định nghĩa lớp dữ liệu `Hotkey`
- **hotkey_manager.py**: Giám sát đầu vào bàn phím toàn cục và kích hoạt các callback
- **ui/main_window.py**: UI chính với danh sách phím tắt, danh mục và các nút hành động
- **ui/create_hotkey.py**: Dialog tạo/sửa phím tắt
- **ui/styles.py**: Định nghĩa stylesheet PyQt5

### Công Nghệ Sử Dụng
- **PyQt5**: Framework giao diện
- **pynput**: Lắng nghe bàn phím toàn cục
- **JSON**: Lưu trữ cấu hình

## 📦 Dependencies

Xem `requirements.txt` để danh sách đầy đủ:
- PyQt5
- pynput

## 🐛 Khắc Phục Sự Cố

### Phím tắt không hoạt động?
- Đảm bảo ứng dụng có quyền cần thiết
- Thử chạy với quyền Administrator
- Kiểm tra `hotkeys.json` để xác nhận cú pháp

### Giao diện không hiển thị?
- Xác minh PyQt5 được cài đặt: `pip install PyQt5`
- Kiểm tra phiên bản Python (3.8+ yêu cầu)

### Python không được tìm thấy?
- Cài đặt Python từ: https://www.python.org/downloads/
- Đảm bảo chọn "Add Python to PATH" khi cài đặt
- Khởi động lại máy tính

## 💡 Mẹo & Thủ Thuật

1. **Chạy khi khởi động Windows**: Tạo shortcut trong thư mục Startup
2. **Quyền Admin**: Chạy CMD/PowerShell với quyền Administrator nếu gặp lỗi
3. **Ví dụ phím tắt**:
   - `Ctrl+Alt+N` - Mở Notepad
   - `Ctrl+Alt+C` - Mở Calculator
   - `Win+Shift+S` - Screenshot

## 📝 Giấy Phép

MIT License - Tự do sử dụng dự án này!

## 👨‍💻 Tác Giả

**Phạm Gia Phúc** (Robertpham912)

## 🤝 Đóng Góp

Chúng tôi chào đón các đóng góp! Bạn có thể:
- Báo cáo lỗi
- Đề xuất tính năng mới
- Gửi pull requests

---

Made with ❤️ cho các người dùng Windows
