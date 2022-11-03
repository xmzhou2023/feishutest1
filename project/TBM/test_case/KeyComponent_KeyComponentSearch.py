import allure
import pytest

from libs.common.time_ui import sleep
from project.TBM.page_object.KeyComponent_KeyComponentSearch import KeyComponentsSearch
from public.base.assert_ui import *

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""


@allure.feature("关键器件-关键器件查询") # 模块名称
class TestCreateProcess:
    @allure.story("创建流程")  # 场景名称
    @allure.title("进入关键器件修订发起页面,查看关键器件-业务审核-维护关键器件显示是否正确")  # 用例名称
    @allure.description("进入关键器件修订发起页面，查看业务审核中维护关键器件部分的内容是否正确（例如摄像头+闪光灯，硬件电子料-基带）")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):
        user = KeyComponentsSearch(drivers)
        user.refresh_webpage_click_menu()
        user.click_operate('50A710U', '修订')
        user.click_key('摄像头+闪光灯')
        user.click_revise_comfirm()
        user.assert_review('摄像头+闪光灯')
        user.assert_review('硬件电子料-基带', False)
        user.refresh_webpage_click_menu()
        user.click_operate('50A710U', '修订')
        user.click_key('硬件电子料-基带')
        user.click_revise_comfirm()
        user.assert_review('摄像头+闪光灯', False)
        user.assert_review('硬件电子料-基带')
        user.refresh_webpage_click_menu()
        user.click_operate('50A710U', '修订')
        user.click_key('摄像头+闪光灯')
        user.click_key('硬件电子料-基带')
        user.click_revise_comfirm()
        user.assert_review('摄像头+闪光灯')
        user.assert_review('硬件电子料-基带')

    @allure.story("创建流程")  # 场景名称
    @allure.title("关键器件修订发起成功")  # 用例名称
    @allure.description("进入关键器件修订发起页面，选择业务审核中维护关键器件部分的人员为多个人，发起成功")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):
        user = KeyComponentsSearch(drivers)
        user.refresh_webpage_click_menu()
        user.click_operate('50A710U', '修订')
        user.click_key('请勾选需要处理的分类')
        user.click_revise_comfirm()
        user.select_business_review('陈月', '硬件电子料-基带')
        user.click_add_submit()
        user.assert_toast()
        process_code = user.get_info()[1]
        user.delete_flow(process_code)


@allure.feature("关键器件-关键器件查询")
class TestCreateProcessExceptionScenario:
    @allure.story("创建流程异常场景")
    @allure.title("请勿重复维护关键器件角色！")  # 用例名称
    @allure.description("进入关键器件修订发起页面，选择业务审核中维护关键器件部分的人员为同一个人，点击提交，提示请勿重复维护关键器件角色！")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_001(self, drivers):
        user = KeyComponentsSearch(drivers)
        user.refresh_webpage_click_menu()
        user.click_operate('50A710U', '修订')
        user.click_key('摄像头+闪光灯')
        user.click_key('硬件电子料-基带')
        user.click_revise_comfirm()
        user.click_add_submit()
        user.assert_toast('请勿重复维护关键器件角色！')


