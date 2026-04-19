class Hotkey:
    def __init__(self, name, keys, action):
        self.name = name  # Name of the hotkey
        self.keys = keys  # Keys associated with the hotkey
        self.action = action  # Action to be performed

    def __repr__(self):
        return f"Hotkey(name={self.name}, keys={self.keys}, action={self.action})"