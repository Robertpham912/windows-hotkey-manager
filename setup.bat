@echo off
chcp 65001 >nul
echo ==========================================
echo Windows Hotkey Manager - Setup
echo ==========================================
echo.
echo Đang cài đặt các dependencies...
echo.

pip install --default-timeout=1000 PyQt5 pynput

echo.
echo ==========================================
echo ✓ Cài đặt hoàn tất!
echo ==========================================
echo.
echo Bây giờ bạn có thể chạy: run.bat
echo.
pause
