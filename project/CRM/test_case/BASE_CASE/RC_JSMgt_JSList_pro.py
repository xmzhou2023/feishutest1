import allure
import pytest
from project.CRM.page_object.RC_JSMgt_JSList_pro import JSPage
from public.base.assert_ui import *
import random, string
import pytest, logging
from public.base.basics import *
from public.base.assert_ui import *
from public.data.unified_login.unified import *
from project.CRM.page_object.Center_Component import NavPage
from public.libs.unified_login.login import Login
from libs.common.read_config import *
from datetime import *
from datetime import timedelta
import math
pro_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import logging
"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""
num = string.ascii_letters + string.digits
digit_no = string.digits
@pytest.fixture(scope='module',autouse=True)
def module_fixture(drivers):
    logging.info("前往RC中的JS Mgt的JS List")
    user = JSPage(drivers)
    user.Clear_Get()
    user = NavPage(drivers)
    user.list_search(content='JS List')
    #user = JSPage(drivers)
    #user.GoTo_JS_List()  # 进入JS页面
    result = DomAssert(drivers)
    result.assert_url("/repairCenter/jobSheetMgt/jobSheetList")
    name = "".join(random.sample(num, 10))  # 名称使用随机数，以防重复名称添加失败
    yield name
    logging.info("\n在当前模块完成后执行的teardown")
    user = JSPage(drivers)
    user.Close_Page()  # 关闭页面
    user.Close_Up_First_Menu("Repair Center")  # 合起菜单




@allure.feature("JSList_pro") # 模块名称
class TestGetJSList:
    @pytest.fixture()
    def class_fixture(self, drivers):
        logging.info("\n这个fixture在每个case前执行一次")
        yield
        logging.info("\n在每个case完成后执行的teardown")
        user = JSPage(drivers)
        user.Clear_Get()  # 恢复查询默认条件


    @allure.story("查询工单")  # 场景名称,中文
    @allure.title("查询工单")  # 用例名称
    @allure.description("JS页面，遍历Service Type下拉框查询正确")
    @allure.severity("critical")  # 用例等级
    # @pytest.mark.parametrize("status", ["RWR", "Normal"])
    @pytest.mark.smoke  # 用例标记
   # @pytest.mark.skip  # 跳过不执行
    def test_1750(self, drivers, class_fixture, __init__):   # 用例名称取名规范'test+场景编号+用例编号'
        user = JSPage(drivers)
        user.JS_Clear_Query_Conditions()
        user.Get_Service_Status_JS(status='Normal')  # 查询成功
        num = DomAssert(drivers)
        if "pro_hk" == __init__:
            num.assert_point_att(1, 3, 'PKJS2022092900688')
        elif "pro_fra" ==__init__:
            num.assert_point_att(1, 3, 'RWJS2022093000055')
        elif "pro_9s" == __init__:
            num.assert_point_att(1, 3, 'TZJSS2022093000018')














if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
