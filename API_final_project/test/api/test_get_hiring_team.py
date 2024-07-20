import unittest

from infra.api.api_wrapper import APIWrapper
from logic.utilities import LoadConfig
from logic.api.get_hiring_team import GetHiringTeam


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._api_request = APIWrapper()
        self.config = LoadConfig.return_file()

    def test_get_hiring_team(self):
        api_get_hiring_team = GetHiringTeam(self._api_request)
        result = api_get_hiring_team.get_hiring_team_api_get()
        body = result.json()
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["message"], self.config["get_hiring_team_message"])
        self.assertTrue(body["success"])


if __name__ == '__main__':
    unittest.main()
