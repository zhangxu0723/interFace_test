import json

import requests


class RunMain(object):
    @staticmethod
    def send_get(url, data, headers):
        res = requests.get(url=url, data=json.dumps(data), headers=headers)
        return res

    @staticmethod
    def send_post(url, data, headers):
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        return res

    def run_main(self, url, method, data=None, headers=None):
        res = None
        if method.upper() == 'GET':
            res = self.send_get(url, data, headers)
        elif method.upper() == 'POST':
            res = self.send_post(url, data, headers)
        else:
            return None
        return res
