import logging
import unittest
import HtmlTestRunner
from interface.utils.configEmail import mail
from interface.utils.demo import RunMain


class TestMethod(unittest.TestCase):
    def setUp(self) -> None:
        self.run = RunMain()

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


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestMethod("test_01"))
    suite.addTest(TestMethod("test_02"))
    runner = HtmlTestRunner.HTMLTestRunner(report_title="this is test")
    runner.run(suite)
    mail()
