import os
import time
import unittest
import HtmlTestRunner
import datetime
from interface.utils.configEmail import mail
from interface.case.test_case import TestMethod
from interface.utils.HTMLTestRunner import HTMLTestRunner

path = os.path.abspath(os.path.dirname(os.getcwd()) + "\\" + "template" + "\\" + "report_template.html")
title = f"{datetime.date.today()}test case"
now_time = (time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
testcase_dir = os.getcwd() + f"\\reports\\{now_time}_result.html"

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
    suite.addTest(TestMethod("test_03"))
    # 根据断言结果生成html测试报告
    # runner = HtmlTestRunner.HTMLTestRunner(report_title=title, template=path)
    # runner.run(suite)
    with open(testcase_dir, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title='接口自动化测试报告', description='Test for Test')
        runner.run(suite)
    # mail()
