import json
import os
import unittest
import xlrd
from interface.utils.demo import RunMain

index = 0


class Handle_Data(object):
    def __init__(self):
        # 创建请求对象实例
        self.run = RunMain()
        # 打开excel文档
        self.excel_data = xlrd.open_workbook(os.path.dirname(__file__) + "\\" + "api.xlsx")
        self.table = self.excel_data.sheets()[0]
        # 行数
        self.rows = self.table.nrows
        # 列数
        self.cols = self.table.ncols
        self.url = self.table.row_values(index)[0]
        self.method = self.table.row_values(index)[1]
        self.res = ""

    def request_data(self):
        if index <= self.rows:
            # 从excel中读取url，请求方法，请求参数，请求头
            if self.table.row_values(index)[2] == "None" or "":
                data = None
            else:
                data = json.loads(self.table.row_values(index)[2])
            if self.table.row_values(index)[3] == "None" or "":
                headers = None
            else:
                headers = eval(self.table.row_values(index)[3])
            self.res = self.run.run_main(self.url, self.method, data, headers)
            print(f"接口请求耗时:{self.res.elapsed.total_seconds()}秒")

    def handle_excel(self):

        # if self.table.row_values(index)[2] == "0":

        if self.method.upper() == "POST":
            res_json = self.res.json()
            try:
                # 先断言url返回的结果，一般为200才继续后面流程
                assert (self.res.status_code == 200)
                # 特征1必须有，判断特征1是否在返回的数据中
                if self.table.row_values(index)[5] != "":
                    assert (self.table.row_values(index)[5] in json.dumps(res_json, ensure_ascii=False))
                # 特征2，3可以有，判断特征2,3是否在返回的数据中
                if self.table.row_values(index)[6] != "":
                    assert (self.table.row_values(index)[6] in json.dumps(res_json, ensure_ascii=False))
                else:
                    assert True
                if self.table.row_values(index)[7] != "":
                    assert (self.table.row_values(index)[7] in json.dumps(res_json, ensure_ascii=False))
                else:
                    assert True
            except Exception as e:
                print(e)
        # get请求只判断返回的code
        elif self.method.upper() == "GET":
            assert (self.res.status_code == 200)


class TestMethod(unittest.TestCase):
    # 每次调用excel处理的方法使index的值，也就是行数+1
    def test_01(self):
        global index
        index += 1
        data = Handle_Data()
        data.request_data()
        data.handle_excel()

    def test_02(self):
        global index
        index += 1
        data = Handle_Data()
        data.request_data()
        data.handle_excel()

    def test_03(self):
        global index
        index += 1
        data = Handle_Data()
        data.request_data()
        data.handle_excel()


if __name__ == '__main__':
    TestMethod().test_01()
    TestMethod().test_02()
    TestMethod().test_03()
