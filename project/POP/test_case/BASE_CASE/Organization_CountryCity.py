import allure
import pytest
from project.POP.page_object.Organization_CountryCity import QueryCountry,ExportCountryCity
from project.POP.page_object.Center_Component import NavPage
from libs.common.read_element import Element
from project.POP.test_case.conftest import *
object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)
@pytest.fixture(scope='function', autouse=True)
def setup_class(drivers):
    logging.info("模块前置条件：前往“POP组织-国家城市”页面")
    nav = NavPage(drivers)
    nav.click_gotonav("组织","国家城市")

@allure.feature("组织-国家城市") # 模块名称
class TestQueryCountry:
    @allure.story("国家城市") # 场景名称
    @allure.title("查询国家")  # 用例名称
    @allure.description("输入国家，查询国家")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self,drivers):
        users = QueryCountry(drivers)
        users .querycountry("国家城市框","China")
        sleep(2)
        # 断言-- 输入国家与查询结果显示的国家一致
        test = users.element_text(user['国家城市断言'])
        ValueAssert.value_assert_equal(test,"China")

    @allure.story("国家城市")  # 场景名称
    @allure.title("查询国家")  # 用例名称
    @allure.description("输入是否禁用，查询对应状态的国家")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):
        users = QueryCountry(drivers)
        users.querycountry("是否禁用框", "禁用")
        sleep(2)
        # 断言-- 输入国家与查询结果显示的国家一致
        test = users.element_text(user['是否禁用断言'])
        ValueAssert.value_assert_equal(test, "否")

    @allure.story("国家城市")  # 场景名称
    @allure.title("查询国家")  # 用例名称
    @allure.description("输入城市等级，查询对应城市等级的国家")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_003(self, drivers):
        users = QueryCountry(drivers)
        users.querycountry("城市等级框", "T1")
        sleep(2)
        # 断言-- 输入国家与查询结果显示的国家一致
        test = users.element_text(user['城市等级断言'])
        ValueAssert.value_assert_equal(test, "T1")

@allure.feature("组织-国家城市") # 模块名称
class TestExportCoutrycity:
    @allure.story("国家城市")  # 场景名称
    @allure.title("导出国家城市列表")  # 用例名称
    @allure.description("点击导出，导出国家城市列表")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        users = ExportCountryCity(drivers)
        users.click_export()
        sleep(0.5)
        # 断言--提示：XXXX导出成功
        test = users.element_text(user['导出成功提示'])
        ValueAssert.value_assert_equal(test,'创建导出任务成功！')



if __name__ == '__main__':
    pytest.main(['Organization_CountryCity.py::TestQueryCountry'])