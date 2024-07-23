from infra.config_provider import ConfigProvider


class LoadConfig:
    """
    this function to load the json file in a fast and efficient way
    """
    @staticmethod
    def return_file():
        return ConfigProvider.load_from_file("../config.json")
