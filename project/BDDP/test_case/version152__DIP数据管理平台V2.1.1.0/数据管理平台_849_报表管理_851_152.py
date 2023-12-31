import pytest
import time
import allure
from project.BDDP.page_object.数据管理平台_报表管理 import baobiaoguanli
from public.base.assert_ui import DomAssert


@allure.feature("数据管理平台_849_报表管理_851")  # 迭代名称
class Teststory_2492:
    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("移动端报表新建验证")  # 用例名称
    @allure.description(
        '步骤1:登录PC端后台管理系统;步骤2:点击报表管理新建;步骤3:选择报表名称应用类型移动端;步骤4:输入主题域选择业务域;步骤5:选择业务负责人.业务组织IT负责人;步骤6:选择页面来源卡片组合;步骤7:选择报表首页差异化是;步骤8:进入角色管理中心进行数据授权;步骤9:选择报表类型总部;步骤10:选择卡片来源财务销售事业分析部;步骤11:选择指标财务销售事业分析部;步骤12:说明销售事业公析;步骤13:点击保存;')  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30876(self, drivers):
        user = baobiaoguanli(drivers)
        user.click_menu1()
        user.click_menu2()
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('报表名称', '销售日报')
        user.input_content('主题域', '零售')
        user.click_theme()
        user.click_theme1()
        user.click_theme2()
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.input_content('业务组织', '深圳传音控股')
        user.click_card_source()
        user.click_card_source1()
        user.click_card_source2()
        # user.click_tg()
        # user.click_tg1()
        # user.click_tg2()
        user.click_explain1('销售情况')
        user.click_report_name1('test')
        user.click_report_name2('test')
        user.click_save_reprot()
        time.sleep(1)
        DomAssert(drivers).assert_att('保存成功！')
        DomAssert(drivers).assert_att('销售日报')
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_report()
        time.sleep(10)
        # user.click_close()

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("PC端报表新建验证")  # 用例名称
    @allure.description(
        "步骤1:登录PC端后台管理系统;步骤2:点击报表管理新建;步骤3:选择报表名称应用类型pc端;步骤4:输入主题域选择业务域;步骤5:选择业务负责人.业务组织IT负责人;步骤6:输入访问地址;步骤7:选择指标财务销售事业分析部;步骤8:说明销售事业公析;步骤9:点击保存;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30877(self, drivers):
        # time.sleep(10)
        user = baobiaoguanli(drivers)
        user.click_menu1()
        user.click_menu2()
        user.click_add()
        user.input_content('应用类型', 'PC端')
        user.assert_input('应用类型', 'PC端')
        user.input_content('报表名称', '销售日报')
        user.input_content('主题域', '零售')
        # user.click_theme()
        # user.click_theme1()
        # user.click_theme2()
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.click_group()
        user.click_group1()
        user.assert_input('业务组织', '深圳传音控股')
        user.click_address()
        user.click_tg()
        user.click_tg1()
        user.click_tg2()
        user.click_explain1('销售情况')
        user.click_report_name01('test')
        user.click_report_name2('test')
        user.click_save_reprot()
        time.sleep(1)
        DomAssert(drivers).assert_att('保存成功！')
        DomAssert(drivers).assert_att('销售日报')
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_report()
        time.sleep(10)
        # user.click_close()

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("大屏端报表新建验证")  # 用例名称
    @allure.description(
        "步骤1:登录PC端后台管理系统;步骤2:点击报表管理新建;步骤3:选择报表名称应用类型大屏端;步骤4:输入主题域选择业务域;步骤5:选择业务负责人.业务组织IT负责人;步骤6:输入访问地址;步骤7:选择指标财务销售事业分析部;步骤8:说明销售事业公析;步骤9:点击保存;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30878(self, drivers):
        # time.sleep(10)
        user = baobiaoguanli(drivers)
        user.click_menu1()
        user.click_menu2()
        user.click_add()
        user.input_content('应用类型', '大屏端')
        user.assert_input('应用类型', '大屏端')
        user.input_content('报表名称', '销售日报')
        user.input_content('主题域', '零售')
        # user.click_theme()
        # user.click_theme1()
        # user.click_theme2()
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.input_content('业务组织', '深圳传音控股')
        user.click_address()
        user.click_tg()
        user.click_tg1()
        user.click_tg2()
        user.click_explain1('销售情况')
        user.click_report_name01('test')
        user.click_report_name2('test')
        user.click_save_reprot()
        time.sleep(1)
        DomAssert(drivers).assert_att('保存成功！')
        DomAssert(drivers).assert_att('销售日报')
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_report()
        time.sleep(10)
        # user.click_close()

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("自助分析端报表新建验证")  # 用例名称
    @allure.description(
        "步骤1:登录PC端后台管理系统;步骤2:点击报表管理新建;步骤3:选择报表名称应用类型自助分析;步骤4:输入主题域选择业务域;步骤5:选择业务负责人.业务组织IT负责人;步骤6:输入访问地址;步骤7:选择指标财务销售事业分析部;步骤8:说明销售事业公析;步骤9:点击保存;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30879(self, drivers):
        # time.sleep(10)
        user = baobiaoguanli(drivers)
        user.click_menu1()
        user.click_menu2()
        user.click_add()
        user.input_content('应用类型', '自助分析')
        user.assert_input('应用类型', '自助分析')
        user.input_content('报表名称', '销售日报')
        user.input_content('主题域', '零售')
        # user.click_theme()
        # user.click_theme1()
        # user.click_theme2()
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.input_content('业务组织', '深圳传音控股')
        user.click_address()
        user.click_tg()
        user.click_tg1()
        user.click_tg2()
        user.click_explain1('销售情况')
        user.click_report_name01('test')
        user.click_report_name2('test')
        user.click_save_reprot()
        time.sleep(1)
        DomAssert(drivers).assert_att('保存成功！')
        DomAssert(drivers).assert_att('销售日报')
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_report()
        time.sleep(10)
        # user.click_close()

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("无首页差异化报表外部引入类报表新建验证")  # 用例名称
    @allure.description(
        "步骤1:登录PC端后台管理系统;步骤2:点击报表管理新建;步骤3:选择报表名称应用类型移动端;步骤4:输入主题域选择业务域;步骤5:选择业务负责人.业务组织IT负责人;步骤6:选择外部引入;步骤7:选择报表首页差异化是;步骤8:进入角色管理中心进行数据授权;步骤9:选择报表类型总部;步骤10:输入外部链接;步骤11:选择指标财务销售事业分析部;步骤12:说明销售事业公析;步骤13:点击保存;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30880(self, drivers):
        # time.sleep(10)
        user = baobiaoguanli(drivers)
        user.click_menu1()
        user.click_menu2()
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('报表名称', '销售日报')
        user.input_content('主题域', '零售')
        # user.click_theme()
        # user.click_theme1()
        # user.click_theme2()
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.input_content('业务组织', '深圳传音控股')
        user.click_external()
        user.click_address()
        user.click_tg()
        user.click_tg1()
        user.click_tg2()
        user.click_explain1('销售情况')
        user.click_report_name01('test')
        user.click_report_name2('test')
        user.click_save_reprot()
        time.sleep(1)
        DomAssert(drivers).assert_att('保存成功！')
        DomAssert(drivers).assert_att('销售日报')
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_report()
        time.sleep(10)
        # user.click_close()

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("无首页差异化报表定制卡片类报表新建验证")  # 用例名称
    @allure.description(
        "步骤1:登录PC端后台管理系统;步骤2:点击报表管理新建;步骤3:选择报表名称应用类型移动端;步骤4:输入主题域选择业务域;步骤5:选择业务负责人.业务组织IT负责人;步骤6:选择定制;步骤7:选择报表首页差异化是;步骤8:进入角色管理中心进行数据授权;步骤9:选择报表类型总部;步骤10:选择私有卡片;步骤11:选择指标财务销售事业分析部;步骤12:说明销售事业公析;步骤13:点击保存;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30881(self, drivers):
        # time.sleep(10)
        user = baobiaoguanli(drivers)
        user.click_menu1()
        user.click_menu2()
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('报表名称', '销售日报')
        user.input_content('主题域', '零售')
        # user.click_theme()
        # user.click_theme1()
        # user.click_theme2()
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.input_content('业务组织', '深圳传音控股')
        user.click_external()
        user.click_address()
        user.click_tg()
        user.click_tg1()
        user.click_tg2()
        user.click_customized()
        user.click_card_source()
        user.click_card_source1()
        user.click_card_source2()
        user.click_explain1('销售情况')
        user.click_report_name01('test')
        user.click_report_name2('test')
        user.click_save_reprot()
        time.sleep(1)
        DomAssert(drivers).assert_att('保存成功！')
        DomAssert(drivers).assert_att('销售日报')
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_report()
        time.sleep(10)
        # user.click_close()

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("无首页差异化报表定制卡片外部引入组合类报表新建验证")  # 用例名称
    @allure.description(
        "步骤1:登录PC端后台管理系统;步骤2:点击报表管理新建;步骤3:选择报表名称应用类型移动端;步骤4:输入主题域选择业务域;步骤5:选择业务负责人.业务组织IT负责人;步骤6:选择定制;步骤7:选择报表首页差异化是;步骤8:进入角色管理中心进行数据授权;步骤9:选择报表类型总部;步骤10:选择私有卡片输入外部链接;步骤11:选择指标财务销售事业分析部;步骤12:说明销售事业公析;步骤13:点击保存;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30883(self, drivers):
        # time.sleep(10)
        user = baobiaoguanli(drivers)
        user.click_menu1()
        user.click_menu2()
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('报表名称', '销售日报')
        user.input_content('主题域', '零售')
        # user.click_theme()
        # user.click_theme1()
        # user.click_theme2()
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.input_content('业务组织', '深圳传音控股')
        user.click_external()
        user.click_address()
        user.click_tg()
        user.click_tg1()
        user.click_tg2()
        user.click_customized()
        user.click_card_source()
        user.click_card_source1()
        user.click_card_source2()
        user.click_explain1('销售情况')
        user.click_report_name01('test')
        user.click_report_name2('test')
        user.click_save_reprot()
        time.sleep(1)
        DomAssert(drivers).assert_att('保存成功！')
        DomAssert(drivers).assert_att('销售日报')
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_report()
        time.sleep(10)
        # user.click_close()

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化卡片组合总部类报表新建验证")  # 用例名称
    @allure.description(
        "步骤1:登录PC端后台管理系统;步骤2:点击报表管理新建;步骤3:选择报表名称应用类型移动端;步骤4:输入主题域选择业务域;步骤5:选择业务负责人.业务组织IT负责人;步骤6:选择页面来源卡片组合;步骤7:选择报表首页差异化是;步骤8:进入角色管理中心进行数据授权;步骤9:选择报表类型总部;步骤10:选择卡片来源财务销售事业分析部;步骤11:选择指标财务销售事业分析部;步骤12:说明销售事业公析;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30884(self, drivers):
        # time.sleep(10)
        user = baobiaoguanli(drivers)
        user.click_menu1()
        user.click_menu2()
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('报表名称', '销售日报')
        user.input_content('主题域', '零售')
        # user.click_theme()
        # user.click_theme1()
        # user.click_theme2()
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.input_content('业务组织', '深圳传音控股')
        user.click_card_source()
        user.click_card_source1()
        user.click_card_source2()
        user.click_tg()
        user.click_tg1()
        user.click_tg2()
        user.click_explain1('销售情况')
        user.click_report_name1('test')
        user.click_report_name2('test')
        user.click_save_reprot()
        time.sleep(1)
        DomAssert(drivers).assert_att('保存成功！')
        DomAssert(drivers).assert_att('销售日报')
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_report()
        time.sleep(10)
        # user.click_close()

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化卡片组合地区部类报表新建验证")  # 用例名称
    @allure.description(
        "步骤1:登录PC端后台管理系统;步骤2:点击报表管理新建;步骤3:选择报表名称应用类型移动端;步骤4:输入主题域选择业务域;步骤5:选择业务负责人.业务组织IT负责人;步骤6:选择页面来源卡片组合;步骤7:选择报表首页差异化是;步骤8:进入角色管理中心进行数据授权;步骤9:选择报表类型地区部;步骤10:选择卡片来源财务销售事业分析部;步骤11:选择指标财务销售事业分析部;步骤12:说明销售事业公析;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30885(self, drivers):
        # time.sleep(10)
        user = baobiaoguanli(drivers)
        user.click_menu1()
        user.click_menu2()
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('报表名称', '销售日报')
        user.input_content('主题域', '零售')
        # user.click_theme()
        # user.click_theme1()
        # user.click_theme2()
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.input_content('业务组织', '深圳传音控股')
        user.click_home()
        user.input_content('报表类型', '地区部')
        user.click_card_source()
        user.click_card_source1()
        user.click_card_source2()
        user.click_tg()
        user.click_tg1()
        user.click_tg2()
        user.click_explain1('销售情况')
        user.click_report_name01('test')
        user.click_report_name2('test')
        user.click_save_reprot()
        time.sleep(1)
        DomAssert(drivers).assert_att('保存成功！')
        DomAssert(drivers).assert_att('销售日报')
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_report()
        time.sleep(10)
        # user.click_close()

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化卡片组合事业部类报表新建验证")  # 用例名称
    @allure.description(
        "步骤1:登录PC端后台管理系统;步骤2:点击报表管理新建;步骤3:选择报表名称应用类型移动端;步骤4:输入主题域选择业务域;步骤5:选择业务负责人.业务组织IT负责人;步骤6:选择页面来源卡片组合;步骤7:选择报表首页差异化是;步骤8:进入角色管理中心进行数据授权;步骤9:选择报表类型事业部;步骤10:选择卡片来源财务销售事业分析部;步骤11:选择指标财务销售事业分析部;步骤12:说明销售事业公析;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30886(self, drivers):
        # time.sleep(10)
        user = baobiaoguanli(drivers)
        user.click_menu1()
        user.click_menu2()
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('报表名称', '销售日报')
        user.input_content('主题域', '零售')
        # user.click_theme()
        # user.click_theme1()
        # user.click_theme2()
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.input_content('业务组织', '深圳传音控股')
        user.click_home()
        user.input_content('报表类型', '事业部')
        user.click_card_source()
        user.click_card_source1()
        user.click_card_source2()
        user.click_tg()
        user.click_tg1()
        user.click_tg2()
        user.click_explain1('销售情况')
        user.click_report_name01('test')
        user.click_report_name2('test')
        user.click_save_reprot()
        time.sleep(1)
        DomAssert(drivers).assert_att('保存成功！')
        DomAssert(drivers).assert_att('销售日报')
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_report()
        time.sleep(10)
        # user.click_close()

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化卡片组合国家类报表新建验证")  # 用例名称
    @allure.description(
        "步骤1:登录PC端后台管理系统;步骤2:点击报表管理新建;步骤3:选择报表名称应用类型移动端;步骤4:输入主题域选择业务域;步骤5:选择业务负责人.业务组织IT负责人;步骤6:选择页面来源卡片组合;步骤7:选择报表首页差异化是;步骤8:进入角色管理中心进行数据授权;步骤9:选择报表类型国家;步骤10:选择卡片来源财务销售事业分析部;步骤11:选择指标财务销售事业分析部;步骤12:说明销售事业公析;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30887(self, drivers):
        # time.sleep(10)
        user = baobiaoguanli(drivers)
        user.click_menu1()
        user.click_menu2()
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('报表名称', '销售日报')
        user.input_content('主题域', '零售')
        # user.click_theme()
        # user.click_theme1()
        # user.click_theme2()
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.input_content('业务组织', '深圳传音控股')
        user.click_home()
        user.input_content('报表类型', '国家')
        user.click_card_source()
        user.click_card_source1()
        user.click_card_source2()
        user.click_tg()
        user.click_tg1()
        user.click_tg2()
        user.click_explain1('销售情况')
        user.click_report_name01('test')
        user.click_report_name2('test')
        user.click_save_reprot()
        time.sleep(1)
        DomAssert(drivers).assert_att('保存成功！')
        DomAssert(drivers).assert_att('销售日报')
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_report()
        time.sleep(10)
        # user.click_close()

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化卡片组合地区部_事业部类报表新建验证")  # 用例名称
    @allure.description(
        "步骤1:登录PC端后台管理系统;步骤2:点击报表管理新建;步骤3:选择报表名称应用类型移动端;步骤4:输入主题域选择业务域;步骤5:选择业务负责人.业务组织IT负责人;步骤6:选择页面来源卡片组合;步骤7:选择报表首页差异化是;步骤8:进入角色管理中心进行数据授权;步骤9:选择报表类型地区部_事业部;步骤10:选择卡片来源财务销售事业分析部;步骤11:选择指标财务销售事业分析部;步骤12:说明销售事业公析;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30888(self, drivers):
        # time.sleep(10)
        user = baobiaoguanli(drivers)
        user.click_menu1()
        user.click_menu2()
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('报表名称', '销售日报')
        user.input_content('主题域', '零售')
        # user.click_theme()
        # user.click_theme1()
        # user.click_theme2()
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.input_content('业务组织', '深圳传音控股')
        user.click_home()
        user.click_home1()
        user.click_CE()
        user.click_BU()
        user.click_card_source()
        user.click_card_source1()
        user.click_card_source2()
        user.click_tg()
        user.click_tg1()
        user.click_tg2()
        user.click_explain1('销售情况')
        user.click_report_name02('test')
        user.click_report_name2('test')
        user.click_save_reprot()
        time.sleep(1)
        DomAssert(drivers).assert_att('保存成功！')
        DomAssert(drivers).assert_att('销售日报')
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_report()
        time.sleep(10)
        # user.click_close()

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化外部引入总部类报表新建验证")  # 用例名称
    @allure.description(
        "步骤1:登录PC端后台管理系统;步骤2:点击报表管理新建;步骤3:选择报表名称应用类型移动端;步骤4:输入主题域选择业务域;步骤5:选择业务负责人.业务组织IT负责人;步骤6:选择外部引入;步骤7:选择报表首页差异化是;步骤8:进入角色管理中心进行数据授权;步骤9:选择报表类型总部;步骤10:输入外部链接;步骤11:选择指标财务销售事业分析部;步骤12:说明销售事业公析;步骤13:点击保存;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30890(self, drivers):
        # time.sleep(10)
        user = baobiaoguanli(drivers)
        user.click_menu1()
        user.click_menu2()
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('报表名称', '销售日报')
        user.input_content('主题域', '零售')
        # user.click_theme()
        # user.click_theme1()
        # user.click_theme2()
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.input_content('业务组织', '深圳传音控股')
        user.click_home()
        user.click_external()
        user.input_content('报表类型', '总部')
        user.click_address1()
        user.click_tg()
        user.click_tg1()
        user.click_tg2()
        user.click_explain1('销售情况')
        user.click_report_name02('test')
        user.click_report_name2('test')
        user.click_save_reprot()
        time.sleep(1)
        DomAssert(drivers).assert_att('保存成功！')
        DomAssert(drivers).assert_att('销售日报')
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_report()
        time.sleep(10)
        # user.click_close()

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化外部引入地区部类报表新建验证")  # 用例名称
    @allure.description(
        "步骤1:登录PC端后台管理系统;步骤2:点击报表管理新建;步骤3:选择报表名称应用类型移动端;步骤4:输入主题域选择业务域;步骤5:选择业务负责人.业务组织IT负责人;步骤6:选择外部引入;步骤7:选择报表首页差异化是;步骤8:进入角色管理中心进行数据授权;步骤9:选择报表类型地区部;步骤10:输入外部链接;步骤11:选择指标财务销售事业分析部;步骤12:说明销售事业公析;步骤13:点击保存;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30891(self, drivers):
        # time.sleep(10)
        user = baobiaoguanli(drivers)
        user.click_menu1()
        user.click_menu2()
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('报表名称', '销售日报')
        user.input_content('主题域', '零售')
        # user.click_theme()
        # user.click_theme1()
        # user.click_theme2()
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.input_content('业务组织', '深圳传音控股')
        user.click_home()
        user.click_external()
        user.input_content('报表类型', '地区部')
        user.click_address1()
        user.click_tg()
        user.click_tg1()
        user.click_tg2()
        user.click_explain1('销售情况')
        user.click_report_name02('test')
        user.click_report_name2('test')
        user.click_save_reprot()
        time.sleep(1)
        DomAssert(drivers).assert_att('保存成功！')
        DomAssert(drivers).assert_att('销售日报')
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_report()
        time.sleep(10)
        # user.click_close()

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化外部引入事业部类报表新建验证")  # 用例名称
    @allure.description(
        "步骤1:登录PC端后台管理系统;步骤2:点击报表管理新建;步骤3:选择报表名称应用类型移动端;步骤4:输入主题域选择业务域;步骤5:选择业务负责人.业务组织IT负责人;步骤6:选择外部引入;步骤7:选择报表首页差异化是;步骤8:进入角色管理中心进行数据授权;步骤9:选择报表类型事业部;步骤10:输入外部链接;步骤11:选择指标财务销售事业分析部;步骤12:说明销售事业公析;步骤13:点击保存;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30892(self, drivers):
        # time.sleep(10)
        user = baobiaoguanli(drivers)
        user.click_menu1()
        user.click_menu2()
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('报表名称', '销售日报')
        user.input_content('主题域', '零售')
        # user.click_theme()
        # user.click_theme1()
        # user.click_theme2()
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.input_content('业务组织', '深圳传音控股')
        user.click_home()
        user.click_external()
        user.input_content('报表类型', '事业部')
        user.click_address1()
        user.click_tg()
        user.click_tg1()
        user.click_tg2()
        user.click_explain1('销售情况')
        user.click_report_name02('test')
        user.click_report_name2('test')
        user.click_save_reprot()
        time.sleep(1)
        DomAssert(drivers).assert_att('保存成功！')
        DomAssert(drivers).assert_att('销售日报')
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_report()
        time.sleep(10)
        # user.click_close()

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化外部引入国家类报表新建验证")  # 用例名称
    @allure.description(
        "步骤1:登录PC端后台管理系统;步骤2:点击报表管理新建;步骤3:选择报表名称应用类型移动端;步骤4:输入主题域选择业务域;步骤5:选择业务负责人.业务组织IT负责人;步骤6:选择外部引入;步骤7:选择报表首页差异化是;步骤8:进入角色管理中心进行数据授权;步骤9:选择报表类型国家部;步骤10:输入外部链接;步骤11:选择指标财务销售事业分析部;步骤12:说明销售事业公析;步骤13:点击保存;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30893(self, drivers):
        # time.sleep(10)
        user = baobiaoguanli(drivers)
        user.click_menu1()
        user.click_menu2()
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('报表名称', '销售日报')
        user.input_content('主题域', '零售')
        # user.click_theme()
        # user.click_theme1()
        # user.click_theme2()
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.input_content('业务组织', '深圳传音控股')
        user.click_home()
        user.click_external()
        user.input_content('报表类型', '国家')
        user.click_address1()
        user.click_tg()
        user.click_tg1()
        user.click_tg2()
        user.click_explain1('销售情况')
        user.click_report_name02('test')
        user.click_report_name2('test')
        user.click_save_reprot()
        time.sleep(1)
        DomAssert(drivers).assert_att('保存成功！')
        DomAssert(drivers).assert_att('销售日报')
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_report()
        time.sleep(10)
        # user.click_close()

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化外部引入地区部_事业部类报表新建验证")  # 用例名称
    @allure.description(
        "步骤1:登录PC端后台管理系统;步骤2:点击报表管理新建;步骤3:选择报表名称应用类型移动端;步骤4:输入主题域选择业务域;步骤5:选择业务负责人.业务组织IT负责人;步骤6:选择外部引入;步骤7:选择报表首页差异化是;步骤8:进入角色管理中心进行数据授权;步骤9:选择报表类型地区事业部;步骤10:输入外部链接;步骤11:选择指标财务销售事业分析部;步骤12:说明销售事业公析;步骤13:点击保存;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30894(self, drivers):
        # time.sleep(10)
        user = baobiaoguanli(drivers)
        user.click_menu1()
        user.click_menu2()
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('报表名称', '销售日报')
        user.input_content('主题域', '零售')
        # user.click_theme()
        # user.click_theme1()
        # user.click_theme2()
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.input_content('业务组织', '深圳传音控股')
        user.click_home()
        user.click_external()
        user.input_content('报表类型', '地区部-事业部')
        user.click_address1()
        user.click_tg()
        user.click_tg1()
        user.click_tg2()
        user.click_explain1('销售情况')
        user.click_report_name02('test')
        user.click_report_name2('test')
        user.click_save_reprot()
        time.sleep(1)
        DomAssert(drivers).assert_att('保存成功！')
        DomAssert(drivers).assert_att('销售日报')
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_report()
        time.sleep(10)
        # user.click_close()

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化外部引入总部地区部_事业部类报表新建验证")  # 用例名称
    @allure.description(
        "步骤1:登录PC端后台管理系统;步骤2:点击报表管理新建;步骤3:选择报表名称应用类型移动端;步骤4:输入主题域选择业务域;步骤5:选择业务负责人.业务组织IT负责人;步骤6:选择外部引入;步骤7:选择报表首页差异化是;步骤8:进入角色管理中心进行数据授权;步骤9:选择报表类型总部地区部;步骤10:输入外部链接;步骤11:选择指标财务销售事业分析部;步骤12:说明销售事业公析;步骤13:点击保存;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30895(self, drivers):
        # time.sleep(10)
        user = baobiaoguanli(drivers)
        user.click_menu1()
        user.click_menu2()
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('报表名称', '销售日报')
        user.input_content('主题域', '零售')
        # user.click_theme()
        # user.click_theme1()
        # user.click_theme2()
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        # user.input_content('业务负责人', '18649432')
        # user.assert_input('业务负责人', '陈嘉18649432')
        # user.input_content('IT负责人', '18648974')
        # user.assert_input('IT负责人', '郭伟18648974')
        # user.input_content('业务组织', '深圳传音控股')
        user.click_external()
        user.click_home()
        user.click_home1()
        user.click_CE()
        user.click_BU()
        user.click_address1()
        user.click_tg()
        user.click_tg1()
        user.click_tg2()
        user.click_explain1('销售情况')
        user.click_report_name03('test')
        user.click_report_name2('test')
        user.click_save_reprot()
        time.sleep(1)
        DomAssert(drivers).assert_att('保存成功！')
        DomAssert(drivers).assert_att('销售日报')
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_report()
        time.sleep(10)
        # user.click_close()

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化定制总部类报表新建验证")  # 用例名称
    @allure.description(
        "步骤1:登录PC端后台管理系统;步骤2:点击报表管理新建;步骤3:选择报表名称应用类型移动端;步骤4:输入主题域选择业务域;步骤5:选择业务负责人.业务组织IT负责人;步骤6:选择页面来源定制;步骤7:选择报表首页差异化是;步骤8:选择报表类型总部;步骤9:进入角色管理中心进行数据授权;步骤10:来源卡片财务销售事业分析部私有化卡片;步骤11:访问地址:输入外部地址;步骤12:选择指标财务销售事业分析部;步骤13:说明销售事业公析;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30896(self, drivers):
        # time.sleep(10)
        user = baobiaoguanli(drivers)
        user.click_menu1()
        user.click_menu2()
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('报表名称', '销售日报')
        user.input_content('主题域', '零售')
        # user.click_theme()
        # user.click_theme1()
        # user.click_theme2()
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.input_content('业务组织', '深圳传音控股')
        user.click_home()
        user.click_external()
        user.input_content('报表类型', '总部')
        user.click_address1()
        user.click_tg()
        user.click_tg1()
        user.click_tg2()
        user.click_customized()
        user.click_card_source()
        user.click_card_source1()
        user.click_card_source2()
        user.click_explain1('销售情况')
        user.click_report_name02('test')
        user.click_report_name2('test')
        user.click_save_reprot()
        time.sleep(1)
        DomAssert(drivers).assert_att('保存成功！')
        DomAssert(drivers).assert_att('销售日报')
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_report()
        time.sleep(10)
        # user.click_close()

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化定制地区部类报表新建验证")  # 用例名称
    @allure.description(
        "步骤1:登录PC端后台管理系统;步骤2:点击报表管理新建;步骤3:选择报表名称应用类型移动端;步骤4:输入主题域选择业务域;步骤5:选择业务负责人.业务组织IT负责人;步骤6:选择页面来源定制;步骤7:选择报表首页差异化是;步骤8:选择报表类型地区部;步骤9:进入角色管理中心进行数据授权;步骤10:来源卡片财务销售事业分析部私有化卡片;步骤11:访问地址:输入外部地址;步骤12:选择指标财务销售事业分析部;步骤13:说明销售事业公析;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30897(self, drivers):
        # time.sleep(10)
        user = baobiaoguanli(drivers)
        user.click_menu1()
        user.click_menu2()
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('报表名称', '销售日报')
        user.input_content('主题域', '零售')
        # user.click_theme()
        # user.click_theme1()
        # user.click_theme2()
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.input_content('业务组织', '深圳传音控股')
        user.click_home()
        user.click_external()
        user.input_content('报表类型', '地区部')
        user.click_address1()
        # user.click_tg()
        # user.click_tg1()
        # user.click_tg2()
        user.click_customized()
        user.click_card_source()
        user.click_card_source1()
        user.click_card_source2()
        user.click_explain1('销售情况')
        user.click_report_name02('test')
        user.click_report_name2('test')
        user.click_save_reprot()
        time.sleep(1)
        DomAssert(drivers).assert_att('保存成功！')
        DomAssert(drivers).assert_att('销售日报')
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_report()
        time.sleep(10)
        # user.click_close()

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化定制国家类报表新建验证")  # 用例名称
    @allure.description(
        "步骤1:登录PC端后台管理系统;步骤2:点击报表管理新建;步骤3:选择报表名称应用类型移动端;步骤4:输入主题域选择业务域;步骤5:选择业务负责人.业务组织IT负责人;步骤6:选择页面来源定制;步骤7:选择报表首页差异化是;步骤8:选择报表类型国家;步骤9:进入角色管理中心进行数据授权;步骤10:来源卡片财务销售事业分析部私有化卡片;步骤11:访问地址:输入外部地址;步骤12:选择指标财务销售事业分析部;步骤13:说明销售事业公析;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30899(self, drivers):
        # time.sleep(10)
        user = baobiaoguanli(drivers)
        user.click_menu1()
        user.click_menu2()
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('报表名称', '销售日报')
        user.input_content('主题域', '零售')
        # user.click_theme()
        # user.click_theme1()
        # user.click_theme2()
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.input_content('业务组织', '深圳传音控股')
        user.click_home()
        user.click_external()
        user.input_content('报表类型', '国家')
        user.click_address1()
        user.click_customized()
        user.click_card_source()
        user.click_card_source1()
        user.click_card_source2()
        user.click_explain1('销售情况')
        user.click_report_name02('test')
        user.click_report_name2('test')
        user.click_save_reprot()
        time.sleep(1)
        DomAssert(drivers).assert_att('保存成功！')
        DomAssert(drivers).assert_att('销售日报')
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_report()
        time.sleep(10)
        # user.click_close()

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化定制地区部_事业部类报表新建验证")  # 用例名称
    @allure.description(
        "步骤1:登录PC端后台管理系统;步骤2:点击报表管理新建;步骤3:选择报表名称应用类型移动端;步骤4:输入主题域选择业务域;步骤5:选择业务负责人.业务组织IT负责人;步骤6:选择页面来源定制;步骤7:选择报表首页差异化是;步骤8:选择报表类型地区部_事业部;步骤9:进入角色管理中心进行数据授权;步骤10:来源卡片财务销售事业分析部私有化卡片;步骤11:访问地址:输入外部地址;步骤12:选择指标财务销售事业分析部;步骤13:说明销售事业公析;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30900(self, drivers):
        # time.sleep(10)
        user = baobiaoguanli(drivers)
        user.click_menu1()
        user.click_menu2()
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('报表名称', '销售日报')
        user.input_content('主题域', '零售')
        # user.click_theme()
        # user.click_theme1()
        # user.click_theme2()
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.input_content('业务组织', '深圳传音控股')
        user.click_home()
        user.click_home1()
        user.click_CE()
        user.click_BU()
        user.click_external()
        user.click_address1()
        user.click_customized()
        user.click_card_source()
        user.click_card_source1()
        user.click_card_source2()
        user.click_explain1('销售情况')
        user.click_report_name03('test')
        user.click_report_name2('test')
        user.click_save_reprot()
        time.sleep(1)
        DomAssert(drivers).assert_att('保存成功！')
        DomAssert(drivers).assert_att('销售日报')
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_report()
        time.sleep(10)
        # user.click_close()

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化卡片组合类报表修改功能验证")  # 用例名称
    @allure.description(
        "步骤1:登录PC端后台管理系统;步骤2:选择已新建成功的报表;步骤3:点击编辑;步骤4:修改报表名称;步骤5:修改主题域;步骤6:修改需求提出人;步骤7:修改业务负责人.业务组织IT负责人;步骤8:修改报表类型卡片组合;步骤9:修改是否差异化是修改报表类型国家;步骤10:修改卡片来源;步骤11:修改分析指标选择2项指标;步骤12:修改说明18字;步骤13:点击保存;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30901(self, drivers):
        # time.sleep(10)
        user = baobiaoguanli(drivers)
        user.click_menu1()
        user.click_menu2()
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('报表名称', '销售日报')
        user.input_content('主题域', '零售')
        # user.click_theme()
        # user.click_theme1()
        # user.click_theme2()
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.input_content('业务组织', '深圳传音控股')
        user.click_home()
        user.input_content('报表类型', '事业部')
        user.click_card_source()
        user.click_card_source1()
        user.click_card_source2()
        user.click_tg()
        user.click_tg1()
        user.click_tg2()
        user.click_explain1('销售情况')
        user.click_report_name04('test')
        user.click_report_name2('test')
        user.click_save_reprot()
        time.sleep(1)
        DomAssert(drivers).assert_att('保存成功！')
        DomAssert(drivers).assert_att('销售日报')
        user.click_edit()
        user.input_content('需求提出人', '18646861')
        user.assert_input('需求提出人', '王佳18646861')
        user.input_content('业务负责人', '18646861')
        user.assert_input('业务负责人', '王佳18646861')
        user.input_content('报表类型', '事业部')
        user.click_card_source()
        user.click_card_source1()
        user.click_card_source2()
        user.click_save_reprot()
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_report()
        time.sleep(10)
        # user.click_close()

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化外部引入类报表修改功能验证")  # 用例名称
    @allure.description(
        "步骤1:登录PC端后台管理系统;步骤2:选择已新建成功的报表;步骤3:点击编辑;步骤4:修改报表名称;步骤5:修改主题域;步骤6:修改需求提出人;步骤7:修改业务负责人.业务组织IT负责人;步骤8:修改报表类型外部引入;步骤9:修改是否差异化是修改报表类型国家;步骤10:修改外部链接;步骤11:修改分析指标选择2项指标;步骤12:修改说明18字;步骤13:点击保存;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30902(self, drivers):
        # time.sleep(10)
        user = baobiaoguanli(drivers)
        user.click_menu1()
        user.click_menu2()
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('报表名称', '销售日报')
        user.input_content('主题域', '零售')
        # user.click_theme()
        # user.click_theme1()
        # user.click_theme2()
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.input_content('业务组织', '深圳传音控股')
        user.click_external()
        user.click_home()
        user.input_content('报表类型', '事业部')
        user.click_address1()
        user.click_tg()
        user.click_tg1()
        user.click_tg2()
        user.click_explain1('销售情况')
        user.click_report_name02('test')
        user.click_report_name2('test')
        user.click_save_reprot()
        time.sleep(1)
        DomAssert(drivers).assert_att('保存成功！')
        DomAssert(drivers).assert_att('销售日报')
        user.click_edit()
        user.input_content('需求提出人', '18646861')
        user.assert_input('需求提出人', '王佳18646861')
        user.input_content('业务负责人', '18646861')
        user.assert_input('业务负责人', '王佳18646861')
        user.input_content('报表类型', '事业部')
        user.click_address1()
        user.click_save_reprot()
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_report()
        time.sleep(10)
        # user.click_close()

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化定制类报表修改功能验证")  # 用例名称
    @allure.description(
        "步骤1:登录PC端后台管理系统;步骤2:选择已新建成功的报表;步骤3:点击编辑;步骤4:修改报表名称;步骤5:修改主题域;步骤6:修改需求提出人;步骤7:修改业务负责人.业务组织IT负责人;步骤8:修改报表类型定制;步骤9:修改是否差异化是修改报表类型国家;步骤10:修改卡片来源外部链接;步骤11:修改分析指标选择2项指标;步骤12:修改说明18字;步骤13:点击保存;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30903(self, drivers):
        # time.sleep(10)
        user = baobiaoguanli(drivers)
        user.click_menu1()
        user.click_menu2()
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('报表名称', '销售日报')
        user.input_content('主题域', '零售')
        # user.click_theme()
        # user.click_theme1()
        # user.click_theme2()
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.input_content('业务组织', '深圳传音控股')
        user.click_home()
        user.click_external()
        user.input_content('报表类型', '总部')
        user.click_address1()
        user.click_tg()
        user.click_tg1()
        user.click_tg2()
        user.click_customized()
        user.click_card_source()
        user.click_card_source1()
        user.click_card_source2()
        user.click_explain1('销售情况')
        user.click_report_name02('test')
        user.click_report_name2('test')
        user.click_save_reprot()
        time.sleep(1)
        DomAssert(drivers).assert_att('保存成功！')
        DomAssert(drivers).assert_att('销售日报')
        user.click_edit()
        user.input_content('需求提出人', '18646861')
        user.assert_input('需求提出人', '王佳18646861')
        user.input_content('业务负责人', '18646861')
        user.assert_input('业务负责人', '王佳18646861')
        user.input_content('报表类型', '事业部')
        user.click_card_source()
        user.click_card_source1()
        user.click_card_source2()
        user.click_address1()
        user.click_save_reprot()
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_report()
        time.sleep(10)
        # user.click_close()

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("无报表差异化卡片组合类报表修改功能验证")  # 用例名称
    @allure.description(
        "步骤1:登录PC端后台管理系统;步骤2:选择已新建成功的报表;步骤3:点击编辑;步骤4:修改报表名称;步骤5:修改主题域;步骤6:修改需求提出人;步骤7:修改业务负责人.业务组织IT负责人;步骤8:修改报表类型卡片组合;步骤9:修改是否差异化否;步骤10:修改卡片来源;步骤11:修改分析指标选择2项指标;步骤12:修改说明18字;步骤13:点击保存;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30904(self, drivers):
        # time.sleep(10)
        user = baobiaoguanli(drivers)
        user.click_menu1()
        user.click_menu2()
        user.click_add()
        user.input_content('应用类型', '移动端')
        user.assert_input('应用类型', '移动端')
        user.input_content('报表名称', '销售日报')
        user.input_content('主题域', '零售')
        # user.click_theme()
        # user.click_theme1()
        # user.click_theme2()
        user.input_content('需求提出人', '18649432')
        user.assert_input('需求提出人', '陈嘉18649432')
        user.input_content('业务负责人', '18649432')
        user.assert_input('业务负责人', '陈嘉18649432')
        user.input_content('IT负责人', '18648974')
        user.assert_input('IT负责人', '郭伟18648974')
        user.input_content('业务组织', '深圳传音控股')
        user.click_card_source()
        user.click_card_source1()
        user.click_card_source2()
        user.click_explain1('销售情况')
        user.click_report_name1('test')
        user.click_report_name2('test')
        user.click_save_reprot()
        time.sleep(1)
        DomAssert(drivers).assert_att('保存成功！')
        DomAssert(drivers).assert_att('销售日报')
        user.click_edit()
        user.input_content('需求提出人', '18646861')
        user.assert_input('需求提出人', '王佳18646861')
        user.input_content('业务负责人', '18646861')
        user.assert_input('业务负责人', '王佳18646861')
        user.click_save_reprot()
        user.click_delete()
        user.click_yes()
        DomAssert(drivers).assert_att('删除成功')
        user.click_close_report()
        time.sleep(10)
        # user.click_close()

    # @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    # @allure.title("报表启用功能验证")  # 用例名称
    # @allure.description("步骤1:登录PC端后台管理系统;步骤2:选择已新建成功的报表;步骤3:点击启用;步骤4:输入申请原因;步骤5:点击保存;")  # 用例描述
    # @allure.severity("blocker")  # 用例等级
    # @pytest.mark.smoke  # 用例标记
    # def test_30907(self, drivers):
    #     #time.sleep(10)
    #     user = baobiaoguanli(drivers)
    #     user.click_menu1()
    #     user.click_menu2()
    #     user.click_add()
    #     user.input_content('应用类型', '移动端')
    #     user.assert_input('应用类型', '移动端')
    #     user.input_content('报表名称', '销售日报')
    #     user.input_content('主题域', '零售')
    #     user.input_content('报表名称', '销售日报')
    #     # user.click_theme()
    #     # user.click_theme1()
    #     # user.click_theme2()
    #     user.input_content('需求提出人', '18649432')
    #     user.assert_input('需求提出人', '陈嘉18649432')
    #     user.input_content('业务负责人', '18649432')
    #     user.assert_input('业务负责人', '陈嘉18649432')
    #     user.input_content('IT负责人', '18648974')
    #     user.assert_input('IT负责人', '郭伟18648974')
    #     user.input_content('业务组织', '深圳传音控股')
    #     user.click_card_source()
    #     user.click_card_source1()
    #     user.click_card_source2()
    #     user.click_explain1('销售情况')
    #     user.click_report_name1('test')
    #     user.click_report_name2('test')
    #     user.click_save_reprot()
    #     time.sleep(1)
    #     DomAssert(drivers).assert_att('保存成功！')
    #     DomAssert(drivers).assert_att('销售日报')
    #     user.click_start()
    #     user.click_yes()
    #     user.click_stop()
    #     user.click_yes()
    #     user.click_edit()
    #     user.click_save()
    #     user.click_delete()
    #     user.click_yes()
    #     DomAssert(drivers).assert_att('删除成功')
    #     user.click_close_report()
    #     time.sleep(10)
    #     #user.click_close()

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("报表类型搜索功能验证")  # 用例名称
    @allure.description("步骤1:登录PC端后台管理系统;步骤2:点击报表搜索框;步骤3:选择报表名称应用类型移动端;步骤4:点击搜索;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30915(self, drivers):
        # time.sleep(10)
        user = baobiaoguanli(drivers)
        user.click_menu1()
        user.click_menu2()
        user.click_code_search()
        user.click_code_search1()
        user.click_search()
        DomAssert(drivers).assert_att("移动端")
        user.click_reset()
        user.click_input_code()
        user.click_search()
        DomAssert(drivers).assert_att("移动端")

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("报表模糊搜索功能验证")  # 用例名称
    @allure.description("步骤1:登录PC端后台管理系统;步骤2:点击模糊搜索框;步骤3:输入模糊报表名称应用类型移动;步骤4:点击搜索;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30916(self, drivers):
        pass

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("无报表差异化外部引入类报表修改功能验证")  # 用例名称
    @allure.description(
        "步骤1:登录PC端后台管理系统;步骤2:选择已新建成功的报表;步骤3:点击编辑;步骤4:修改报表名称;步骤5:修改主题域;步骤6:修改需求提出人;步骤7:修改业务负责人.业务组织IT负责人;步骤8:修改报表类型外部引入;步骤9:修改是否差异化否;步骤10:修改外部链接;步骤11:修改分析指标选择2项指标;步骤12:修改说明18字;步骤13:点击保存;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30905(self, drivers):
        pass

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("无报表差异化定制类报表修改功能验证")  # 用例名称
    @allure.description(
        "步骤1:登录PC端后台管理系统;步骤2:选择已新建成功的报表;步骤3:点击编辑;步骤4:修改报表名称;步骤5:修改主题域;步骤6:修改需求提出人;步骤7:修改业务负责人.业务组织IT负责人;步骤8:修改报表类型定制;步骤9:修改是否差异化否;步骤10:修改卡片来源外部链接;步骤11:修改分析指标选择2项指标;步骤12:修改说明18字;步骤13:点击保存;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30906(self, drivers):
        pass

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("报表类型已启用选择功能验证")  # 用例名称
    @allure.description("步骤1:登录PC端后台管理系统;步骤2:点击首页;步骤3:选择已启用;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30912(self, drivers):
        pass

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("报表类型已停用选择功能验证")  # 用例名称
    @allure.description("步骤1:登录PC端后台管理系统;步骤2:点击首页;步骤3:选择已停用;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30913(self, drivers):
        pass

    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("新建报表卡片来源卡片搜索功能验证")  # 用例名称
    @allure.description(
        "步骤1:登录PC端后台管理系统;步骤2:点击报表管理新建;步骤3:选择报表名称应用类型移动端;步骤4:输入主题域选择业务域;步骤5:选择业务负责人.业务组织IT负责人;步骤6:选择报表组件分享;步骤7:选择是否公开公开;步骤8:选择首页报表池是;步骤9:搜索下钻报表财务销售零售供应链库存金额;")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30914(self, drivers):
        pass


if __name__ == '__main__':
    pass
