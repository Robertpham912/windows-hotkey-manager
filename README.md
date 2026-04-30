# ⌨️ Windows Hotkey Manager

A powerful Windows hotkey manager to create custom keyboard shortcuts for launching applications and executing actions.

## 🎯 Features

- ✅ Create custom hotkeys with any key combination (Ctrl, Shift, Alt, Win)
- ✅ Launch applications with custom shortcuts
- ✅ Execute system commands and actions
- ✅ Save and load hotkey configurations
- ✅ Beautiful PyQt5 GUI interface
- ✅ Real-time hotkey monitoring
- ✅ Category-based hotkey organization

## 📋 Project Structure

```
windows-hotkey-manager/
├── main.py                 # Main application entry point
├── requirements.txt        # Python dependencies
├── config.py              # Configuration manager (save/load JSON)
├── models.py              # Hotkey data model
├── hotkey_manager.py      # Hotkey detection and execution
├── ui/
│   ├── __init__.py        # UI package initialization
│   ├── main_window.py     # Main window with hotkey list
│   ├── create_hotkey.py   # Dialog for creating new hotkeys
│   └── styles.py          # PyQt5 styling
└── README.md              # This file
```

## 🚀 Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Robertpham912/windows-hotkey-manager.git
   cd windows-hotkey-manager
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   # or
   source venv/bin/activate      # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Usage

### Run the application
```bash
python main.py
```

### Create a hotkey
1. Click **"➕ New Hotkey"** button
2. Enter hotkey name (e.g., "Open Spotify")
3. Select key combination (modifiers + key)
4. Choose action or application
5. Click **"💾 Save Hotkey"**

### Manage hotkeys
- **View**: All hotkeys appear in the main list
- **Edit**: Select and click **"✏️ Edit"**
- **Delete**: Select and click **"🗑️ Delete"**
- **Search**: Use the search bar to find hotkeys

## 📁 Configuration

Hotkeys are saved in `hotkeys.json`:
```json
{
  "hotkeys": [
    {
      "name": "Open Spotify",
      "keys": "Ctrl+Alt+S",
      "action": "spotify.exe"
    }
  ]
}
```

## 🔧 Development

### File Descriptions

- **main.py**: Initializes the PyQt5 application and starts the hotkey manager
- **config.py**: Handles JSON-based configuration storage
- **models.py**: Defines the `Hotkey` data class
- **hotkey_manager.py**: Monitors global keyboard input and triggers callbacks
- **ui/main_window.py**: Main UI with hotkey list, categories, and action buttons
- **ui/create_hotkey.py**: Dialog for creating/editing hotkeys
- **ui/styles.py**: PyQt5 stylesheet definitions

### Technologies Used
- **PyQt5**: GUI framework
- **pynput**: Global keyboard listener
- **JSON**: Configuration storage

## 📦 Dependencies

See `requirements.txt` for complete list:
- PyQt5
- pynput

## 🐛 Troubleshooting

### Hotkeys not working?
- Ensure the application has necessary permissions
- Try running as administrator
- Check `hotkeys.json` for correct syntax

### GUI not displaying?
- Verify PyQt5 is installed: `pip install PyQt5`
- Check Python version (3.8+ required)

## 📝 License

MIT License - feel free to use this project!

## 👨‍💻 Author

**Phạm Gia Phúc** (Robertpham912)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

---

Made with ❤️ for Windows users
