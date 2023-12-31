from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.AssetManagement_AssetDefinition import AssetDefinitionPage
from public.base.assert_ui import ValueAssert, DomAssert
import logging
from libs.common.connect_sql import *
from libs.common.time_ui import sleep
from public.base.basics import Base
import datetime
import pytest
import allure

"""后置关闭菜单方法  pytest.fixture(scope='作用域' function函数级别  """
@pytest.fixture(scope='function')
def function_menu_fixture(drivers):
    yield
    menu = LoginPage(drivers)
    get_menu_class = menu.get_open_menu_class()
    class_value = "tags-view-item router-link-exact-active router-link-active active"
    if class_value == str(get_menu_class):
        menu.click_close_open_menu()

@allure.feature("资产管理-资产定义")
class TestQueryAsset:
    @allure.story("查询资产")
    @allure.title("资产管理页面，查询资产")
    @allure.description("资产管理页面，根据创建日期与资产名称筛选资产，断言列表是否能正常查询指定的资产")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    @pytest.mark.UT
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """考勤管理-打开考勤记录页面"""
        user.click_gotomenu("Asset Management", "Asset Definition")

        query = AssetDefinitionPage(drivers)
        """获取当天日期"""
        base = Base(drivers)
        today = base.get_datetime_today()

        query.query_createdate_category('2022-11-01', today, 'Promotion Gift')
        get_asset_name_cn = query.get_list_field_content('Get list Asset Name CN')
        query.query_asset_name(get_asset_name_cn)
        query.click_search()

        get_category = query.get_list_field_content('Get list Category')
        get_asset_name_cn2 = query.get_list_field_content('Get list Asset Name CN')
        ValueAssert.value_assert_equal(get_asset_name_cn, get_asset_name_cn2)
        ValueAssert.value_assert_equal('Promotion Gift', get_category)
        get_total = query.get_list_total()
        query.assert_total(get_total)


@allure.feature("资产管理-资产定义")
class TestAddAsset:
    @allure.story("新增资产")
    @allure.title("资产管理页面，新增资产")
    @allure.description("资产管理页面，新增资产操作，断言资产管理列表是否加载新增的资产信息")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    @pytest.mark.UT
    def test_002_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """考勤管理-打开考勤记录页面"""
        user.click_gotomenu("Asset Management", "Asset Definition")

        add = AssetDefinitionPage(drivers)
        #点击add新增按钮
        add.click_add_asset()
        #随机生成资产编号
        num = add.asset_random()
        version = 'max1'+num
        name_en = 'Infinix Smart Phone'+num
        name_cn = 'Infinix智能机' + num

        #新增资产
        add.add_asset('Infinix', 'Headquarters', 'Promotion Gift', name_en, name_cn, version, '88')
        add.click_upload_picture('20211207_110302.png')
        DomAssert(drivers).assert_att("Success")
        #点击提交按钮
        add.click_add_submit()
        DomAssert(drivers).assert_att("Created Successfully")

        #查询新建的资产信息
        """获取当天日期"""
        base = Base(drivers)
        today = base.get_datetime_today()
        #根据Create Date,Category,Asset Name字段筛选新增的资产数据
        add.query_asset_info(today, today, 'Promotion Gift', name_en)
        add.click_search()

        #返回Asset Definition列表，查询是否加载新增的资产信息
        brand = add.get_list_field_content('Get list Brand')
        design_by = add.get_list_field_content('Get list Design By')
        category = add.get_list_field_content('Get list Category')
        get_version = add.get_list_field_content('Get list Version')
        asset_name_cn = add.get_list_field_content('Get list Asset Name CN')
        asset_name_en = add.get_list_field_content('Get list Asset Name EN')
        get_cost = add.get_list_field_content('Get list Cost')
        create_date = add.get_list_field_content('Get list Create Date')
        get_picture = add.get_list_field_content('Get list Picture')
        #断言相等比较列表字段内容是否一致
        ValueAssert.value_assert_equal(brand, 'Infinix')
        ValueAssert.value_assert_equal(design_by, 'Headquarters')
        ValueAssert.value_assert_equal(category, 'Promotion Gift')
        ValueAssert.value_assert_equal(get_version, version)
        ValueAssert.value_assert_equal(asset_name_cn, name_cn)
        ValueAssert.value_assert_equal(asset_name_en, name_en)
        ValueAssert.value_assert_In(get_cost, '88')
        ValueAssert.value_assert_In(today, create_date)
        ValueAssert.value_assert_equal("Picture", get_picture)


