import logging
import unittest
import HtmlTestRunner
from interface.utils.getHtmlPath import get_htmlPath
from interface.utils.configEmail import SendEmail
from interface.utils.demo import RunMain


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
        logging.fatal(res)
        assert (res["errcode"] == 10000)

    def test_02(self):
        url = "https://tsapi.amap.com/v1/track/service/add"
        method = "POST"
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
    new_html = get_htmlPath()
    htmlPath = new_html.html_list()
    m = SendEmail(
        username='18001098773@163.com',
        passwd='FEHRWZTRHUDPIWZM',
        recv=['zhangxu01@sinoiov.com'],
        title='测试报告',
        content='发送邮件',
        file=f'reports//{htmlPath}',
        ssl=True,
    )
    # m.send_email()
    # unittest.main()
