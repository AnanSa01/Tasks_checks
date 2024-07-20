from logic.api._base_init import BaseInit


class HealthCheck(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def health_check_api_get(self):
        return self._request.get_request(f"{self.config["base_url"]}/health", self.config["header"])

    def return_data_in_health_check(self, body_of_health_check):
        return body_of_health_check["data"]
