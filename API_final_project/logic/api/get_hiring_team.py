from logic.api._base_init import BaseInit


class GetHiringTeam(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def get_hiring_team_api_get(self):
        return self._request.get_request(
            f"{self.config["base_url"]}/get-hiring-team?{self.config["get_hiring_team_function"]}",
            self.config["header"])
