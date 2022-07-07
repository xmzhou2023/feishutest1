from project.DCR.page_object.menu import MenuPage
from project.DCR.page_object.SalesManagement_SalesOrder import SalesOrderPage
from project.DCR.page_object.login import LoginPage
from public.base.basics import Base
from public.base.assert_ui import ValueAssert
from libs.common.connect_sql import *
from libs.common.time_ui import sleep
import pytest
import allure


@allure.feature("销售管理-销售单")
class TestAddSubSalesOrder():
    @allure.story("新增")
    @allure.title("销售单页面，新增二代销售单操作")
    @allure.description("销售单页面，新增销售单操作成功后，校验新增的销售单是否存在")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_001(self, drivers):
        """DCR 二代账号登录"""
        user = LoginPage(drivers)
        user.dcr_login(drivers, "BD291501", "dcr123456")
        sleep(5)
        """销售管理菜单-出库单-筛选出库单用例"""
        menu = MenuPage(drivers)
        menu.click_gotomenu("Sales Management", "Sales Order")
        sleep(5)
        """销售订单页面，新建销售单、直接出库、筛选、然后快速收货场景功能"""
        """调用新增销售单用例"""
        add_sales = SalesOrderPage(drivers)
        add_sales.click_add_sales()
        add_sales.input_sales_buyer("EG000562")
        add_sales.input_sales_brand('TECNO')
        add_sales.input_sales_product("SPARK 6 Go 64+4 AQUA BLUE")
        add_sales.input_sales_quantity('1')
        add_sales.click_submit()
        sleep(1)
        add_sales.click_submit_OK()
        sleep(3)
        """二代用户，查询数据库最近新建的销售单ID"""
        user = SQL('DCR', 'test')
        sql = "select order_code,status from t_channel_sale_ticket where warehouse_id = '62134' and seller_id = '1596874516539662' and buyer_id = '1596874516539668' and status = 0 order by created_time desc limit 1"
        result = user.query_db(sql)
        order = result[0].get("order_code")
        status = result[0].get("status")
        if status == 0:
            sales_status = "Pending"
        """销售单页面，按销售单ID筛选销售单信息"""
        add_sales.input_sales_order_ID(order)
        add_sales.click_search()
        sleep(2)
        """获取列表，销售单ID与Status文本内容"""
        get_sales_order = add_sales.get_text_sales_id()
        get_status = add_sales.get_text_sales_status1()
        """调用断言方法，判断数据库表中查询的销售单ID，与列表获取的销售单ID文本匹配是否一致"""
        ValueAssert.value_assert_equal(get_sales_order, order)
        ValueAssert.value_assert_equal(get_status, sales_status)
        sleep(1)


@allure.feature("销售管理-销售单")
class TestDeliverySubSalesOrder():
    @allure.story("新增")
    @allure.title("销售单页面，对新增的销售单进行出库操作")
    @allure.description("销售单页面，对新增的销售单进行出库操作成功后，校验销售单对应的状态是否更新为：Delivered")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_002_001(self, drivers):
        """刷新页面"""
        base = Base(drivers)
        base.refresh()
        sleep(3.5)
        """打开Report Analysis->IMEI Inventory Query菜单"""
        menu = MenuPage(drivers)
        menu.click_gotomenu("Report Analysis", "IMEI Inventory Query")

        """调用菜单栏，打开IMEI Inventory Query菜单，获取product对应的IMEI"""
        delivery = SalesOrderPage(drivers)
        """查询IMEI Inventory Query页面 指定product的IMEI"""
        delivery.click_unfold()
        sleep(2)
        delivery.input_material_id("11001120")
        delivery.click_inventory_search()
        imei = delivery.get_text_imei_inventory()

        """ 刷新页面 """
        base.refresh()
        menu.click_gotomenu("Sales Management", "Sales Order")
        sleep(5)

        """二代用户，查询数据库最近新建的销售单ID"""
        user = SQL('DCR', 'test')
        sql = "select order_code,status from t_channel_sale_ticket where warehouse_id = '62134' and seller_id = '1596874516539662' and buyer_id = '1596874516539668' and status = 0 order by created_time desc limit 1"
        result = user.query_db(sql)
        order = result[0].get("order_code")
        # status = result[0].get("status")
        # if status == 80200000:
        #     sales_status = "Delivered"
        """销售单页面，按销售单ID筛选销售单信息"""
        delivery.input_sales_order_ID(order)
        delivery.click_search()
        sleep(2)
        """勾选新建的销售单，直接出库操作"""
        delivery.click_checkbox_orderID()
        delivery.click_Delivery_button()
        sleep(3)
        delivery.input_Payment_Mode('Wechat')
        sleep(1)
        delivery.input_imei(imei)
        delivery.click_check()
        delivery.click_submit_delivery()
        """销售单页面，按销售单ID筛选销售单信息，断言该条销售单对应的状态是否更新为：Delivered状态"""
        text_sales_order = delivery.get_text_sales_id()
        delivery.input_sales_order_ID(text_sales_order)
        delivery.click_search()
        sleep(2)
        text_status = delivery.get_text_sales_status2()
        """出库操作成功后，验证该条销售单对应的状态是否更新为：Delivered状态"""
        ValueAssert.value_assert_equal(text_status, "Delivered")


if __name__ == '__main__':
    pytest.main(['SalesManagement_SalesOrder.py'])