import unittest

from infra.api.api_wrapper import APIWrapper
from logic.api.about_this_profile_NS import AboutThisProfile


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._api_request = APIWrapper()

    def test_about_this_profile(self):
        api_about_this_profile = AboutThisProfile(self._api_request)
        result = api_about_this_profile.about_this_profile()
        body = result.json()
        print(body)
        # data = body["data"]  it changes everytime
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["message"], "")

if __name__ == '__main__':
    unittest.main()
