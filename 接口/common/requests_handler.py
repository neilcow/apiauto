import requests


class RequestHandler(object):
    def __init__(self):
        self.session = requests.Session()

    def visit(self, method, url, params=None, data=None, json=None, **kwargs):
        res = self.session.request(method=method, url=url, params=params, data=data, json=json, **kwargs)
        try:
            return res.json()
        except ValueError:
            print('not json')