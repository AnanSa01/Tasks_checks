import requests


class APIWrapper:

    def __init__(self):
        self._request = None

    def get_request(self, url, body=None):
        return requests.get(url, json=body)

    def post_request(self, url, body=None):
        return requests.post(url, data=body)
