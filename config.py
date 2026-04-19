import json

class ConfigManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def save_config(self, data):
        with open(self.file_path, 'w') as json_file:
            json.dump(data, json_file)

    def load_config(self):
        try:
            with open(self.file_path, 'r') as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}