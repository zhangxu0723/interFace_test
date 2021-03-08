from interface.utils.getHtmlPath import get_htmlPath
import pytest
from interface.case.extend_file import utrailer_case
import os
import allure

index = 0


@allure.feature("登录功能")
class Test_Server_Login(object):
    # 每次调用excel处理的方法使index的值，也就是行数+1
    @allure.story("登录功能")
    def test_login(self):
        global index
        index += 1
        print(index)
        data = utrailer_case(index)
        data.get_response()
        data.assert_result()

    @allure.story("税筹首页信息")
    def test_homePage(self):
        global index
        index += 1
        print(index)
        data = utrailer_case(index)
        data.get_response()
        data.assert_result()

    @allure.story("找车首页信息")
    def test_stat(self):
        global index
        index += 1
        print(index)
        data = utrailer_case(index)
        data.get_response()
        data.assert_result()


@allure.feature("税筹订单功能")
class Test_Server_Order(object):
    @allure.story("税筹建单")
    def test_order_save(self):
        global index
        index += 1
        print(index)
        data = utrailer_case(index)
        data.get_response()
        data.assert_result()

    @allure.story("税筹订单列表")
    def test_order_list(self):
        global index
        index += 1
        print(index)
        data = utrailer_case(index)
        data.get_response()
        data.assert_result()

    @allure.story("税筹订单详情")
    def test_order_info(self):
        global index
        index += 1
        print(index)
        data = utrailer_case(index)
        data.get_response()
        data.assert_result()

    @allure.story("税筹订单取消")
    def test_order_cancel(self):
        global index
        index += 1
        print(index)
        data = utrailer_case(index)
        data.get_response()
        data.assert_result()


