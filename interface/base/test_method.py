import unittest
import HtmlTestRunner
import datetime
from interface.utils.configEmail import mail
from interface.case.test_case import TestMethod


if __name__ == '__main__':
    t_case = TestMethod()
    suite = unittest.TestSuite()
    suite.addTest(TestMethod("test_01"))
    suite.addTest(TestMethod("test_02"))
    suite.addTest(TestMethod("test_03"))
    runner = HtmlTestRunner.HTMLTestRunner(report_title=f"{datetime.date.today()}test case")
    runner.run(suite)
    mail()
