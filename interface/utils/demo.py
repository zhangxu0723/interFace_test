import requests


class RunMain(object):
    @staticmethod
    def send_get(url, data, headers):
        res = requests.get(url=url, data=data, headers=headers).json()
        return res

    @staticmethod
    def send_post(url, data, headers):
        res = requests.post(url=url, data=data, headers=headers).json()
        return res

    def run_main(self, url, method, data=None, headers=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data, headers)
        elif method == 'POST':
            res = self.send_post(url, data, headers)
        return res