@allure.feature("关键器件-关键器件流程")  # 模块名称
class TestTheProcessOfExaminationAndApproval:
    @allure.story("流程审批")  # 场景名称
    @allure.title("摄像头+闪光灯节点，审批成功")  # 用例名称
    @allure.description("摄像头+闪光灯节点，关键器件中的摄像头+闪光灯节点，点击左侧三角，点击下面的模块，点击物料编码右侧的加号，物料编码下面出现一行，点击新出现这行的加号，填写代申请编码信息，点击其他模块保存成功（像这样随便填几个模块），点击同意，提示操作成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_001(self, drivers, KeyDevice_Revise_API):
        user = KeyComponentsSearch(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(KeyDevice_Revise_API[0], '摄像头+闪光灯')
        user.click_onework_unfold('摄像头+闪光灯')
        user.click_onework_module('CTP')
        user.click_onework_code_add()
        user.click_onework_material_add('CTP(1供)')
        user.click_onework_material_pending_code('CTP(1供)')
        user.input_onework_material_details('物料属性', '属性test')
        user.scroll_onework_material_param()
        user.input_onework_material_parameter('技术类型', 'GFF', False)
        user.input_onework_material_parameter('CG颜色', 'CG颜色test')
        user.input_onework_material_parameter('接口类型', '接口类型test')
        user.input_onework_material_parameter('连接方式', '焊接', False)
        user.click_oneworks_agree()
        user.click_oneworks_confirm()
        user.assert_toast()
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("硬件电子料-基带节点，审批成功")  # 用例名称
    @allure.description("硬件电子料-基带节点，关键器件中的硬件电子料-基带节点，点击左侧三角，点击下面的模块，点击物料编码右侧的加号，物料编码下面出现一行，点击新出现这行的加号，填写代申请编码信息，点击其他模块保存成功（像这样随便填几个模块），点击同意，提示操作成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_002(self, drivers, KeyDevice_Revise_API):
        user = KeyComponentsSearch(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(KeyDevice_Revise_API[0], '硬件电子料-基带')
        user.click_onework_unfold('硬件电子料-基带')
        user.click_onework_module('CPU')
        user.click_onework_code_add()
        user.click_onework_material_add('CPU(1供)')
        user.click_onework_material_pending_code('CPU(1供)')
        user.input_onework_material_details('物料属性', '属性test')
        user.click_oneworks_agree()
        user.click_oneworks_confirm()
        user.assert_toast()
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("标准化代表节点，审批成功")  # 用例名称
    @allure.description("标准化代表节点，找到标准化评估责任人，点击左侧全选，点击右侧一键填写，弹出一键填写框，字段名称选择责任人，责任人选择xxx，点击确定，提示已选分类的审批人设置成功，点击关闭按钮，弹框关闭，点击同意，提示操作成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_003(self, drivers, KeyDevice_Revise_nodeMat_API):
        user = KeyComponentsSearch(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(KeyDevice_Revise_nodeMat_API[0], '标准化代表')
        user.click_onework_checkbox()
        user.click_onework_onepress()
        user.input_onework_onepress('责任人', '李小素')
        user.click_onework_onepress_confirm()
        user.click_onework_onepress_cancel()
        user.click_oneworks_agree()
        user.click_oneworks_confirm()
        user.assert_toast()
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("采购代表节点，审批成功")  # 用例名称
    @allure.description("采购代表节点，找到采购评估责任人，点击左侧全选，点击右侧一键填写，弹出一键填写框，字段名称选择资源商务，责任人选择xxx，点击确定，提示已选分类的审批人设置成功；字段名称选择采购执行，责任人选择xxx，点击确定，提示已选分类的审批人设置成功；字段名称选择采购PTC，责任人选择xxx，点击确定，提示已选分类的审批人设置成功；字段名称选择采购SQM，责任人选择xxx，点击确定。提示已选分类的审批人设置成功，点击关闭按钮，弹框关闭，点击同意，提示操作成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_004(self, drivers, KeyDevice_Revise_nodeMat_API):
        user = KeyComponentsSearch(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(KeyDevice_Revise_nodeMat_API[0], '采购代表')
        user.click_onework_checkbox()
        user.click_onework_onepress()
        user.input_onework_onepress('资源商务', '李小素')
        user.click_onework_onepress_confirm()
        DomAssert(drivers).assert_att('已选分类的审批人设置成功')
        user.input_onework_onepress('采购执行', '李小素')
        user.click_onework_onepress_confirm()
        DomAssert(drivers).assert_att('已选分类的审批人设置成功')
        user.input_onework_onepress('采购PTC', '李小素')
        user.click_onework_onepress_confirm()
        DomAssert(drivers).assert_att('已选分类的审批人设置成功')
        user.input_onework_onepress('采购SQM', '李小素')
        user.click_onework_onepress_confirm()
        DomAssert(drivers).assert_att('已选分类的审批人设置成功')
        user.click_onework_onepress_cancel()
        user.click_oneworks_agree()
        user.click_oneworks_confirm()
        user.assert_toast()
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("资源商务评估节点，审批成功")  # 用例名称
    @allure.description("资源商务评估节点，（所有前面填过信息的这里都可以填采购评估-资源商务）勾选是否新供应商、国产化属性、供应商选择原因类别、是否客供物料、价格趋势（6个月）、是否NUDD、评审结论（选通过或者选建议修改，填原因及修改建议），填写供应商选择原因、份额（只能输数字1-100）、关联物料（只能填物料）、NUDD说明、NUDD管理方案、原因及修改建议；点击同意，有必填不填时有提示，点击确定")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_005(self, drivers, KeyDevice_Revise_Approver_API):
        user = KeyComponentsSearch(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(KeyDevice_Revise_Approver_API[0], '资源商务评估')
        user.click_onework_unfold('摄像头+闪光灯')
        user.click_onework_module('CTP')
        user.click_onework_material_pending_code('CTP(1供)')
        user.input_onework_procurement_evaluation('供应商名称', 'TEST', False)
        user.input_onework_procurement_evaluation('是否新供应商', '否', False)
        user.input_onework_procurement_evaluation('国产化属性', '0', False)
        user.input_onework_procurement_evaluation('供应商选择原因类别', '成本因素', False)
        user.input_onework_procurement_evaluation('供应商选择原因', '供应商选择原因TEST')
        user.input_onework_procurement_evaluation('份额', '50')
        user.input_onework_procurement_evaluation('是否客供物料', '是', False)
        user.input_onework_procurement_evaluation('价格趋势（6个月）', '持平', False)
        user.input_onework_procurement_evaluation('是否NUDD', '是', False)
        user.input_onework_procurement_evaluation('NUDD说明', 'NUDD说明TEST')
        user.input_onework_procurement_evaluation('NUDD管理方案', 'NUDD管理方案TEST')
        user.input_onework_procurement_evaluation('评审结论', '通过', False)
        user.input_onework_procurement_evaluation('原因及修改建议', '原因及修改建议TEST')
        user.click_onework_unfold('硬件电子料-基带')
        user.click_onework_module('CPU')
        user.click_onework_material_pending_code('CPU(1供)')
        user.input_onework_procurement_evaluation('供应商名称', 'TEST', False)
        user.input_onework_procurement_evaluation('是否新供应商', '否', False)
        user.input_onework_procurement_evaluation('国产化属性', '0', False)
        user.input_onework_procurement_evaluation('供应商选择原因类别', '成本因素', False)
        user.input_onework_procurement_evaluation('供应商选择原因', '供应商选择原因TEST')
        user.input_onework_procurement_evaluation('份额', '50')
        user.input_onework_procurement_evaluation('是否客供物料', '是', False)
        user.input_onework_procurement_evaluation('价格趋势（6个月）', '持平', False)
        user.input_onework_procurement_evaluation('是否NUDD', '是', False)
        user.input_onework_procurement_evaluation('NUDD说明', 'NUDD说明TEST')
        user.input_onework_procurement_evaluation('NUDD管理方案', 'NUDD管理方案TEST')
        user.input_onework_procurement_evaluation('评审结论', '通过', False)
        user.input_onework_procurement_evaluation('原因及修改建议', '原因及修改建议TEST')
        user.click_oneworks_agree()
        user.click_oneworks_confirm()
        user.assert_toast()
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("采购执行评估节点，审批成功")  # 用例名称
    @allure.description("采购执行评估节点，（所有前面填过信息的这里都可以填采购评估-采购执行）勾选产能评审结论（选通过或者选建议修改，填原因及修改建议），填写L/T(天)、最小下单量(pcs)、此项目峰值需求(K/M)、供应商总产能(K/M)、分配传音产能(K/M)、供应弹性(%)、共用项目需求合计(K/M)、此项目产能分配(""K/M)、共用项目名、原因及修改建议、备料建议，点击同意，有必填不填时有提示，点击确定")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_006(self, drivers, KeyDevice_Revise_Approver_API):
        user = KeyComponentsSearch(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(KeyDevice_Revise_Approver_API[0], '采购执行评估')
        user.click_onework_unfold('摄像头+闪光灯')
        user.click_onework_module('CTP')
        user.click_onework_material_pending_code('CTP(1供)')
        user.scroll_onework_material_details('采购执行')
        user.input_onework_procurement_execution('L/T(天)', '1')
        user.input_onework_procurement_execution('最小下单量(pcs)', '1')
        user.input_onework_procurement_execution('此项目峰值需求(K/M)', '1')
        user.input_onework_procurement_execution('供应商总产能(K/M)', '1')
        user.input_onework_procurement_execution('分配传音产能(K/M)', '1')
        user.input_onework_procurement_execution('供应弹性(%)', '1')
        user.input_onework_procurement_execution('共用项目需求合计(K/M)', '1')
        user.input_onework_procurement_execution('此项目产能分配(K/M)', '1')
        user.input_onework_procurement_execution('共用项目名', '共用项目名test')
        user.input_onework_procurement_execution('产能评审结论', '通过', False)
        user.input_onework_procurement_execution('原因及修改建议', '原因及修改建议test')
        user.input_onework_procurement_execution('备料建议', '备料建议test')
        user.click_onework_unfold('硬件电子料-基带')
        user.click_onework_module('CPU')
        user.click_onework_material_pending_code('CPU(1供)')
        user.scroll_onework_material_details('采购执行')
        user.input_onework_procurement_execution('L/T(天)', '1')
        user.input_onework_procurement_execution('最小下单量(pcs)', '1')
        user.input_onework_procurement_execution('此项目峰值需求(K/M)', '1')
        user.input_onework_procurement_execution('供应商总产能(K/M)', '1')
        user.input_onework_procurement_execution('分配传音产能(K/M)', '1')
        user.input_onework_procurement_execution('供应弹性(%)', '1')
        user.input_onework_procurement_execution('共用项目需求合计(K/M)', '1')
        user.input_onework_procurement_execution('此项目产能分配(K/M)', '1')
        user.input_onework_procurement_execution('共用项目名', '共用项目名test')
        user.input_onework_procurement_execution('产能评审结论', '通过', False)
        user.input_onework_procurement_execution('原因及修改建议', '原因及修改建议test')
        user.input_onework_procurement_execution('备料建议', '备料建议test')
        user.click_oneworks_agree()
        user.click_oneworks_confirm()
        user.assert_toast()
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("采购PTC评估节点，审批成功")  # 用例名称
    @allure.description("采购PTC评估节点，（所有前面填过信息的这里都可以填采购评估-PTC）勾选评审结论（选通过或者选不同意，填原因及修改建议），填写原因及修改建议，，点击同意，有必填不填时有提示，点击确定")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_007(self, drivers, KeyDevice_Revise_Approver_API):
        user = KeyComponentsSearch(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(KeyDevice_Revise_Approver_API[0], '采购PTC评估')
        user.click_onework_unfold('摄像头+闪光灯')
        user.click_onework_module('CTP')
        user.click_onework_material_pending_code('CTP(1供)')
        user.scroll_onework_material_details('PTC')
        user.input_onework_ptc('评审结论', '同意')
        user.input_onework_ptc('原因及修改建议', '原因及修改建议test')
        user.click_onework_unfold('硬件电子料-基带')
        user.click_onework_module('CPU')
        user.click_onework_material_pending_code('CPU(1供)')
        user.scroll_onework_material_details('PTC')
        user.input_onework_ptc('评审结论', '同意')
        user.input_onework_ptc('原因及修改建议', '原因及修改建议test')
        user.click_oneworks_agree()
        user.click_oneworks_confirm()
        user.assert_toast()
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("采购SQM评估节点，审批成功")  # 用例名称
    @allure.description("采购SQM评估节点，（所有前面填过信息的这里都可以填采购评估-SQM）勾选评审结论（选通过或者选不同意，填原因及修改建议），填写原因及修改建议，点击同意，有必填不填时有提示，点击确定")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.UT  # 用例标记
    def test_002_008(self, drivers, KeyDevice_Revise_Approver_API):
        user = KeyComponentsSearch(drivers)
        user.refresh_webpage()
        user.enter_oneworks_edit(KeyDevice_Revise_Approver_API[0], '采购SQM评估')
        user.click_onework_unfold('摄像头+闪光灯')
        user.click_onework_module('CTP')
        user.click_onework_material_pending_code('CTP(1供)')
        user.scroll_onework_material_details('SQM')
        user.input_onework_sqm('评审结论', '同意')
        user.input_onework_sqm('原因及修改建议', '原因及修改建议test')
        user.click_onework_unfold('硬件电子料-基带')
        user.click_onework_module('CPU')
        user.click_onework_material_pending_code('CPU(1供)')
        user.scroll_onework_material_details('SQM')
        user.input_onework_sqm('评审结论', '同意')
        user.input_onework_sqm('原因及修改建议', '原因及修改建议test')
        user.click_oneworks_agree()
        user.click_oneworks_confirm()
        user.assert_toast()
        user.quit_oneworks()

    @allure.story("流程审批")  # 场景名称
    @allure.title("标准化部评估节点，审批成功后可以再次发起修订流程")  # 用例名称
    @allure.description("关键器件-关键器件流程，查看单据状态已变为审批通过，可以再次点击修订勾选几个（例如摄像头+闪光灯，硬件电子料-基带），发起修订流程")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_009(self, drivers, KeyDevice_Revise_API):
        user = KeyComponentsSearch(drivers)
        user.refresh_webpage()
        user.KD_image(KeyDevice_Revise_API[0])
        user.KD_hardware(KeyDevice_Revise_API[0])
        user.KD_standard(KeyDevice_Revise_API[0])
        user.KD_purchase(KeyDevice_Revise_API[0])
        user.KD_Resources(KeyDevice_Revise_API[0])
        user.KD_Executive(KeyDevice_Revise_API[0])
        user.KD_PTC(KeyDevice_Revise_API[0])
        user.KD_SQM(KeyDevice_Revise_API[0])
        user.KD_standard_evaluation(KeyDevice_Revise_API[0])
        user.assert_my_application_node(KeyDevice_Revise_API[0], '审批抄送', True)
        sleep(60)
        user.assert_my_application_flow(KeyDevice_Revise_API[0], '审批完成')
        document_status = user.get_info()[5]
        ValueAssert.value_assert_equal(document_status, '审批通过')
        user.refresh_webpage_click_menu()
        user.click_operate('50A710U', '修订')
        user.click_key('请勾选需要处理的分类')
        user.click_revise_comfirm()
        user.select_business_review('陈月', '硬件电子料-基带')
        user.click_add_submit()
        user.assert_toast()
        process_code = user.get_info()[1]
        user.delete_flow(process_code)
if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
