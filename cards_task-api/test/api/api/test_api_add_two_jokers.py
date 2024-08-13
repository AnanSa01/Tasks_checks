import unittest
from infra.both.config_provider import ConfigProvider
from infra.api.api_wrapper import APIWrapper
from logic.api.api_add_two_jokers import APIAddTwoJokers


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.api_request = APIWrapper()

    def test_add_two_jokers(self):
        """
        this function tests adding two card of jokers if the user enables it
        """
        api_add_two_jokers = APIAddTwoJokers(self.api_request)
        self.config = ConfigProvider.load_from_file('../../config.json')
        data = self.config['add_jokers']
        result = api_add_two_jokers.api_post_add_two_jokers(data)

        print(result.body)


if __name__ == '__main__':
    unittest.main()
