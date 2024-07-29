import json


class ConfigProvider:
    """
    this function is to load the config from the json file and to use it
    """

    @staticmethod
    def load_from_file(filename):
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty library.")
