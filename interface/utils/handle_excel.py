import xlrd
import os


class Excel(object):
    def __init__(self):
        self.data = xlrd.open_workbook(os.path.dirname(__file__) + "\\" + "api.xlsx")
        self.data_list = []

    def handle(self):
        table = self.data.sheets()[0]
        rows = table.nrows
        cols = table.ncols
        for i in range(1, rows):
            content = table.row_values(i)
            self.data_list.append(content)
        return self.data_list


if __name__ == '__main__':
    Excel().handle()
