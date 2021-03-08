import os
import xlrd
from interface.utils.demo import RunMain
import abc
import threading
import json


class Handle_Data(metaclass=abc.ABCMeta):
    def __init__(self, index):
        # 创建请求对象实例
        self.run = RunMain()
        # 打开excel文档
        self.excel_data = xlrd.open_workbook(os.path.dirname(__file__) + "\\" + "api.xlsx")
        self.table = self.excel_data.sheets()[0]
        self.index = index
        self.url = self.table.row_values(index)[0]
        self.method = self.table.row_values(index)[1]
        self.res_json = ""
        # 行数
        self.rows = self.table.nrows
        # 列数
        self.cols = self.table.ncols
        self.res = ""
        self.data = ""
        self.headers = ""

    def set_data(self):
        self.data = json.loads(self.table.row_values(self.index)[2])
        return self.data

    def set_headers(self):
        self.headers = eval(self.table.row_values(self.index)[3])
        return self.headers

    @abc.abstractmethod
    def get_tokenId(self):
        pass

    def get_response(self):
        self.res = self.run.run_main(self.url, self.method, self.set_data(), self.set_headers())
        print(f"接口请求耗时:{self.res.elapsed.total_seconds()}秒")

    def assert_result(self):
        if self.method.upper() == "POST":
            res_json = self.res.json()
            # 先断言url返回的结果，一般为200才继续后面流程
            assert (self.res.status_code == 200)
            # 判断返回值的长度
            if self.table.row_values(self.index)[4] == 1:
                assert (len(res_json["body"]["data"]) > 0)
            if self.table.row_values(self.index)[5] != "":
                assert (self.table.row_values(self.index)[5] in json.dumps(res_json, ensure_ascii=False))
            # 多线程压力测试，excel中第7列数字是多少，并发多少次
            if self.table.row_values(self.index)[6] is not None:
                thread_pool = []
                for i in range(int(self.table.row_values(self.index)[6])):
                    th = threading.Thread(target=self.get_response)
                    thread_pool.append(th)
                for th in thread_pool:
                    th.start()
                for th in thread_pool:
                    threading.Thread.join(th)
            if self.table.row_values(self.index)[7] != "":
                assert (self.table.row_values(self.index)[7] in json.dumps(res_json, ensure_ascii=False))
            else:
                assert True
            if self.table.row_values(self.index)[8] != "":
                assert (self.table.row_values(self.index)[8] in json.dumps(res_json, ensure_ascii=False))
            else:
                assert True
        # get请求只判断返回的code
        elif self.method.upper() == "GET":
            assert (self.res.status_code == 200)
        else:
            assert False
