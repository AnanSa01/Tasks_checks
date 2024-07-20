import requests


class APIWrapper:
    """
    using "requests" package to use API data in many functions
    """

    def __init__(self):
        self._request = None

    @staticmethod
    def get_request(url, headers=None, body=None):
        return requests.get(url, headers=headers, json=body)

    @staticmethod
    def post_request(url, headers=None, body=None):
        return requests.post(url, headers=headers, json=body)

    @staticmethod
    def put_request(url, headers=None, body=None):
        return requests.put(url, headers=headers, json=body)

    @staticmethod
    def delete_request(url, headers=None, body=None):
        return requests.delete(url, headers=headers, json=body)
