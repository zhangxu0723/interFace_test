import json
import logging
import os
import unittest
import xlrd
from interface.utils.demo import RunMain


run = RunMain()
excel_data = xlrd.open_workbook(os.path.dirname(__file__) + "\\" + "api.xlsx")
table = excel_data.sheets()[0]
rows = table.nrows
cols = table.ncols
index = 0


def handle_excel():
    if index <= rows:
        url = table.row_values(index)[0]
        method = table.row_values(index)[1]
        data = json.loads(table.row_values(index)[2])
        headers = eval(table.row_values(index)[3])
        res = run.run_main(url, method, data, headers)
        res_json = res.json()
        assert (res.status_code == 200)
        if table.row_values(index)[4] != "":
            assert (table.row_values(index)[4] in json.dumps(res_json, ensure_ascii=False))
        if table.row_values(index)[5] != "":
            assert (table.row_values(index)[5] in json.dumps(res_json, ensure_ascii=False))
        else:
            assert True
        if table.row_values(index)[6] != "":
            assert (table.row_values(index)[6] in json.dumps(res_json, ensure_ascii=False))
        else:
            assert True


class TestMethod(unittest.TestCase):
    def test_01(self):
        global index
        index += 1
        handle_excel()

    def test_02(self):
        global index
        index += 1
        handle_excel()
