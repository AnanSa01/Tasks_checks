import requests


class APIWrapper:

    def __init__(self):
        self._request = None

    def get_request(self, url, headers=None, body=None):
        return requests.get(url, headers=headers, json=body)

    def post_request(self, url, headers=None, body=None):
        return requests.post(url, headers=headers, json=body)
