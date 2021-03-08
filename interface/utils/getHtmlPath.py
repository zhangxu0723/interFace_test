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

    @staticmethod
    def remove_trash():
        trash = os.listdir(os.getcwd())
        if "result" in trash:
            del_list = os.listdir(os.getcwd() + "\\" + "result")
            for i in del_list:
                os.remove(os.getcwd() + "\\" + "result" + "\\" + i)
        else:
            return None


if __name__ == '__main__':
    print(get_htmlPath().remove_trash())
