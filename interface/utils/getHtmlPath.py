import os


class get_htmlPath(object):
    @staticmethod
    def get_path():
        return os.getcwd() + "\\reports"

    def html_list(self):
        dir_list = os.listdir(self.get_path())
        dir_list.sort(key=lambda x: os.path.getmtime(self.get_path() + '\\' + x))
        for i in dir_list[:-1]:
            os.remove(self.get_path() + "\\" + i)
        return dir_list[-1]


if __name__ == '__main__':
    print(get_htmlPath().html_list())
