from pynput import keyboard

class HotkeyManager:
    def __init__(self):
        self.hotkeys = {}
        self.listener = keyboard.Listener(on_press=self.on_press)

    def register_hotkey(self, key_combination, callback):
        if key_combination not in self.hotkeys:
            self.hotkeys[key_combination] = callback
            print(f"Registered hotkey: {key_combination}")

    def on_press(self, key):
        try:
            current_hotkey = keyboard.Key.fn + key
            if current_hotkey in self.hotkeys:
                self.hotkeys[current_hotkey]()
        except AttributeError:
            pass

    def start(self):
        self.listener.start()
        print("Hotkey manager started.")

    def stop(self):
        self.listener.stop()
        print("Hotkey manager stopped.")
