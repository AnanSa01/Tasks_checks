from logic.api._base_init import BaseInit


class SearchEmployees(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def search_employees_api_get(self):
        return self._request.get_request(
            f"{self.config["base_url"]}/search-employees?{self.config["search_employees_function"]}",
            self.config["header"])
