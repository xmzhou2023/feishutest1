import allure
import pytest

from public.base.assert_ui import *
from project.DRP.page_object.Center_Component import NavPage
from project.DRP.page_object.DRPDataMgmt_ColorLibrary import ColorLibrary


@pytest.fixture(scope='module', autouse=True)
def setup_module(drivers):
    logging.info("模块前置条件：前往“DRP数据管理-颜色库”页面")
    user = NavPage(drivers)
    user.click_gotonav("DRP数据管理", "颜色库")
    user = DomAssert(drivers)
    user.assert_url("/dataManage/colorLibrary")


@allure.feature("DRP数据管理-颜色库")
class TestSearchColor:
    @allure.story("查询颜色")
    @allure.title("按照颜色条件（颜色名称Zh）过滤颜色库信息")
    @allure.description("输入颜色名称Zh，查询 颜色=123 的颜色库信息")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_001(self, drivers):
        color = ColorLibrary(drivers)
        color.input_color("半透黑")
        color.query_button()
        color.screen_assert("颜色名称Zh", "半透黑")
        color.reset_button()

    @allure.story("查询颜色")
    @allure.title("按照颜色条件（颜色名称En）过滤颜色库信息")
    @allure.description("输入颜色名称En，查询 颜色=ABC 的颜色库信息")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_002(self, drivers):
        color = ColorLibrary(drivers)
        color.input_color("Aegean Blue")
        color.query_button()
        color.screen_assert("颜色名称En", "Aegean Blue")
        color.reset_button()

    @allure.story("查询颜色")
    @allure.title("按照颜色条件（颜色编码）过滤颜色库信息")
    @allure.description("输入颜色编码，查询 颜色编码=# 的颜色库信息")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_003(self, drivers):
        color = ColorLibrary(drivers)
        color.input_color("#")
        color.query_button()
        color.screen_assert("颜色编码", "#")
        color.reset_button()

    @allure.story("查询可用状态")
    @allure.title("按照可用状态条件过滤颜色库信息")
    @allure.description("选择可用状态 为禁用的颜色库信息")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_004(self, drivers):
        color = ColorLibrary(drivers)
        color.choice_state("禁用")
        color.query_button()
        color.screen_assert("可用状态", "禁用")
        color.reset_button()

    @allure.story("组合查询颜色库（颜色、可用状态）")
    @allure.title("按照可用状态条件过滤颜色库信息")
    @allure.description("选择可用状态 为禁用的颜色库信息")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_005(self, drivers):
        color = ColorLibrary(drivers)
        color.input_color("#")
        color.choice_state("启用")
        color.query_button()
        color.screen_assert("颜色编码", "#")
        color.screen_assert("可用状态", "启用")
        color.reset_button()

    @allure.story("查询条件重置")
    @allure.title("点击重置按钮，查询条件清空，列表数据恢复")
    @allure.description("先通过条件过滤， 点击重置按钮，查询条件清空，列表数据恢复")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_006(self, drivers):
        color = ColorLibrary(drivers)
        color.input_color("#")
        color.choice_state("启用")
        color.query_button()
        beforeNum = color.listnum_assert()
        color.reset_button()
        afterNum = color.listnum_assert()
        ValueAssert.value_assert_Notequal(beforeNum, afterNum)


@allure.feature("DRP数据管理-颜色库")
class TestExportColorLibrary:
    @allure.story("导出Excel")
    @allure.title("点击导出按钮，导出Excel")
    @allure.description("点击导出按钮，导出Excel")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_001(self, drivers):
        color = ColorLibrary(drivers)
        color.export_button("drp_color_export")


@allure.feature("DRP数据管理-颜色库")
class TestAppendColor:
    @allure.story("新增颜色库数据")
    @allure.title("点击新增按钮，维护颜色信息 保存")
    @allure.description("点击新增按钮，维护颜色信息 颜色名称Zh=123,颜色名称Eh=ABC,备注=123，保存成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_001(self, drivers):
        color = ColorLibrary(drivers)
        color.append_button()
        color.input_colorinf("3", "", "123")
        color.input_colorinf("4", "", "ABC")
        color.input_colorinf("5", "", "123")
        color.save_button()
        color.list_assert(inputcolor="AB", lis="2", colorcode="ABC")  # 页面列表数据断言
        color.list_assert(inputcolor="AB", lis="3", colorcode="123")  # 页面列表数据断言
        color.clear_testdata("123", "ABC", "123", "隆江")


@allure.feature("DRP数据管理-颜色库")
class TestEditColor:
    @allure.story("修改颜色库数据")
    @allure.title("点击指定行编辑按钮，修改颜色信息 保存")
    @allure.description("点击指定行编辑按钮，修改颜色信息 颜色名称Zh=123->456,颜色名称Eh=ABC->zzz,备注=123->aaa，保存成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.skip
    def test_004_001(self, drivers):
        color = ColorLibrary(drivers)
        # color.precondition_addtestdata(drivers)
        color.precondition_selecttestdata("ABC")
        color.edit_button("ABC")
        color.edit_color("ABC","3","123","456")
        color.save_button()
        color.list_assert(inputcolor="456", lis="3", colorcode="456")  # 页面列表数据断言
        color.clear_testdata("456",  "隆江")



if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/DRPDataMgmt_ColorLibrary.py'])