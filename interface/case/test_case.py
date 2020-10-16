import json
import os
import unittest
import xlrd
from interface.utils.demo import RunMain


# 创建请求对象实例
run = RunMain()
# 打开html文档
excel_data = xlrd.open_workbook(os.path.dirname(__file__) + "\\" + "api.xlsx")
table = excel_data.sheets()[0]
# 行数
rows = table.nrows
# 列数
cols = table.ncols
index = 0


def handle_excel():
    if index <= rows:
        # 从excel中读取url，请求方法，请求参数，请求头
        url = table.row_values(index)[0]
        method = table.row_values(index)[1]
        data = json.loads(table.row_values(index)[2])
        headers = eval(table.row_values(index)[3])
        res = run.run_main(url, method, data, headers)
        res_json = res.json()
        # 先断言url返回的结果，一般为200才继续后面流程
        assert (res.status_code == 200)
        # 特征1必须有，判断特征1是否在返回的数据中
        if table.row_values(index)[4] != "":
            assert (table.row_values(index)[4] in json.dumps(res_json, ensure_ascii=False))
        # 特征2，3可以有，判断特征2,3是否在返回的数据中
        if table.row_values(index)[5] != "":
            assert (table.row_values(index)[5] in json.dumps(res_json, ensure_ascii=False))
        else:
            assert True
        if table.row_values(index)[6] != "":
            assert (table.row_values(index)[6] in json.dumps(res_json, ensure_ascii=False))
        else:
            assert True


class TestMethod(unittest.TestCase):
    # 每次调用excel处理的方法使index的值，也就是行数+1
    def test_01(self):
        global index
        index += 1
        handle_excel()

    def test_02(self):
        global index
        index += 1
        handle_excel()
