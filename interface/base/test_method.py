import logging
import unittest
import HtmlTestRunner
from interface.configEmail import SendEmail
from interface.demo import RunMain


class TestMethod(unittest.TestCase):
    def setUp(self) -> None:
        self.run = RunMain()

    def test_01(self):
        url = "https://tsapi.amap.com/v1/track/service/add"
        method = "POST"
        data = {
            "key": "d152f8a6692d46b7ce09c21b1f583f65",
            "name": "test03"
        }
        res = self.run.run_main(url, method, data)
        self.assertTrue(res["errcode"] == 10000)

    def test_02(self):
        url = "https://tsapi.amap.com/v1/track/service/add"
        method = "POST"
        data = {
            "key": "d152f8a6692d46b7ce09c21b1f583f65",
            "name": "test02"
        }
        res = self.run.run_main(url, method, data)
        self.assertTrue(res["errcode"] == 10000)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestMethod("test_01"))
    suite.addTest(TestMethod("test_02"))
    runner = HtmlTestRunner.HTMLTestRunner(report_title="this is test")
    runner.run(suite)
    m = SendEmail(
        username='18001098773@163.com',
        passwd='FEHRWZTRHUDPIWZM',
        recv=['zhangxu01@sinoiov.com'],
        title='测试报告',
        content='发送邮件',
        file=r'reports/TestResults___main__.TestMethod_2020-10-13_23-18-36.html',
        ssl=True,
    )
    m.send_email()
    # unittest.main()
