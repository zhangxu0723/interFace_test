import os


class get_htmlPath(object):
    # 获取当前工作目录
    @staticmethod
    def get_path():
        return os.getcwd() + "\\reports"

    def html_list(self):
        # 获取生成html地址，删除旧的html文件
        dir_list = os.listdir(self.get_path())
        dir_list.sort(key=lambda x: os.path.getmtime(self.get_path() + '\\' + x))
        for i in dir_list[:-1]:
            os.remove(self.get_path() + "\\" + i)
        return dir_list[-1]
