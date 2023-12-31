from datetime import datetime
import pytest
from public.base.assert_ui import *
from project.TBM.page_object.ShippingCountry_ShippingCountryFlow import ShippingCountryFlow


@allure.feature("出货国家-出货国家流程")  # 模块名称
class TestCreateProcess:
    @allure.story("创建流程")  # 场景名称
    @allure.title("创建流程成功")  # 用例名称
    @allure.description("项目信息随便填，产品定义信息随便填（品牌暂时选择Infinix），选择汇签/抄送人员，点击提交，提示请求成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):
        user = ShippingCountryFlow(drivers)
        querytime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_add_item_info('品牌', 'Infinix')
        user.input_add_item_info('项目', f'项目名称{querytime}')
        user.click_add()
        user.input_product_definition_info('全球版本', 'SMART')
        user.input_product_definition_info('市场名称', f'市场名称{querytime}')
        user.input_product_definition_info('项目名称', f'项目名称{querytime}')
        user.input_product_definition_info('MEMORY', '256+12')
        user.input_product_definition_info('BAND STRATEGY', '拉美BOM')
        user.input_product_definition_info('项目经理', '李小素')
        user.input_product_definition_info('摄像头', '摄像头')
        user.input_product_definition_info('型号', '型号')
        user.input_product_definition_info('新增', '新增')
        user.input_product_definition_info('再增', '2.5G')
        user.input_product_definition_info('配色', '魅海蓝/Aqua Blue')
        user.input_product_definition_info('尺寸', '64M+13M+2M')
        user.input_product_definition_info('首单量产时间', querytime[0:10])
        user.click_product_definition_confirm()
        user.select_signatory('汇签人员', '李小素')
        user.click_add_submit()
        DomAssert(drivers).assert_att('请求成功')
        process_code = user.get_info(f'项目名称{querytime}')[2]
        user.delete_shipping_country_flow(process_code)

    @allure.story("创建流程")  # 场景名称
    @allure.title("选择全球版本，汇签人员会自动获取人员")  # 用例名称
    @allure.description("进入出货国家流程后，点击进行新增，新增页面选择品牌后，在产品定义信息中点击新增，新增时选择全球版本，选择全球版本后，汇签人员会自动获取人员")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):
        user = ShippingCountryFlow(drivers)
        user.refresh_webpage_click_menu()
        querytime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        user.click_add()
        user.input_add_item_info('品牌', 'Infinix')
        user.input_add_item_info('项目', f'项目名称{querytime}')
        user.click_add()
        user.input_product_definition_info('全球版本', 'SMART')
        user.assert_version_get_member('SMART')
        user.input_product_definition_info('全球版本', 'HOT')
        user.assert_version_get_member('HOT')
        user.input_product_definition_info('全球版本', 'NOTE')
        user.assert_version_get_member('NOTE')

    @allure.story("创建流程")  # 场景名称
    @allure.title("新增产品经理和项目经理，查看抄送人员是自动添加登录人+产品经理+项目经理")  # 用例名称
    @allure.description("进入出货国家流程，点击新增，新增页面选择品牌后，在产品定义信息中，新增产品经理和项目经理，查看抄送人员是自动添加登录人+产品经理+项目经理")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_003(self, drivers):
        user = ShippingCountryFlow(drivers)
        user.refresh_webpage_click_menu()
        querytime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        user.click_add()
        user.input_add_item_info('品牌', 'Infinix')
        user.input_add_item_info('项目', f'项目名称{querytime}')
        user.click_add()
        user.input_product_definition_info('产品经理', '陈月')
        user.input_product_definition_info('项目经理', '潘美佳')
        user.assert_member('抄送人员', ['陈月', '潘美佳', '李小素'])

    @allure.story("创建流程")  # 场景名称
    @allure.title("产品定义信息中存在该条已选择的数据")  # 用例名称
    @allure.description("进入出货国家流程，点击新增，新增页面选择品牌后，在产品定义信息中，点击变更已有产品，会弹出选择框，选中其中一条数据，点击选择，产品定义信息中存在该条已选择的数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_004(self, drivers):
        user = ShippingCountryFlow(drivers)
        user.refresh_webpage_click_menu()
        querytime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        user.click_add()
        user.input_add_item_info('品牌', 'Infinix')
        user.input_add_item_info('项目', f'项目名称{querytime}')
        user.click_products()
        user.search_products('市场名称', '出货国家查询-变更产品-全流程-自动化测试项目-市场名称')
        user.select_products('出货国家查询-变更产品-全流程-自动化测试项目-市场名称')
        user.assert_change_success('出货国家查询-变更产品-全流程-自动化测试项目-市场名称')

    @allure.story("创建流程")  # 场景名称
    @allure.title("产品定义信息中新增一条数据，新增后点击复制成功")  # 用例名称
    @allure.description("进入出货国家流程，点击新增，新增页面选择品牌后，在产品定义信息中新增一条数据，新增后点击复制，查看是会出现一条相同的数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_005(self, drivers):
        user = ShippingCountryFlow(drivers)
        querytime = datetime.now().strftime('%Y-%m-%d')
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_add_item_info('品牌', 'Infinix')
        user.input_add_item_info('项目', '项目名称测试复制')
        user.click_add()
        user.input_product_definition_info('全球版本', 'SMART')
        user.input_product_definition_info('市场名称', '市场名称测试复制')
        user.input_product_definition_info('项目名称', '项目名称测试复制')
        user.input_product_definition_info('MEMORY', '256+12')
        user.input_product_definition_info('BAND STRATEGY', '拉美BOM')
        user.input_product_definition_info('项目经理', '李小素')
        user.input_product_definition_info('摄像头', '摄像头')
        user.input_product_definition_info('型号', '型号')
        user.input_product_definition_info('新增', '新增')
        user.input_product_definition_info('再增', '2.5G')
        user.input_product_definition_info('配色', '魅海蓝/Aqua Blue')
        user.input_product_definition_info('尺寸', '64M+13M+2M')
        user.input_product_definition_info('首单量产时间', querytime)
        user.click_product_definition_confirm()
        user.click_product_definition_copy()
        user.assert_toast('复制产品成功！')
        user.assert_copy_success('项目名称测试复制')

    @allure.story("创建流程")  # 场景名称
    @allure.title("产品定义信息中新增一条数据，删除成功")  # 用例名称
    @allure.description("进入出货国家流程，点击新增，新增页面选择品牌后，在产品定义信息中，新增多条数据，新增后选择一条进行删除，删除时会弹出提示框“确定删除吗?”，点击确定，该条数据会被删除，页面上不存在该条数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_006(self, drivers):
        user = ShippingCountryFlow(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_add_item_info('品牌', 'Infinix')
        user.input_add_item_info('项目', '项目名称测试删除')
        user.click_add()
        user.input_product_definition_info('全球版本', 'SMART')
        user.input_product_definition_info('市场名称', '市场名称测试删除')
        user.input_product_definition_info('项目名称', '项目名称测试删除')
        user.input_product_definition_info('MEMORY', '256+12')
        user.input_product_definition_info('BAND STRATEGY', '拉美BOM')
        user.click_product_definition_confirm()
        user.click_product_definition_delete()
        DomAssert(drivers).assert_att('确定删除吗?')
        user.click_dialog_confirm()
        DomAssert(drivers).assert_att('暂无数据')

    @allure.story("创建流程")  # 场景名称
    @allure.title("上传附件成功")  # 用例名称
    @allure.description("进入出货国家流程，点击新增，新增页面所有内容正确填写，点击附件，并且进行选择一个文件上传，能上传成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_007(self, drivers):
        user = ShippingCountryFlow(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_add_item_info('品牌', 'Infinix')
        user.input_add_item_info('项目', '项目名称测试复制')
        user.add_upload_file('检查结果.PNG')
        user.assert_upload('检查结果.PNG')


@allure.feature("出货国家-出货国家流程")  # 模块名称
class TestTheProcessOfExaminationAndApproval:
    @allure.story("流程审批")  # 场景名称
    @allure.title("产品部管理员审核成功")  # 用例名称
    @allure.description("出货国家：产品部管理员审核,点击同意，提示请求成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_001(self, drivers, SaleCountry_API):
        user = ShippingCountryFlow(drivers)
        user.refresh_webpage()
        user.assert_my_todo_node(SaleCountry_API[0], '产品部管理员审核', True)
        user.enter_oneworks_edit(SaleCountry_API[0])
        user.assert_OneWorks_AgreeFlow()
        user.assert_my_todo_node(SaleCountry_API[0], '产品部汇签', True)

    @allure.story("流程审批")  # 场景名称
    @allure.title("产品部汇签审核成功")  # 用例名称
    @allure.description("出货国家：产品部汇签,点击同意，提示请求成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_002(self, drivers, SaleCountry_Audit_API):
        user = ShippingCountryFlow(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(SaleCountry_Audit_API[0])
        user.assert_OneWorks_AgreeFlow()
        user.assert_my_todo_node(SaleCountry_Audit_API[0], '产品经理修改', True)

    @allure.story("流程审批")  # 场景名称
    @allure.title("产品经理修改审核成功")  # 用例名称
    @allure.description("出货国家：产品经理修改, 产品定义信息：点击编辑，修改信息后，点击确定，点击同意")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_003(self, drivers, SaleCountry_Join_API):
        user = ShippingCountryFlow(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(SaleCountry_Join_API[0])
        user.click_product_definition_edit()
        querytime2 = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        querytime = datetime.now().strftime('%Y-%m-%d')
        user.input_product_definition_info('全球版本', 'HOT')
        user.input_product_definition_info('市场名称', f'市场名称{querytime2}')
        user.input_product_definition_info('项目名称', f'项目名称{querytime2}')
        user.input_product_definition_info('MEMORY', '512+8')
        user.input_product_definition_info('BAND STRATEGY', '东南亚BOM')
        user.input_product_definition_info('项目经理', '李小素')
        user.input_product_definition_info('摄像头', '摄像头test')
        user.input_product_definition_info('型号', '型号test')
        user.input_product_definition_info('新增', '新增test')
        user.input_product_definition_info('再增', '5G')
        user.input_product_definition_info('配色', '波尔多红/Bordeaux Red')
        user.input_product_definition_info('尺寸', '108M+8M+8M')
        user.input_product_definition_info('首单量产时间', querytime)
        user.click_product_definition_confirm()
        user.assert_OneWorks_AgreeFlow()
        user.assert_my_todo_node(SaleCountry_Join_API[0], '产品部管理员复核', True)

    @allure.story("流程审批")  # 场景名称
    @allure.title("产品部管理员复核审核成功")  # 用例名称
    @allure.description("出货国家：产品部管理员复核 ,点击同意，提示请求成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_004(self, drivers, SaleCountry_managerModify_API):
        user = ShippingCountryFlow(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(SaleCountry_managerModify_API[0])
        user.assert_OneWorks_AgreeFlow()
        user.assert_my_todo_node(SaleCountry_managerModify_API[0], '项目经理审批', True)

    @allure.story("流程审批")  # 场景名称
    @allure.title("项目经理审批审核成功后，流程结束，状态变为审批通过")  # 用例名称
    @allure.description("出货国家:抄送（自动抄送，不需要操作）,出货国家-出货国家流程，查看单据状态已变为审批通过")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_005(self, drivers, SaleCountry_API):
        user = ShippingCountryFlow(drivers)
        user.refresh_webpage()
        user = ShippingCountryFlow(drivers)
        user.refresh_webpage_click_menu()
        user.product_department_administrator_review(SaleCountry_API[0])
        user.product_department_sign(SaleCountry_API[0])
        user.product_manager_modification(SaleCountry_API[0])
        user.product_department_administrator_re_review(SaleCountry_API[0])
        user.enter_oneworks_edit(SaleCountry_API[0])
        user.assert_OneWorks_AgreeFlow()
        user.assert_my_application_node(SaleCountry_API[0], '抄送', True)
        sleep(60)
        user.assert_my_application_flow(SaleCountry_API[0], '审批完成')
        document_status = user.get_info(SaleCountry_API[0])[6]
        ValueAssert.value_assert_equal(document_status, '审批通过')


@allure.feature("出货国家-出货国家流程")
class TestCreateProcessExceptionScenario:
    @allure.story("创建流程异常场景")
    @allure.title("请完善项目信息！")
    @allure.description("进入出货国家流程，点击新增，新增页面选择品牌后，不填写项目名称，在产品定义信息中进行新增一条数据，点击提交，会提示“请完善项目信息！”")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_003_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        user = ShippingCountryFlow(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_add_item_info('品牌', 'Infinix')
        user.click_add_submit()
        user.assert_toast('请完善项目信息！')

    @allure.story("创建流程异常场景")
    @allure.title("产品定义信息不能为空")
    @allure.description("进入出货国家流程，点击新增，新增页面选择品牌后，填写项目名称后，不进行新增产品定义信息，点击提交，会给出提示“产品定义信息不能为空”")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_003_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        user = ShippingCountryFlow(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_add_item_info('品牌', 'Infinix')
        user.input_add_item_info('项目', '产品定义信息不能为空')
        user.click_add_submit()
        user.assert_toast('产品定义信息不能为空')

    @allure.story("创建流程异常场景")
    @allure.title("No.1行xxxxx不能为空")
    @allure.description("进入出货国家流程，点击新增，新增页面选择品牌后，填写项目名称，在产品定义信息中点击新增，其中一项内容不填写，其他内容正确填写，点击提交，给出提示No.1行xxxxx不能为空")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_003_003(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        user = ShippingCountryFlow(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_add_item_info('品牌', 'Infinix')
        user.input_add_item_info('项目', '产品定义信息不能为空')
        user.click_add()
        user.click_add_submit()
        user.assert_toast('No.1行全球版本不能为空')
        user.input_product_definition_info('全球版本', 'SMART')
        user.click_add_submit()
        DomAssert(drivers).assert_att('No.1行市场名称不能为空')
        user.input_product_definition_info('市场名称', '市场名称测试删除')
        user.click_add_submit()
        DomAssert(drivers).assert_att('No.1行项目名称不能为空')
        user.input_product_definition_info('项目名称', '项目名称测试删除')
        user.click_add_submit()
        DomAssert(drivers).assert_att('No.1行MEMORY不能为空')
        user.input_product_definition_info('MEMORY', '256+12')
        user.click_add_submit()
        DomAssert(drivers).assert_att('No.1行BAND STRATEGY不能为空')

    @allure.story("创建流程异常场景")
    @allure.title("汇签人不能为空")
    @allure.description("进入出货国家流程，点击新增，所有内容都正确填写，汇签人员进行全部删除，点击提交，会给出提示“汇签人不能为空”")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_003_004(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        user = ShippingCountryFlow(drivers)
        querytime = datetime.now().strftime('%Y-%m-%d')
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_add_item_info('品牌', 'Infinix')
        user.input_add_item_info('项目', '汇签人不能为空')
        user.click_add()
        user.input_product_definition_info('全球版本', 'SMART')
        user.input_product_definition_info('市场名称', '汇签人不能为空')
        user.input_product_definition_info('项目名称', '汇签人不能为空')
        user.input_product_definition_info('MEMORY', '256+12')
        user.input_product_definition_info('BAND STRATEGY', '拉美BOM')
        user.input_product_definition_info('项目经理', '李小素')
        user.input_product_definition_info('摄像头', '摄像头')
        user.input_product_definition_info('型号', '型号')
        user.input_product_definition_info('新增', '新增')
        user.input_product_definition_info('再增', '2.5G')
        user.input_product_definition_info('配色', '魅海蓝/Aqua Blue')
        user.input_product_definition_info('尺寸', '64M+13M+2M')
        user.input_product_definition_info('首单量产时间', querytime)
        user.click_product_definition_confirm()
        user.clear_member('汇签人员')
        user.click_add_submit()
        user.assert_toast('汇签人不能为空')

    @allure.story("创建流程异常场景")
    @allure.title("抄送人不能为空")
    @allure.description("进入出货国家流程，点击新增，所有内容都正确填写，汇签人员进行全部删除，点击提交，会给出提示“抄送人不能为空”")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.UT
    def test_003_005(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        user = ShippingCountryFlow(drivers)
        querytime = datetime.now().strftime('%Y-%m-%d')
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_add_item_info('品牌', 'Infinix')
        user.input_add_item_info('项目', '抄送人不能为空')
        user.click_add()
        user.input_product_definition_info('全球版本', 'SMART')
        user.input_product_definition_info('市场名称', '抄送人不能为空')
        user.input_product_definition_info('项目名称', '抄送人不能为空')
        user.input_product_definition_info('MEMORY', '256+12')
        user.input_product_definition_info('BAND STRATEGY', '拉美BOM')
        user.input_product_definition_info('项目经理', '李小素')
        user.input_product_definition_info('摄像头', '摄像头')
        user.input_product_definition_info('型号', '型号')
        user.input_product_definition_info('新增', '新增')
        user.input_product_definition_info('再增', '2.5G')
        user.input_product_definition_info('配色', '魅海蓝/Aqua Blue')
        user.input_product_definition_info('尺寸', '64M+13M+2M')
        user.input_product_definition_info('首单量产时间', querytime)
        user.click_product_definition_confirm()
        user.clear_member('抄送人员')
        user.click_add_submit()
        user.assert_toast('抄送人不能为空')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("第2行与第1行产品重复！")  # 用例名称
    @allure.description("进入出货国家流程，点击新增，所有内容都正确填写，将已经填写好的产品定义信息再复制一行，直接提交，会给出提示“第2行与第1行产品重复！”")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_003_006(self, drivers):
        user = ShippingCountryFlow(drivers)
        querytime = datetime.now().strftime('%Y-%m-%d')
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_add_item_info('品牌', 'Infinix')
        user.input_add_item_info('项目', '项目名称测试复制')
        user.click_add()
        user.input_product_definition_info('全球版本', 'SMART')
        user.input_product_definition_info('市场名称', '市场名称测试复制')
        user.input_product_definition_info('项目名称', '项目名称测试复制')
        user.input_product_definition_info('MEMORY', '256+12')
        user.input_product_definition_info('BAND STRATEGY', '拉美BOM')
        user.input_product_definition_info('项目经理', '李小素')
        user.input_product_definition_info('摄像头', '摄像头')
        user.input_product_definition_info('型号', '型号')
        user.input_product_definition_info('新增', '新增')
        user.input_product_definition_info('再增', '2.5G')
        user.input_product_definition_info('配色', '魅海蓝/Aqua Blue')
        user.input_product_definition_info('尺寸', '64M+13M+2M')
        user.input_product_definition_info('首单量产时间', querytime)
        user.click_product_definition_confirm()
        user.click_product_definition_copy()
        user.select_signatory('汇签人员', '李小素')
        user.click_add_submit()
        user.assert_toast('第2行与第1行产品重复！')

    @allure.story("创建流程异常场景")  # 场景名称
    @allure.title("产品定义信息不能为空")  # 用例名称
    @allure.description("进入出货国家流程，点击新增，新增后产品定义信息不进行新增，直接点击提交，会给出提示“产品定义信息不能为空”")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_003_007(self, drivers):
        user = ShippingCountryFlow(drivers)
        user.refresh_webpage_click_menu()
        user.click_add()
        user.input_add_item_info('品牌', 'Infinix')
        user.input_add_item_info('项目', '项目名称测试复制')
        user.select_signatory('汇签人员', '李小素')
        user.click_add_submit()
        user.assert_toast('产品定义信息不能为空')


if __name__ == '__main__':
    pytest.main(['ShippingCountry_ShippingCountryFlow.py'])
