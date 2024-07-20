from infra.config_provider import ConfigProvider


class LoadConfig:
    @staticmethod
    def return_file():
        return ConfigProvider.load_from_file("../config.json")
