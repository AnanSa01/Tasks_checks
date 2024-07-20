from logic.utilities import LoadConfig


class BaseInit:
    def __init__(self, request):
        self._request = request
        self.config = LoadConfig.return_file()
