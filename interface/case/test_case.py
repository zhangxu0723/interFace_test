import logging
import unittest
from interface.utils.demo import RunMain
from interface.utils.handle_excel import Excel


class TestMethod(unittest.TestCase):
    def setUp(self) -> None:
        self.run = RunMain()
        self.excel = Excel()

    def test_01(self):
        url = "https://tsapi.amap.com/v1/track/service/add"
        method = "post"
        data = {
            "key": "d152f8a6692d46b7ce09c21b1f583f65",
            "name": "test03"
        }
        res = self.run.run_main(url, method, data)
        logging.fatal(res)
        assert (res["errcode"] == 10000)

    def test_02(self):
        url = "https://tsapi.amap.com/v1/track/service/add"
        method = "delete"
        data = {
            "key": "d152f8a6692d46b7ce09c21b1f583f65",
            "name": "test06"
        }
        res = self.run.run_main(url, method, data)
        logging.fatal(res)
        assert (res["errcode"] == 20009)
