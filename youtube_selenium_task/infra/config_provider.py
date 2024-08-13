import json


class ConfigProvider:

    @staticmethod
    def load_from_file(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty library.")
