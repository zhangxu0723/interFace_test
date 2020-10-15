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

    def test_03(self):
        url = "https://test-ebs.utrailer.cn/api/web/order/list"
        method = "post"
        data = {"head": {"sequenceCode": "60472556-97f3-4229-51e1-6050535a07f3", "callType": "H5",
                         "protocolVersion": "2.0", "appVersion": "2.0.0", "systemVersion": "11.2.2", "bizId": "7",
                         "requestTime": 1602752911000, "mobileModel": "iPhone"},
                "body": {"pageSize": 30, "pageNum": 1, "sortField": "", "sortOrder": "", "status": "ALL"},
                "sign": "25991ba0237dc398cfa24e55201380ef"}
        headers = {
            "tokenid": "40e19653-ed79-4283-86d0-dda06654b3ac",
            "content-type": "text/plain"
        }
        res = self.run.run_main(url, method, data, headers)
        logging.fatal(res)
        assert (res["head"]["errorMessage"] == "操作成功")
