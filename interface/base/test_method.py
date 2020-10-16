import unittest
import HtmlTestRunner
import datetime
from interface.utils.configEmail import mail
from interface.case.test_case import TestMethod

'''
    主文件，运行所有测试用例
'''
if __name__ == '__main__':
    # 测试用例实例化
    t_case = TestMethod()
    # 测试类实例化
    suite = unittest.TestSuite()
    suite.addTest(TestMethod("test_01"))
    suite.addTest(TestMethod("test_02"))
    # 根据断言结果生成html测试报告
    runner = HtmlTestRunner.HTMLTestRunner(report_title=f"{datetime.date.today()}test case")
    runner.run(suite)
    mail()
