import handle_case
import time
import json
import threading

tokenId = ""
order_no = ""
order_id = ""
apply_id = ""


class utrailer_case(handle_case.Handle_Data):
    def set_data(self):
        # 从excel中读取url，请求方法，请求参数，请求头
        self.data = json.loads(self.table.row_values(self.index)[2])
        # 税筹修改订单时间
        self.change_order_time()
        # 取消订单单独判断
        if self.url.split("/")[-1] == "cancel" or "api/web/order/info" in self.url:
            self.get_order_id()
        # 车源申请详情id
        if "vm/vehicle/apply/detail" in self.url:
            self.apply_detail()
        return self.data

    def set_headers(self):
        self.headers = eval(self.table.row_values(self.index)[3])
        # 获取tokenId
        if "tokenId" in list(self.headers.keys()):
            self.get_tokenId()
        return self.headers

    # 税筹获取tokenId
    def get_tokenId(self):
        self.headers["tokenId"] = tokenId

    def assert_result(self):
        if self.method.upper() == "POST":
            res_json = self.res.json()
            # 先断言url返回的结果，一般为200才继续后面流程
            assert (self.res.status_code == 200)
            # 税筹接口特殊判断
            self.interface_callback()
            # 判断返回值的长度
            if self.table.row_values(self.index)[4] == 1:
                assert (len(res_json["body"]["data"]) > 0)
            # 特征1必须有，判断特征1是否在返回的数据中
            if self.table.row_values(self.index)[5] != "":
                assert (self.table.row_values(self.index)[5] in json.dumps(res_json, ensure_ascii=False))
            # 压力测试
            if self.table.row_values(self.index)[6] is not None:
                thread_pool = []
                for i in range(int(self.table.row_values(self.index)[6])):
                    thread = threading.Thread(target=self.get_response)
                    thread_pool.append(thread)
                for th in thread_pool:
                    th.start()
                for th in thread_pool:
                    threading.Thread.join(th)
            # 特征2，3可以有，判断特征2,3是否在返回的数据中
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

    # 税筹接口判断
    def interface_callback(self):
        res_json = self.res.json()
        if type(res_json["body"]) is dict:
            if "data" in list(res_json["body"].keys()):
                print(res_json["body"]["data"])
                number = list(res_json["body"]["data"][0].keys())
                if "orderNo" in number or "applyNo" in number:
                    if "id" in list(res_json["body"]["data"][0].keys()):
                        global order_id, apply_id
                        order_id = res_json["body"]["data"][0]["id"]
                        apply_id = res_json["body"]["data"][0]["id"]
                    else:
                        print(res_json)
                else:
                    print(res_json)
            else:
                print(res_json)
        else:
            print(res_json)
            if "data" not in list(res_json.keys()) and "body" in list(res_json.keys()):
                global order_no
                order_no = res_json["body"]
        if "login" in self.url and "admin" not in self.url:
            global tokenId
            tokenId = res_json["body"]["sessionId"]

    # 税筹修改订单时间
    def change_order_time(self):
        if "body" in list(self.data.keys()):
            if "expArriveTime" in list(self.data["body"].keys()) and "expDepartTime" in list(self.data["body"].keys()):
                self.data["body"]["expDepartTime"] = time.strftime("%Y-%m-%d %H:%M:%S",
                                                                   time.localtime(time.time() + 60 * 60))
                self.data["body"]["expArriveTime"] = time.strftime("%Y-%m-%d %H:%M:%S",
                                                                   time.localtime(time.time() + 60 * 60 * 5))
            if "loadTime" in list(self.data["body"].keys()) and "loadFinishTime" in list(self.data["body"].keys()):
                self.data["body"]["loadTime"] = time.strftime("%Y-%m-%d %H:%M:%S",
                                                              time.localtime(time.time() + 60 * 60))
                self.data["body"]["loadFinishTime"] = time.strftime("%Y-%m-%d %H:%M:%S",
                                                                    time.localtime(time.time() + 60 * 60))
                self.data["body"]["unLoadTime"] = time.strftime("%Y-%m-%d %H:%M:%S",
                                                                time.localtime(time.time() + 60 * 60 * 5))
                self.data["body"]["unLoadFinishTime"] = time.strftime("%Y-%m-%d %H:%M:%S",
                                                                      time.localtime(time.time() + 60 * 60 * 5))

    # 获取订单id
    def get_order_id(self):
        self.data["body"]["id"] = str(order_id)

    # 车源申请详情
    def apply_detail(self):
        self.data["body"]["id"] = str(apply_id)