'''
@allure.feature("找车订单功能")
class Test_Server_vmOrder(object):
    @allure.story("找车订单建单")
    def test_vm_order_save(self):
        global index
        index += 1
        print(index)
        data = Handle_Data(index)
        data.request_data()
        data.handle_excel()

    @allure.story("找车订单列表")
    def test_vm_order_list(self):
        global index
        index += 1
        print(index)
        data = Handle_Data(index)
        data.request_data()
        data.handle_excel()

    @allure.story("找车订单详情")
    def test_vm_order_info(self):
        global index
        index += 1
        print(index)
        data = Handle_Data(index)
        data.request_data()
        data.handle_excel()

    @allure.story("找车订单取消")
    def test_vm_order_cancel(self):
        global index
        index += 1
        print(index)
        data = Handle_Data(index)
        data.request_data()
        data.handle_excel()


@allure.feature("运力池功能")
class Test_Server_Manager(object):
    @allure.story("司机列表")
    def test_driver_list(self):
        global index
        index += 1
        print(index)
        data = Handle_Data(index)
        data.request_data()
        data.handle_excel()

    @allure.story("司机详情")
    def test_driver_detail(self):
        global index
        index += 1
        print(index)
        data = Handle_Data(index)
        data.request_data()
        data.handle_excel()

    @allure.story("车辆列表")
    def test_vehicle_list(self):
        global index
        index += 1
        print(index)
        data = Handle_Data(index)
        data.request_data()
        data.handle_excel()

    @allure.story("车辆详情")
    def test_vehicle_detail(self):
        global index
        index += 1
        print(index)
        data = Handle_Data(index)
        data.request_data()
        data.handle_excel()

    @allure.story("普通查询地址列表")
    def test_normal_address_list(self):
        global index
        index += 1
        print(index)
        data = Handle_Data(index)
        data.request_data()
        data.handle_excel()

    @allure.story("曾用车普通查询")
    def test_normal_vehicle_used_query(self):
        global index
        index += 1
        print(index)
        data = Handle_Data(index)
        data.request_data()
        data.handle_excel()

    @allure.story("运力池普通查询")
    def test_normal_vehicle_platform_query(self):
        global index
        index += 1
        print(index)
        data = Handle_Data(index)
        data.request_data()
        data.handle_excel()

    @allure.story("曾用车高级查询")
    def test_high_vehicle_used_query(self):
        global index
        index += 1
        print(index)
        data = Handle_Data(index)
        data.request_data()
        data.handle_excel()

    @allure.story("运力池高级查询")
    def test_high_vehicle_platform_query(self):
        global index
        index += 1
        print(index)
        data = Handle_Data(index)
        data.request_data()
        data.handle_excel()

    @allure.story("车源申请列表")
    def test_vehicle_apply_list(self):
        global index
        index += 1
        print(index)
        data = Handle_Data(index)
        data.request_data()
        data.handle_excel()

    @allure.story("车源申请详情")
    def test_vehicle_apply_detail(self):
        global index
        index += 1
        print(index)
        data = Handle_Data(index)
        data.request_data()
        data.handle_excel()

    @allure.story("收款人列表")
    def test_payee_info_list(self):
        global index
        index += 1
        print(index)
        data = Handle_Data(index)
        data.request_data()
        data.handle_excel()

    @allure.story("收款人详情")
    def test_payee_info_detail(self):
        global index
        index += 1
        print(index)
        data = Handle_Data(index)
        data.request_data()
        data.handle_excel()


@allure.feature("支付功能")
class Test_Server_Payment(object):
    @allure.story("支付申请")
    def test_payment_apply_list(self):
        global index
        index += 1
        print(index)
        data = Handle_Data(index)
        data.request_data()
        data.handle_excel()

    @allure.story("支付审核")
    def test_payment_audit_list(self):
        global index
        index += 1
        print(index)
        data = Handle_Data(index)
        data.request_data()
        data.handle_excel()

    @allure.story("支付列表")
    def test_payment_pay_list(self):
        global index
        index += 1
        print(index)
        data = Handle_Data(index)
        data.request_data()
        data.handle_excel()

    @allure.story("支付记录")
    def test_payment_log_list(self):
        global index
        index += 1
        print(index)
        data = Handle_Data(index)
        data.request_data()
        data.handle_excel()


@allure.feature("开票功能")
class Test_Server_Invoice(object):
    @allure.story("开票申请")
    def test_invoice_order_list(self):
        global index
        index += 1
        print(index)
        data = Handle_Data(index)
        data.request_data()
        data.handle_excel()

    @allure.story("开票记录")
    def test_invoice_log_list(self):
        global index
        index += 1
        print(index)
        data = Handle_Data(index)
        data.request_data()
        data.handle_excel()

    @allure.story("发票地址管理")
    def test_invoice_address_list(self):
        global index
        index += 1
        print(index)
        data = Handle_Data(index)
        data.request_data()
        data.handle_excel()

    @allure.story("邮寄地址管理")
    def test_invoice_send_list(self):
        global index
        index += 1
        print(index)
        data = Handle_Data(index)
        data.request_data()
        data.handle_excel()

    @allure.story("企业钱包")
    def test_payment_trade_list(self):
        global index
        index += 1
        print(index)
        data = Handle_Data(index)
        data.request_data()
        data.handle_excel()

    @allure.story("剩余金额")
    def test_payment_account(self):
        global index
        index += 1
        print(index)
        data = Handle_Data(index)
        data.request_data()
        data.handle_excel()

    @allure.story("返利金额")
    def test_rebate_list(self):
        global index
        index += 1
        print(index)
        data = Handle_Data(index)
        data.request_data()
        data.handle_excel()


@allure.feature("地址功能")
class Test_Server_Address(object):
    @allure.story("地址管理")
    def test_address_list(self):
        global index
        index += 1
        print(index)
        data = Handle_Data(index)
        data.request_data()
        data.handle_excel()
'''

if __name__ == '__main__':
    get_htmlPath().remove_trash()
    pytest.main(['--alluredir', './result'])
    os.system('allure generate ./result -o ./report --clean')
