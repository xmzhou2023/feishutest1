import allure
import pytest
from public.base.assert_ui import *
from project.TBM.page_object.BOMCooperation_BareMobilePhoneBomCooperation import BareMobilePhoneBomCooperation

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("BOM协作-单机头BOM协作")
class TestCreateProcess:

    @allure.story("创建流程")
    @allure.title("创建流程成功")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在产出品选择一个物料编码，用量填写为1000，点击提交，能提交成功“创建流程成功”")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_001(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_bare_mobile_phone_bom_cooperation_add()
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('制作类型', '单机头BOM制作')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('品牌', 'itel')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('机型', 'X572-1')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('阶段', '试产阶段')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('市场', '埃塞本地')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('同时做衍生BOM', '否')
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.input_bare_mobile_phone_bom_cooperation_bomtree('BOM状态', '试产')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('物料编码', '12011067')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('用量', '1000')
        user.select_bare_mobile_phone_bom_cooperation_business_review('李小素')
        user.click_bare_mobile_phone_bom_cooperation_add_submit()
        DomAssert(drivers).assert_att('创建流程成功')
        user.refresh()
        user.assert_bare_mobile_phone_bom_cooperation_add_result('单机头BOM制作', 'X572-1', 'itel', '埃塞本地', '试产阶段', '审批中', '未同步')
        process_code = user.get_bare_mobile_phone_bom_cooperation_info()[2]
        user.delete_bare_mobile_phone_bom_cooperation_flow(process_code)

    @allure.story("创建流程")
    @allure.title("创建流程成功")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOM "
                        "tree中点击新增BOM，正确填入产成品数据，在指纹模组中新增两颗物料，添加替代组都为A1，份额为一个20，一个80，其他内容正确填写，点击提交，能提交成功并且提示“创建流程成功”")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_002(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_bare_mobile_phone_bom_cooperation_add()
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('制作类型', '单机头BOM制作')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('品牌', 'itel')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('机型', 'X572-1')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('阶段', '试产阶段')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('市场', '埃塞本地')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('同时做衍生BOM', '否')
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.input_bare_mobile_phone_bom_cooperation_bomtree('BOM状态', '试产')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('物料编码', '12011331')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('用量', '1000')
        user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('指纹模组', '物料编码', '17600563')
        user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('指纹模组', '用量', '1000')
        user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('指纹模组', '替代组', 'A1')
        user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('指纹模组', '份额', '20')
        user.click_bare_mobile_phone_bom_cooperation_optional_material()
        user.move_to_add_material('17600563')
        user.input_bare_mobile_phone_bom_cooperation_optional_material('17600563', '物料编码', '17600606')
        user.input_bare_mobile_phone_bom_cooperation_optional_material('17600563', '用量', '1000')
        user.input_bare_mobile_phone_bom_cooperation_optional_material('17600563', '替代组', 'A1')
        user.input_bare_mobile_phone_bom_cooperation_optional_material('17600563', '份额', '80')
        user.select_bare_mobile_phone_bom_cooperation_business_review('李小素')
        user.click_bare_mobile_phone_bom_cooperation_add_submit()
        DomAssert(drivers).assert_att('创建流程成功')
        user.refresh()
        user.assert_bare_mobile_phone_bom_cooperation_add_result('单机头BOM制作', 'X572-1', 'itel', '埃塞本地', '试产阶段', '审批中', '未同步')
        process_code = user.get_bare_mobile_phone_bom_cooperation_info()[2]
        user.delete_bare_mobile_phone_bom_cooperation_flow(process_code)

    @allure.story("创建流程")
    @allure.title("正确选择物料编码，点击一键填写，填写内容保存正确")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM "
                        "tree中点击新增BOM，在单机头中和PCBA中正确选择物料编码，选中两颗物料，点击一键填写，填写用量和1000点击确认，页面上显示两颗物料用量都为1000")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.FT
    def test_001_003(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.bare_mobile_phone_bom_cooperation_add_bom_info()
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.input_bare_mobile_phone_bom_cooperation_bomtree('BOM状态', '试产')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('物料编码', '12011336')
        user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('电池', '物料编码', '25001649')
        user.click_bare_mobile_phone_bom_cooperation_checkbox()
        user.input_bare_mobile_phone_bom_cooperation_one_press('用量', '1000')
        amount = user.get_bare_mobile_phone_bom_cooperation_bomtree_info('单机头')[7]
        ValueAssert(drivers).value_assert_equal(amount, '1000')
        amount = user.get_bare_mobile_phone_bom_cooperation_bomtree_info('电池')[7]
        ValueAssert(drivers).value_assert_equal(amount, '1000')

    @allure.story("创建流程")
    @allure.title("BOM tree中不选择物料，页面上不存在删除按钮")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，不选择物料，页面上不存在删除按钮")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.FT
    def test_001_004(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.bare_mobile_phone_bom_cooperation_add_bom_info()
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.assert_bare_mobile_phone_bom_cooperation_batch_delete(False)

    @allure.story("创建流程")
    @allure.title("选择物料，页面上存在删除按钮")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，选择物料，页面上存在删除按钮")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.FT
    def test_001_005(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.bare_mobile_phone_bom_cooperation_add_bom_info()
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.click_bare_mobile_phone_bom_cooperation_checkbox()
        user.assert_bare_mobile_phone_bom_cooperation_batch_delete(True)

    @allure.story("创建流程")
    @allure.title("选中父节点物料后点击删除，删除页面数据")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确添加物料，选中父节点物料后点击删除，删除页面数据")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.FT
    def test_001_006(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.bare_mobile_phone_bom_cooperation_add_bom_info()
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.click_bare_mobile_phone_bom_cooperation_bomtree_delete('单机头')
        user.click_bare_mobile_phone_bom_cooperation_batch_confirm()
        DomAssert(drivers).assert_att('暂无数据')

    @allure.story("创建流程")
    @allure.title("选中子节点物料后点击删除，清子节点内容")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，正确添加物料，选中子节点物料后点击删除，子节点内容会清空")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.FT
    def test_001_007(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.bare_mobile_phone_bom_cooperation_add_bom_info()
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('电池', '物料编码', '25001649')
        user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('电池', '用量', '1000')
        user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('电池', '替代组', 'A1')
        user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('电池', '份额', '20')
        user.click_bare_mobile_phone_bom_cooperation_bomtree_delete('电池')
        amount = user.get_bare_mobile_phone_bom_cooperation_bomtree_info('电池')[4]
        ValueAssert(drivers).value_assert_equal(amount, '')
        amount = user.get_bare_mobile_phone_bom_cooperation_bomtree_info('电池')[7]
        ValueAssert(drivers).value_assert_equal(amount, '')
        amount = user.get_bare_mobile_phone_bom_cooperation_bomtree_info('电池')[8]
        ValueAssert(drivers).value_assert_equal(amount, '')
        amount = user.get_bare_mobile_phone_bom_cooperation_bomtree_info('电池')[9]
        ValueAssert(drivers).value_assert_equal(amount, '')

    # @allure.story("创建流程")
    # @allure.title("选中子节点物料后点击删除，清子节点内容")
    # @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，选择导入BOM选择正确的文件进行导入，并能应用，点击应用后页面显示的数据与模板的数据一致")
    # @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.FT
    # def test_001_008(self, drivers):
    #     user = BareMobilePhoneBomCooperation(drivers)
    #     user.refresh_webpage_click_menu()
    #     user.bare_mobile_phone_bom_cooperation_add_bom_info()
    #     user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
    #     user.click_bare_mobile_phone_bom_cooperation_bom_import()
    #     user.upload_bare_mobile_phone_bom_cooperation_true_file()

@allure.feature("BOM协作-单机头BOM协作")
class TestCreateProcessExceptionScenario:

    @allure.story("创建流程异常场景")
    @allure.title("导入Bom之前需要选中模板")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个不存在模板的品牌，其他内容正确填写，查看BOM Tree，无新增BOM按钮；点击导入提示'导入Bom之前需要选中模板'")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.FT
    def test_002_001(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_bare_mobile_phone_bom_cooperation_add()
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('制作类型', '单机头BOM制作')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('品牌', 'aaaaa')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('机型', 'X572-1')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('阶段', '试产阶段')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('市场', '埃塞本地')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('同时做衍生BOM', '否')
        user.assert_bare_mobile_phone_bom_cooperation_add_bomtree_exist(False)
        user.click_bare_mobile_phone_bom_cooperation_bom_import()
        DomAssert(drivers).assert_att('导入Bom之前需要选中模板')

    @allure.story("创建流程异常场景")
    @allure.title("不添加BOM内容，提示BOM状态不能为空")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，在BOM tree中点击新增BOM，不添加BOM内容，其他内容正确填写，点击提交，提示BOM状态不能为空")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.FT
    def test_002_002(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_bare_mobile_phone_bom_cooperation_add()
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('制作类型', '单机头BOM制作')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('品牌', 'itel')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('机型', 'X572-1')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('阶段', '试产阶段')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('市场', '埃塞本地')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('同时做衍生BOM', '否')
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.click_bare_mobile_phone_bom_cooperation_add_submit()
        DomAssert(drivers).assert_att('BOM状态不能为空')

    @allure.story("创建流程异常场景")
    @allure.title("不选择BOM状态，提示BOM状态不能为空")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，在BOM tree中点击新增BOM，不选择BOM状态，其他内容正确填写，点击提交，提示BOM状态不能为空")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.FT
    def test_002_003(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_bare_mobile_phone_bom_cooperation_add()
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('制作类型', '单机头BOM制作')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('品牌', 'itel')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('机型', 'X572-1')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('阶段', '试产阶段')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('市场', '埃塞本地')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('同时做衍生BOM', '否')
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.input_bare_mobile_phone_bom_cooperation_bomtree('物料编码', '12011336')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('用量', '1000')
        user.click_bare_mobile_phone_bom_cooperation_add_submit()
        DomAssert(drivers).assert_att('BOM状态不能为空')

    @allure.story("创建流程异常场景")
    @allure.title("BOM编码[null]的物料组在对应的模板中未设置！")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，在BOM tree中点击新增BOM，不填写物料编码，其他内容正确填写，点击提交，提示BOM编码[null]的物料组在对应的模板中未设置！")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.FT
    def test_002_004(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_bare_mobile_phone_bom_cooperation_add()
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('制作类型', '单机头BOM制作')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('品牌', 'itel')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('机型', 'X572-1')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('阶段', '试产阶段')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('市场', '埃塞本地')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('同时做衍生BOM', '否')
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.input_bare_mobile_phone_bom_cooperation_bomtree('BOM状态', '试产')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('用量', '1000')
        user.select_bare_mobile_phone_bom_cooperation_business_review('李小素')
        user.click_bare_mobile_phone_bom_cooperation_add_submit()
        DomAssert(drivers).assert_att('BOM编码[null]的物料组在对应的模板中未设置！')

    @allure.story("创建流程异常场景")
    @allure.title("xxxxxxxx的数量为空")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOM "
                        "tree中点击新增BOM，在产出品选择一个物料编码，用量不进行填写，点击提交，不能提交成功并给出提示“xxxxxxxx的数量为空!”")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.FT
    def test_002_005(self, drivers):
        """
        回归测试用例：005
        用例：进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOM tree中点击新增BOM，在产出品选择一个物料编码，
            用量不进行填写，点击提交，不能提交成功并给出提示“xxxxxxxx的数量为空!”
        """
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_bare_mobile_phone_bom_cooperation_add()
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('制作类型', '单机头BOM制作')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('品牌', 'itel')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('机型', 'X572-1')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('阶段', '试产阶段')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('市场', '埃塞本地')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('同时做衍生BOM', '否')
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.input_bare_mobile_phone_bom_cooperation_bomtree('BOM状态', '试产')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('物料编码', '12011336')
        user.select_bare_mobile_phone_bom_cooperation_business_review('李小素')
        user.click_bare_mobile_phone_bom_cooperation_add_submit()
        DomAssert(drivers).assert_att('[12011336]的数量为空!')

    @allure.story("创建流程异常场景")
    @allure.title("父阶BOM料号xxxxxxxx用量不为1000")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOM "
                        "tree中点击新增BOM，在产出品选择一个物料编码，用量填写为1，点击提交，不能提交成功并给出提示“父阶BOM料号xxxxxxxx用量不为1000”")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.FT
    def test_002_006(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_bare_mobile_phone_bom_cooperation_add()
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('制作类型', '单机头BOM制作')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('品牌', 'itel')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('机型', 'X572-1')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('阶段', '试产阶段')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('市场', '埃塞本地')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('同时做衍生BOM', '否')
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.input_bare_mobile_phone_bom_cooperation_bomtree('BOM状态', '试产')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('物料编码', '12011336')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('用量', '1')
        user.select_bare_mobile_phone_bom_cooperation_business_review('李小素')
        user.click_bare_mobile_phone_bom_cooperation_add_submit()
        DomAssert(drivers).assert_att('父阶BOM料号12011336用量不为1000')

    @allure.story("创建流程异常场景")
    @allure.title("用量只能填写非0数字(最多3位小数)")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOM "
                        "tree中点击新增BOM，在产出品选择一个物料编码，用量填写为非数字类型，点击提交，不能提交成功并给出提示“用量只能填写非0数字(最多3位小数)”")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.FT
    def test_002_007(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_bare_mobile_phone_bom_cooperation_add()
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('制作类型', '单机头BOM制作')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('品牌', 'itel')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('机型', 'X572-1')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('阶段', '试产阶段')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('市场', '埃塞本地')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('同时做衍生BOM', '否')
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.input_bare_mobile_phone_bom_cooperation_bomtree('BOM状态', '试产')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('物料编码', '12011336')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('用量', 'a')
        user.select_bare_mobile_phone_bom_cooperation_business_review('李小素')
        user.click_bare_mobile_phone_bom_cooperation_add_submit()
        DomAssert(drivers).assert_att('用量只能填写非0数字(最多3位小数)')

    @allure.story("创建流程异常场景")
    @allure.title("父阶BOM料号XXXXXXXX下的子阶BOM料号XXXXXXXX用量不为1000")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOM "
                        "tree中点击新增BOM，正确填入产成品数据，选择单机头的物料编码，输入PCBA用量为1，点击提示，不能提交成功并给出提示“父阶BOM料号XXXXXXXX下的子阶BOM"
                        "料号XXXXXXXX用量不为1000”")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.FT
    def test_002_008(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_bare_mobile_phone_bom_cooperation_add()
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('制作类型', '单机头BOM制作')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('品牌', 'itel')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('机型', 'X572-1')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('阶段', '试产阶段')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('市场', '埃塞本地')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('同时做衍生BOM', '否')
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.input_bare_mobile_phone_bom_cooperation_bomtree('BOM状态', '试产')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('物料编码', '12011336')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('用量', '1000')
        user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('PCBA', '物料编码', '12101691')
        user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('PCBA', '用量', '1')
        user.select_bare_mobile_phone_bom_cooperation_business_review('李小素')
        user.click_bare_mobile_phone_bom_cooperation_add_submit()
        DomAssert(drivers).assert_att('父阶BOM料号12011336下的子阶BOM料号12101691用量不为1000')

    @allure.story("创建流程异常场景")
    @allure.title("业务评审MPM不能为空！")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOM "
                        "tree中点击新增BOM，正确填入产成品数据，业务评审不选择相应的评审人员，点击提交，不能提交成功，并给出提示“业务评审MPM不能为空！”")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.FT
    def test_002_009(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_bare_mobile_phone_bom_cooperation_add()
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('制作类型', '单机头BOM制作')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('品牌', 'itel')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('机型', 'X572-1')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('阶段', '试产阶段')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('市场', '埃塞本地')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('同时做衍生BOM', '否')
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.input_bare_mobile_phone_bom_cooperation_bomtree('BOM状态', '试产')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('物料编码', '12011336')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('用量', '1000')
        user.click_bare_mobile_phone_bom_cooperation_add_submit()
        DomAssert(drivers).assert_att('业务评审MPM不能为空！')

    @allure.story("创建流程异常场景")
    @allure.title("业务评审MPM不能为空！")
    @allure.description("进入新增页面制作类型选择单机头BOM制作，选择一个存在模板的品牌，在BOM "
                        "tree中点击新增BOM，正确填入产成品数据，业务评审MPM不选择评审人员，其他选择审批人员，点击提交，不能提交成功，并给出提示“业务评审MPM不能为空！”")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.FT
    def test_002_010(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.click_bare_mobile_phone_bom_cooperation_add()
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('制作类型', '单机头BOM制作')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('品牌', 'itel')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('机型', 'X572-1')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('阶段', '试产阶段')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('市场', '埃塞本地')
        user.input_bare_mobile_phone_bom_cooperation_add_bom_info('同时做衍生BOM', '否')
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.input_bare_mobile_phone_bom_cooperation_bomtree('BOM状态', '试产')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('物料编码', '12011336')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('用量', '1000')
        user.select_bare_mobile_phone_bom_cooperation_business_review('李小素', '项目经理')
        user.click_bare_mobile_phone_bom_cooperation_add_submit()
        DomAssert(drivers).assert_att('业务评审MPM不能为空！')

    @allure.story("创建流程异常场景")
    @allure.title("[XXXXXX] 替代组[XX]的份额总和不为100")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM "
                        "tree中点击新增BOM，正确填入产成品数据，在充电器中新增两颗物料，添加替代组都为A1，份额为一个20，一个20"
                        "，其他内容正确填写，点击提交，不能提交成功并且提示替代组&份额相加不为100")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.FT
    def test_002_011(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.bare_mobile_phone_bom_cooperation_add_bom_info()
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.input_bare_mobile_phone_bom_cooperation_bomtree('BOM状态', '试产')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('物料编码', '12011336')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('用量', '1000')
        user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('电池', '物料编码', '25001649')
        user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('电池', '用量', '1000')
        user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('电池', '替代组', 'A1')
        user.input_bare_mobile_phone_bom_cooperation_optional_bomtree('电池', '份额', '20')
        user.click_bare_mobile_phone_bom_cooperation_optional_material()
        user.move_to_add_material('25001649')
        user.input_bare_mobile_phone_bom_cooperation_optional_material('25001649', '物料编码', '25001643')
        user.input_bare_mobile_phone_bom_cooperation_optional_material('25001649', '用量', '1000')
        user.input_bare_mobile_phone_bom_cooperation_optional_material('25001649', '替代组', 'A1')
        user.input_bare_mobile_phone_bom_cooperation_optional_material('25001649', '份额', '20')
        user.select_bare_mobile_phone_bom_cooperation_business_review('李小素')
        user.click_bare_mobile_phone_bom_cooperation_add_submit()
        DomAssert(drivers).assert_att('[12011336] 替代组[A1]的份额总和不为100')

    @allure.story("创建流程异常场景")
    @allure.title("填入产成品数据，不选择物料，一键填写用量，页面上没有填写上任何数据")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM "
                        "tree中点击新增BOM，正确填入产成品数据，不选择物料，点击一键填写，填写用量为1000，点击确定，页面上没有填写上任何数据")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.FT
    def test_002_012(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.bare_mobile_phone_bom_cooperation_add_bom_info()
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.input_bare_mobile_phone_bom_cooperation_bomtree('BOM状态', '试产')
        user.input_bare_mobile_phone_bom_cooperation_bomtree('物料编码', '12011336')
        user.input_bare_mobile_phone_bom_cooperation_one_press('用量', '1000')
        amount = user.get_bare_mobile_phone_bom_cooperation_bomtree_info('单机头')[7]
        ValueAssert(drivers).value_assert_equal(amount, '')

    @allure.story("创建流程异常场景")
    @allure.title("不填写产成品数据，全选一键填写用量，页面上没有填写上任何数据")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM "
                        "tree中点击新增BOM，在产成品中不选择物料编码，全选选中物料，点击一键填写，一键填写时选择用量和1000，点击确定，页面上不会新增用量数量")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.FT
    def test_002_013(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.bare_mobile_phone_bom_cooperation_add_bom_info()
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.click_bare_mobile_phone_bom_cooperation_checkbox()
        user.input_bare_mobile_phone_bom_cooperation_one_press('用量', '1000')
        amount = user.get_bare_mobile_phone_bom_cooperation_bomtree_info('单机头')[7]
        ValueAssert(drivers).value_assert_equal(amount, '')

    @allure.story("创建流程异常场景")
    @allure.title("文件类型非excel!")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM "
                        "tree中点击新增BOM，选择导入BOM选择一个错误的文件格式进行导入，不能导入成功并提示“文件类型非excel!”")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.FT
    def test_002_014(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.bare_mobile_phone_bom_cooperation_add_bom_info()
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.click_bare_mobile_phone_bom_cooperation_bom_import()
        user.upload_bare_mobile_phone_bom_cooperation_wrong_file()
        DomAssert(drivers).assert_att('文件类型非excel!')

    @allure.story("创建流程异常场景")
    @allure.title("模板正确内容错误的文件导入失败，并在校验结果给出相应错误提示，导出校验可点击")
    @allure.description("进入新增页面制作类型选择单机头BOM协作，选择一个存在模板的品牌，在BOM "
                        "tree中点击新增BOM，选择导入BOM选择一个模板正确内容错误的文件进行导入，导入失败，并在校验结果给出相应错误提示，导出校验可点击并能成功下载文件")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.FT
    def test_002_015(self, drivers):
        user = BareMobilePhoneBomCooperation(drivers)
        user.refresh_webpage_click_menu()
        user.bare_mobile_phone_bom_cooperation_add_bom_info()
        user.click_bare_mobile_phone_bom_cooperation_add_bomtree()
        user.click_bare_mobile_phone_bom_cooperation_bom_import()
        user.upload_bare_mobile_phone_bom_cooperation_wrongcontent_file()
        user.assert_bare_mobile_phone_bom_cooperation_wrongcontent_upload_result()



if __name__ == '__main__':
    pytest.main(['BOMCooperation_BareMobilePhoneBomCooperation.py'])