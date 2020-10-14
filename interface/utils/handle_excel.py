import xlrd
import os


class Excel(object):
    def __init__(self):
        self.data = xlrd.open_workbook(os.path.dirname(__file__) + "\\" + "api.xlsx")

    def handle(self):
        table = self.data.sheets()[0]
        rows = table.nrows
        for i in range(1, rows):
            data = table.row_values(i)
            print(data)


if __name__ == '__main__':
    Excel().handle()
