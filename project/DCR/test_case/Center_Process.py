from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.Center_Process import SalesOrderPage
from project.DCR.page_object.Center_Process import InboundReceiptPage
from project.DCR.page_object.SalesManagement_ReturnOrder import ReturnOrderPage
from public.base.basics import Base
from libs.common.connect_sql import *
from public.base.assert_ui import ValueAssert, DomAssert
from libs.common.time_ui import sleep
import pytest
import allure


@allure.feature("销售管理-销售单菜单")
class TestAddDeliverySubSalesOrder:
    @allure.story("业务流程")
    @allure.title("销售单页面，新增销售单操作")
    @allure.description("销售单页面，新增销售单操作成功后，校验新增的销售单是否存在")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_001(self, drivers):
        """DCR 二代账号登录"""
        user = LoginPage(drivers)
        user.dcr_login(drivers, "BD291501", "dcr123456")

        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Sales Management", "Sales Order")

        """销售订单页面，新建销售单、直接出库、筛选、然后快速收货场景功能"""
        add_sales = SalesOrderPage(drivers)
        add_sales.click_add_sales()
        add_sales.input_sales_buyer("EG000562")
        add_sales.input_sales_brand('TECNO')
        add_sales.input_sales_product("SPARK 6 Go 64+4 AQUA BLUE")
        add_sales.input_sales_quantity('1')
        add_sales.click_submit()
        add_sales.click_submit_OK()

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

        """获取列表，销售单ID与Status文本内容"""
        get_sales_order = add_sales.get_text_sales_id()
        get_status = add_sales.get_text_sales_status1()
        """调用断言方法，判断数据库表中查询的销售单ID，与列表获取的销售单ID文本匹配是否一致"""
        ValueAssert.value_assert_equal(get_sales_order, order)
        ValueAssert.value_assert_equal(get_status, sales_status)
        sleep(1)


    @allure.story("业务流程")
    @allure.title("销售单页面，对新增的销售单进行出库操作")
    @allure.description("销售单页面，对新增的销售单进行出库操作成功后，校验销售单状态是否更新")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_002(self, drivers):
        """刷新页面"""
        base = Base(drivers)
        base.refresh()
        sleep(3.5)

        """打开Report Analysis->IMEI Inventory Query菜单"""
        user = LoginPage(drivers)
        user.click_gotomenu("Report Analysis", "IMEI Inventory Query")

        """调用菜单栏，打开IMEI Inventory Query菜单，获取product对应的IMEI"""
        delivery = SalesOrderPage(drivers)
        """查询IMEI Inventory Query页面 指定product的IMEI"""
        delivery.click_unfold()

        delivery.input_material_id("11001120")
        delivery.click_inventory_search()
        imei = delivery.get_text_imei_inventory()

        """ 刷新页面 """
        base.refresh()
        user.click_gotomenu("Sales Management", "Sales Order")

        """二代用户，查询数据库最近新建的销售单ID"""
        user = SQL('DCR', 'test')
        sql = "select order_code,status from t_channel_sale_ticket where warehouse_id = '62134' and seller_id = '1596874516539662' and buyer_id = '1596874516539668' and status = 0 order by created_time desc limit 1"
        result = user.query_db(sql)
        order = result[0].get("order_code")
        """销售单页面，按销售单ID筛选销售单信息"""
        delivery.input_sales_order_ID(order)
        delivery.click_search()

        """勾选新建的销售单，直接出库操作"""
        delivery.click_checkbox_orderID()
        delivery.click_Delivery_button()
        delivery.input_Payment_Mode('Wechat')

        delivery.input_imei(imei)
        delivery.click_check()
        delivery.click_submit_delivery()
        """销售单页面，按销售单ID筛选销售单信息，断言该条销售单对应的状态是否更新为：Delivered状态"""
        text_sales_order = delivery.get_text_sales_id()
        delivery.input_sales_order_ID(text_sales_order)
        delivery.click_search()
        text_status = delivery.get_text_sales_status2()
        """出库操作成功后，验证该条销售单对应的状态是否更新为：Delivered状态"""
        ValueAssert.value_assert_equal(text_status, "Delivered")
        sleep(1)

    @allure.story("业务流程")
    @allure.title("采购管理页面，零售商用户快速收货操作")
    @allure.description("采购管理页面，零售商用户快速收货操作成功后，校验收货状态是否更新")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_003(self, drivers):
        """DCR 二代账号登录"""
        user = LoginPage(drivers)
        user.dcr_login(drivers, "EG00056201", "dcr123456")

        """销售管理菜单-出库单-筛选出库单用例"""
        user = LoginPage(drivers)
        user.click_gotomenu("Purchase Management", "Inbound Receipt")

        """定义账号标识是否是二代sub_Account还是零售商retail_Account 账号收货"""
        usercount = "retail_Account"

        """调用零售商收货筛选与 快速收货用例"""
        receipt = InboundReceiptPage(drivers)
        """查询BD40344201国包账号下出库单数据库表，返回销售单ID与出库单ID，作为筛选条件，验证新增的出库单是否成功"""
        if usercount == "sub_Account":
            """从数据库表，查询最近新建的销售单ID与出库单ID"""
            user = SQL('DCR', 'test')
            varsql = "select order_code,delivery_code from t_channel_delivery_ticket  where warehouse_id='62139' and seller_id='1596874516539667' and buyer_id='1596874516539662' and status=80200000 order by created_time desc limit 1"
            result = user.query_db(varsql)
            salesid = result[0].get("order_code")
            deliveryid = result[0].get("delivery_code")
        elif usercount == "retail_Account":
            """从数据库表，查询最近新建的销售单ID与出库单ID"""
            user = SQL('DCR', 'test')
            varsql1 = "select order_code,delivery_code,status from t_channel_delivery_ticket  where warehouse_id='62134' and seller_id='1596874516539662' and buyer_id='1596874516539668' and status=80200000 order by created_time desc limit 1"
            result = user.query_db(varsql1)
            salesid = result[0].get("order_code")
            deliveryid = result[0].get("delivery_code")

            receipt.input_salesOrder(salesid)
            receipt.input_deliveryOrder(deliveryid)
            receipt.click_search()

            receipt.click_checkbox()
            receipt.click_received()
            receipt.click_save()
            """获取收货提交成功提示语，断言是否包含Successfully提示语"""
            dom = DomAssert(drivers)
            dom.assert_att("Successfully")
            sleep(1.5)
            status = receipt.get_text_status()
            """ 二代收货页面，断言收货后Status更新为：Goods Receipt状态 """
            ValueAssert.value_assert_equal(status, "Goods Receipt")
            """获取列表文本 销售单ID与 出库单ID"""
            salesorder = receipt.get_text_salesOrder(salesid)
            deliveryorder = receipt.get_text_deliveryOrder(deliveryid)
            """筛选二代收货列表数据，断言数据正确性"""
            ValueAssert.value_assert_equal(salesorder, salesid)
            ValueAssert.value_assert_equal(deliveryorder, deliveryid)
            sleep(1)


    @allure.story("业务流程")
    @allure.title("退货页面，零售商用户，对已收货的销售单，进行退货操作")
    @allure.description("退货页面，零售商用户收货成功后，对已收货的销售的，进行退货操作")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_004_001(self, drivers):
            """零售商EG00056201账号, 进行退货操作"""
            """刷新页面"""
            refresh = Base(drivers)
            refresh.refresh()

            """打开Purchase Management菜单"""
            menu = LoginPage(drivers)
            menu.click_gotomenu("Sales Management", "Return Order")

            """实例化 二代退货单类"""
            return_order = ReturnOrderPage(drivers)
            """从数据库表，查询二代账号，最近新建的销售单ID与出库单ID"""
            user = SQL('DCR', 'test')
            varsql = "select order_code,delivery_code from t_channel_delivery_ticket  where warehouse_id='62134' and seller_id='1596874516539662' and buyer_id='1596874516539668' and status=80200001 order by created_time desc limit 1"
            result = user.query_db(varsql)
            delivery_code = result[0].get("delivery_code")

            return_order.click_Add()
            return_order.click_Return_Type()
            return_order.radio_Delivery_order()
            return_order.input_Delivery_order(delivery_code)
            return_order.click_Check()
            record = return_order.get_text_Record()
            ValueAssert.value_assert_equal("Success", record)
            return_order.click_Submit()

            """断言页面是否存在提交成功 Submit Success!文本"""
            dom = DomAssert(drivers)
            dom.assert_att("Submit Success!")
            """方法参数赋值给变量"""
            return_order.input_Delivery_Orderid(delivery_code)
            return_order.click_Search()

            """筛选退货列表页，获取退货出库单ID文本 与数据库表中查询的出库单ID对比是否一致"""
            Delivery_OrderID = return_order.get_text_deliveryID()
            status = return_order.get_return_status()
            ValueAssert.value_assert_equal(Delivery_OrderID, delivery_code)
            ValueAssert.value_assert_equal("Pending Approval", status)
            sleep(1)


    @allure.story("业务流程")
    @allure.title("退货单页面，二代账号, 进行审核退货单操作")
    @allure.description("二代账号, 进行退货审核操作")
    @allure.severity("critical")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_005(self, drivers):
        """退货单列表页面，二代账号, 进行审核退货单操作"""
        user = LoginPage(drivers)
        user.dcr_login(drivers, "BD291501", "dcr123456")

        """打开Purchase Management菜单"""
        user.click_gotomenu("Sales Management", "Return Order")

        """实例化 Return order退货单类"""
        return_approve = ReturnOrderPage(drivers)
        """从数据库表，查询二代账号，最近新建的销售单ID与出库单ID"""
        varsql1 = "select order_code,delivery_code from t_channel_delivery_ticket  where warehouse_id='62134' and seller_id='1596874516539662' and buyer_id='1596874516539668' and status=80200001 order by created_time desc limit 1"
        user = SQL('DCR', 'test')
        result = user.query_db(varsql1)
        delivery_code = result[0].get("delivery_code")

        return_approve.input_Delivery_Orderid(delivery_code)
        return_approve.click_Search()

        return_approve.click_checkbox()
        return_approve.click_Approve_button()
        return_approve.input_remark("同意退货")
        return_approve.click_agree()

        """ 断言页面是否存在审核成功Approval successfully文本 """
        dom = DomAssert(drivers)
        dom.assert_att("Approval successfully")

        """退货成功后，获取列表第一个状态，断言判断是否审核成功"""
        status = return_approve.get_text_Status()
        ValueAssert.value_assert_equal("Approved", status)
        sleep(1)


if __name__ == '__main__':
    pytest.main(['Center_Process'])
