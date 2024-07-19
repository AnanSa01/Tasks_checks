from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class GetJobDetails:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_from_file("../../config.json")

    def find_job_details_api_get(self):
        return self._request.get_request(f"{self.config["base_url"]}/get-job-details?{self.config["get_job_details_function"]}",self.config["header"])