@allure.feature("资产管理-资产定义")
class TestEditAsset:
    @allure.story("修改资产")
    @allure.title("资产管理页面，修改资产")
    @allure.description("资产管理页面，对新增的资产，进行修改操作，断言资产管理列表是否更新修改后的资产信息")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    @pytest.mark.UT
    def test_003_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """考勤管理-打开考勤记录页面"""
        user.click_gotomenu("Asset Management", "Asset Definition")
        edit = AssetDefinitionPage(drivers)

        """获取当天日期"""
        base = Base(drivers)
        today = base.get_datetime_today()

        #根据Create Date,Category,Asset Name字段筛选新增的资产数据，进行编辑操作
        edit.query_asset_info_edit(today, today, 'Promotion Gift')
        edit.click_search()
        get_asset_name_en1 = edit.get_list_field_content('Get list Asset Name EN')
        edit.query_asset_name(get_asset_name_en1)
        edit.click_search()

        #点击编辑按钮
        edit.click_edit()
        #随机生成资产编号
        num = edit.asset_random()
        version = 'max1'+num
        name_en = 'Infinix Smart Phone'+num
        name_cn = 'Infinix智能机' + num
        #修改资产属性
        edit.edit_asset(name_en, name_cn, version, '93')
        #点击提交
        edit.click_edit_submit()
        DomAssert(drivers).assert_att("Edited Successfully")
        sleep(1)
        #根据修改后的资产名称，筛查修改后的资产数据
        edit.query_asset_info(today, today, 'Promotion Gift', name_en)
        edit.click_search()

        #断言列表是否更新修改后的内容
        get_version = edit.get_list_field_content('Get list Version')
        get_asset_name_cn = edit.get_list_field_content('Get list Asset Name CN')
        get_asset_name_en = edit.get_list_field_content('Get list Asset Name EN')
        get_cost = edit.get_list_field_content('Get list Cost')
        create_date = edit.get_list_field_content('Get list Create Date')

        ValueAssert.value_assert_equal(get_version, version)
        ValueAssert.value_assert_equal(get_asset_name_cn, name_cn)
        ValueAssert.value_assert_equal(get_asset_name_en, name_en)
        ValueAssert.value_assert_In(get_cost, '93')
        ValueAssert.value_assert_In(today, create_date)


@allure.feature("资产管理-资产定义")
class TestDeleteAsset:
    @allure.story("删除资产")
    @allure.title("资产定义页面，删除当前新增的资产")
    @allure.description("资产定义页面，对新增的资产进行删除操作，断言是否删除成功")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    @pytest.mark.UT
    def test_004_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """考勤管理-打开考勤记录页面"""
        user.click_gotomenu("Asset Management", "Asset Definition")
        delete = AssetDefinitionPage(drivers)

        """获取当天日期"""
        base = Base(drivers)
        today = base.get_datetime_today()

        #根据Create Date,Category,Asset Name字段筛选新增的资产数据，进行删除操作
        delete.query_asset_info_edit(today, today, 'Promotion Gift')
        delete.click_search()
        get_asset_name_en1 = delete.get_list_field_content('Get list Asset Name EN')
        delete.query_asset_name(get_asset_name_en1)
        delete.click_search()

        get_total = delete.get_list_total()
        logging.info("获取Asset Definition列表总条数为：{}".format(get_total))
        if int(get_total) >= 1:
            sql1 = SQL('DCR', 'test', 'SQL', 'db2')
            sql_query_id = f"select id from t_retail_asset_definition where asset_name_en='{get_asset_name_en1}'"
            result = sql1.query_db(sql_query_id)
            logging.info("打印返回值result:{}".format(result))
            asset_id = result[0].get("id")
            logging.info("打印结果asset_id:{}".format(asset_id))
            sql1.delete_db(
                    f"delete from t_retail_asset_definition where asset_name_en='{get_asset_name_en1}'")
            sql1.delete_db(
                    f"delete from t_retail_asset_definition_country  where  asset_id='{asset_id}'")
        else:
            logging.info("打印Asset Definition列表总条数为：{}".format(get_total))


if __name__ == '__main__':
    pytest.main(['AssetManagement_AssetDefinition.py'])
