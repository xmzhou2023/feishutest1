import pytest

from project.TBM.api.api import APIRequest
from public.data.unified_login.unified import *
from public.base.assert_ui import *
from public.libs.unified_login.login import Login
from libs.common.read_config import *

pro_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture(scope='session', autouse=True)
def __init__(drivers, env_name):
    """初始化"""
    global pro_env
    pro_env = env_name
    logging.info("【{}】项目【{}】环境- UI自动化开始执行".format(pro_name, pro_env))
    ini = ReadConfig(pro_name, pro_env)

    """使用统一登录"""
    logging.info("前置条件：传音统一登录开始")
    user = Login(drivers)
    user.IPM_login(drivers, ini.url, account[2]['usernum'], account[2]['passwd'])
    DomAssert(drivers).assert_exact_att('首页')
    logging.info("前置条件：传音统一登录成功")


@pytest.fixture(scope='function', autouse=False)
def BarePhone_API():
    logging.info('开始前置操作')
    user = APIRequest()
    api_response = user.API_BarePhone_Add()
    yield api_response
    logging.info('开始后置操作')
    user.API_Bom_Delete(api_response[1], api_response[2])


@pytest.fixture(scope='function', autouse=False)
def BarePhone_Factory_API():
    logging.info('开始前置操作-新建流程-补充工厂审批同意')
    user = APIRequest()
    api_response = user.API_BarePhone_Add()
    user.API_BarePhone_Factory(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_Bom_Delete(api_response[1], api_response[2])


@pytest.fixture(scope='function', autouse=False)
def BarePhone_StructureEnginner_API():
    logging.info('开始前置操作-新建流程-结构工程师审批同意')
    user = APIRequest()
    api_response = user.API_BarePhone_Add()
    user.API_BarePhone_StructureEnginner(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_Bom_Delete(api_response[1], api_response[2])


@pytest.fixture(scope='function', autouse=False)
def BarePhone_Approval_API():
    logging.info('开始前置操作-新建流程-业务审核审批同意')
    user = APIRequest()
    api_response = user.API_BarePhone_Add()
    user.API_BarePhone_Approval(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_Bom_Delete(api_response[1], api_response[2])


@pytest.fixture(scope='function', autouse=False)
def BarePhone_Approval_Fail_API():
    logging.info('开始前置操作-新建流程-业务审核审批同意')
    user = APIRequest()
    api_response = user.API_BarePhone_Fail_Add()
    user.API_BarePhone_Approval(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_Bom_Delete(api_response[1], api_response[2])


@pytest.fixture(scope='function', autouse=False)
def BarePhone_bomEnginner_API():
    logging.info('开始前置操作-新建流程-BOM工程师审批同意')
    user = APIRequest()
    api_response = user.API_BarePhone_Add()
    user.API_BarePhone_bomEnginner(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_Bom_Delete(api_response[1], api_response[2])


@pytest.fixture(scope='function', autouse=False)
def BarePhone_bomEnginner_Fail_API():
    logging.info('开始前置操作-新建流程-BOM工程师审批同意')
    user = APIRequest()
    api_response = user.API_BarePhone_Fail_Add()
    user.API_BarePhone_bomEnginner(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_Bom_Delete(api_response[1], api_response[2])


@pytest.fixture(scope='function', autouse=False)
def Machine_API():
    logging.info('开始前置操作')
    user = APIRequest()
    api_response = user.API_Machine_Add()
    yield api_response
    logging.info('开始后置操作')
    user.API_Bom_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def Machine_Derive_API():
    logging.info('开始前置操作')
    user = APIRequest()
    api_response = user.API_Derive_Machine_Add()
    yield api_response
    logging.info('开始后置操作')
    user.API_Bom_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def Machine_Factory_API():
    logging.info('开始前置操作-新建流程-补充工厂审批同意')
    user = APIRequest()
    api_response = user.API_Machine_Add()
    user.API_Machine_Factory(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_Bom_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def Machine_Derive_Factory_API():
    logging.info('开始前置操作-新建流程-补充工厂审批同意')
    user = APIRequest()
    api_response = user.API_Derive_Machine_Add()
    user.API_Derive_Machine_Factory(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_Bom_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def Machine_bomEnginner_API():
    logging.info('开始前置操作-新建流程-BOM工程师审批审批同意')
    user = APIRequest()
    api_response = user.API_Machine_Add()
    user.API_Machine_bomEnginner(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_Bom_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def Machine_Derive_bomEnginner_API():
    logging.info('开始前置操作-新建流程-BOM工程师审批审批同意')
    user = APIRequest()
    api_response = user.API_Derive_Machine_Add()
    user.API_Derive_Machine_bomEnginner(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_Bom_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def Machine_Approval_API():
    logging.info('开始前置操作-新建流程-业务审核审批同意')
    user = APIRequest()
    api_response = user.API_Machine_Add()
    user.API_Machine_Approval(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_Bom_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def Machine_Derive_Approval_API():
    logging.info('开始前置操作-新建流程-业务审核审批同意')
    user = APIRequest()
    api_response = user.API_Derive_Machine_Add()
    user.API_Derive_Machine_Approval(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_Bom_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def KeyDevice_API():
    logging.info('开始前置操作')
    user = APIRequest()
    api_response = user.API_KeyDevice_Add()
    yield api_response
    logging.info('开始后置操作')
    user.API_KeyDevice_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def KeyDevice_Revise_API():
    logging.info('开始前置操作')
    user = APIRequest()
    api_response = user.API_KeyDevice_Revise()
    yield api_response
    logging.info('开始后置操作')
    user.API_KeyDevice_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def KeyDevice_Revise_nodeMat_API():
    logging.info('开始前置操作-nodeMat审批')
    user = APIRequest()
    api_response = user.API_KeyDevice_Revise()
    user.API_KeyDevice_image(api_response[0], api_response[1], api_response[2])
    user.API_KeyDevice_hardware(api_response[0], api_response[1], api_response[2], username='18651509')
    yield api_response
    logging.info('开始后置操作')
    user.API_KeyDevice_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def KeyDevice_nodeMat_API():
    logging.info('开始前置操作-nodeMat审批')
    user = APIRequest()
    api_response = user.API_KeyDevice_Add()
    user.API_KeyDevice_image(api_response[0], api_response[1], api_response[2])
    user.API_KeyDevice_hardware(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_KeyDevice_Delete(api_response[1], api_response[2])


@pytest.fixture(scope='function', autouse=False)
def KeyDevice_Approver_API():
    logging.info('开始前置操作-代表审批')
    user = APIRequest()
    api_response = user.API_KeyDevice_Add()
    user.API_KeyDevice_image(api_response[0], api_response[1], api_response[2])
    user.API_KeyDevice_hardware(api_response[0], api_response[1], api_response[2])
    user.API_KeyDevice_StandardDeputy(api_response[0], api_response[1], api_response[2])
    user.API_KeyDevice_PurchaseDeputy(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_KeyDevice_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def KeyDevice_Revise_Approver_API():
    logging.info('开始前置操作-代表审批')
    user = APIRequest()
    api_response = user.API_KeyDevice_Revise()
    user.API_KeyDevice_image(api_response[0], api_response[1], api_response[2])
    user.API_KeyDevice_hardware(api_response[0], api_response[1], api_response[2], username='18651509')
    user.API_KeyDevice_StandardDeputy(api_response[0], api_response[1], api_response[2])
    user.API_KeyDevice_PurchaseDeputy(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_KeyDevice_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def SaleCountry_API():
    logging.info('开始前置操作')
    user = APIRequest()
    api_response = user.API_SaleCountry_Add()
    yield api_response
    logging.info('开始后置操作')
    user.API_SaleCountry_Delete(api_response[1], api_response[2])


@pytest.fixture(scope='function', autouse=False)
def SaleCountry_Audit_API():
    logging.info('开始前置操作-产品部管理员审核同意')
    user = APIRequest()
    api_response = user.API_SaleCountry_Add()
    user.API_Change_Audit(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_SaleCountry_Delete(api_response[1], api_response[2])


@pytest.fixture(scope='function', autouse=False)
def SaleCountry_Join_API():
    logging.info('开始前置操作-产品部汇签同意')
    user = APIRequest()
    api_response = user.API_SaleCountry_Add()
    user.API_Change_Join(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_SaleCountry_Delete(api_response[1], api_response[2])


@pytest.fixture(scope='function', autouse=False)
def SaleCountry_managerModify_API():
    logging.info('开始前置操作-产品经理修改同意')
    user = APIRequest()
    api_response = user.API_SaleCountry_Add()
    user.API_Change_managerModify(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_SaleCountry_Delete(api_response[1], api_response[2])


@pytest.fixture(scope='function', autouse=False)
def SaleCountry_ProductChange_API():
    logging.info('开始前置操作-变更产品')
    user = APIRequest()
    api_response = user.API_Change_Product('出货国家查询变更产品部分流程')
    yield api_response
    logging.info('开始后置操作')
    user.API_SaleCountry_Delete(api_response[1], api_response[2])


@pytest.fixture(scope='function', autouse=False)
def SaleCountry_CountryChange_API():
    logging.info('开始前置操作-变更国家')
    user = APIRequest()
    api_response = user.API_Change_Country('项目名称test2023-01-30-15:23:43')
    yield api_response
    logging.info('开始后置操作')
    user.API_SaleCountry_Delete(api_response[1], api_response[2])


@pytest.fixture(scope='function', autouse=False)
def SaleCountry_ProductChange_All_API():
    logging.info('开始前置操作-变更产品')
    user = APIRequest()
    api_response = user.API_Change_Product('出货国家查询-变更产品自动化全流程测试')
    yield api_response
    logging.info('开始后置操作')
    user.API_SaleCountry_Delete(api_response[1], api_response[2])


@pytest.fixture(scope='function', autouse=False)
def SaleCountry_ProductChange_Audit_API():
    logging.info('开始前置操作-变更产品-产品部管理员审核同意')
    user = APIRequest()
    api_response = user.API_Change_Product('出货国家查询变更产品部分流程')
    user.API_Change_Audit(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_SaleCountry_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def SaleCountry_CountryChange_Audit_API():
    logging.info('开始前置操作-变更国家-产品部管理员审核同意')
    user = APIRequest()
    api_response = user.API_Change_Country('项目名称test2023-01-30-15:23:43')
    user.API_Change_Audit(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_SaleCountry_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def SaleCountry_ProductChange_Join_API():
    logging.info('开始前置操作-变更产品-产品部汇签同意')
    user = APIRequest()
    api_response = user.API_Change_Product('出货国家查询变更产品部分流程')
    user.API_Change_Join(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_SaleCountry_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def SaleCountry_CountryChange_Join_API():
    logging.info('开始前置操作-变更国家-产品部汇签同意')
    user = APIRequest()
    api_response = user.API_Change_Country('项目名称test2023-01-30-15:23:43')
    user.API_Change_Join(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_SaleCountry_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def SaleCountry_ProductChange_managerModify_API():
    logging.info('开始前置操作-变更产品-产品经理修改同意')
    user = APIRequest()
    api_response = user.API_Change_Product('出货国家查询变更产品部分流程')
    user.API_Change_managerModify(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_SaleCountry_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def SaleCountry_CountryChange_managerModify_API():
    logging.info('开始前置操作-变更国家-产品经理修改同意')
    user = APIRequest()
    api_response = user.API_Change_Country('项目名称test2023-01-30-15:23:43')
    user.API_ChangeCountry_managerModify(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_SaleCountry_Delete(api_response[1], api_response[2])


@pytest.fixture(scope='function', autouse=False)
def KeyDevice_SQL():
    a = SQL('TBM', 'test')
    a.change_db(
        "delete from kd_flow_main  where device_bid in (select t.bid from kd_device_info t where t.brand='itel' and t.model='50A1S')"
    )
    a.change_db(
        "delete from kd_device_arch_info where brand ='itel' and model='50A1S'"
    )
    a.change_db(
        "delete from kd_device_info where brand ='itel' and model='50A1S'"
    )
    logging.info('开始：调用sql脚本修改数据库数据')
    yield
    a.change_db(
        "delete from kd_flow_main  where device_bid in (select t.bid from kd_device_info t where t.brand='itel' and t.model='50A1S')"
    )
    a.change_db(
        "delete from kd_device_arch_info where brand ='itel' and model='50A1S'"
    )
    a.change_db(
        "delete from kd_device_info where brand ='itel' and model='50A1S'"
    )
    logging.info('结束：调用sql脚本修改数据库数据')

@pytest.fixture(scope='function', autouse=False)
def KeyDevice_SQL_50A712U():
    a = SQL('TBM', 'test')
    a.change_db(
        "delete from kd_flow_main  where device_bid in (select t.bid from kd_device_info t where t.brand='itel' and t.model='50A712U')"
    )
    a.change_db(
        "delete from kd_device_arch_info where brand ='itel' and model='50A712U'"
    )
    a.change_db(
        "delete from kd_device_info where brand ='itel' and model='50A712U'"
    )
    logging.info('开始：调用sql脚本修改数据库数据')
    yield
    a.change_db(
        "delete from kd_flow_main  where device_bid in (select t.bid from kd_device_info t where t.brand='itel' and t.model='50A712U')"
    )
    a.change_db(
        "delete from kd_device_arch_info where brand ='itel' and model='50A712U'"
    )
    a.change_db(
        "delete from kd_device_info where brand ='itel' and model='50A712U'"
    )
    logging.info('结束：调用sql脚本修改数据库数据')

@pytest.fixture(scope='function', autouse=False)
def Foreign_API():
    logging.info('开始前置操作')
    user = APIRequest()
    api_response = user.API_Foreign_Add()
    yield api_response
    logging.info('开始后置操作')
    user.API_Bom_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def Foreign_Derived_API():
    logging.info('开始前置操作')
    user = APIRequest()
    api_response = user.API_Foreign_Derived_Add()
    yield api_response
    logging.info('开始后置操作')
    user.API_Bom_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def Foreign_Derived_Approval_API():
    logging.info('开始前置操作-新建流程-业务审核通过')
    user = APIRequest()
    api_response = user.API_Foreign_Derived_Add()
    user.API_Foreign_Approval(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_Bom_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def Foreign_Approval_API():
    logging.info('开始前置操作-新建流程-业务审核通过')
    user = APIRequest()
    api_response = user.API_Foreign_Add()
    user.API_Foreign_Approval(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_Bom_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def Foreign_Failed_API():
    logging.info('开始前置操作')
    user = APIRequest()
    api_response = user.API_Foreign_Failed_Add()
    user.API_Foreign_Approval(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_Bom_Delete(api_response[1], api_response[2])


@pytest.fixture(scope='function', autouse=False)
def PCBA_API():
    logging.info('开始前置操作')
    user = APIRequest()
    api_response = user.API_PCBA_Add()
    yield api_response
    logging.info('开始后置操作')
    user.API_Bom_Delete(api_response[1], api_response[2])


@pytest.fixture(scope='function', autouse=False)
def PCBA_Derived_API():
    logging.info('开始前置操作')
    user = APIRequest()
    api_response = user.API_PCBA_Derived_Add()
    yield api_response
    logging.info('开始后置操作')
    user.API_Bom_Delete(api_response[1], api_response[2])


@pytest.fixture(scope='function', autouse=False)
def PCBA_Factory_API():
    logging.info('开始前置操作-新建流程-补充工厂审批同意')
    user = APIRequest()
    api_response = user.API_PCBA_Add()
    user.API_PCBA_Factory(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_Bom_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def PCBA_Derived_Factory_API():
    logging.info('开始前置操作-新建流程-补充工厂审批同意')
    user = APIRequest()
    api_response = user.API_PCBA_Derived_Add()
    user.API_PCBA_Factory(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_Bom_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def PCBA_Structure_API():
    logging.info('开始前置操作-新建流程-基带工程师审批同意')
    user = APIRequest()
    api_response = user.API_PCBA_Add()
    user.API_PCBA_Structure(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_Bom_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def PCBA_Derived_Structure_API():
    logging.info('开始前置操作-新建流程-基带工程师审批同意')
    user = APIRequest()
    api_response = user.API_PCBA_Derived_Add()
    user.API_Derived_PCBA_Structure(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_Bom_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def PCBA_Purchase_API():
    logging.info('开始前置操作-新建流程-采购审核同意')
    user = APIRequest()
    api_response = user.API_PCBA_Add()
    user.API_PCBA_Purchase(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_Bom_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def PCBA_Derived_Purchase_API():
    logging.info('开始前置操作-新建流程-采购审核同意')
    user = APIRequest()
    api_response = user.API_PCBA_Derived_Add()
    user.API_Derived_PCBA_Purchase(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_Bom_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def PCBA_Business_API():
    logging.info('开始前置操作-新建流程-业务审核同意')
    user = APIRequest()
    api_response = user.API_PCBA_Add()
    user.API_PCBA_Business(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_Bom_Delete(api_response[1], api_response[2])


@pytest.fixture(scope='function', autouse=False)
def PCBA_Derived_Business_API():
    logging.info('开始前置操作-新建流程-业务审核同意')
    user = APIRequest()
    api_response = user.API_PCBA_Derived_Add()
    user.API_Derived_PCBA_Business(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_Bom_Delete(api_response[1], api_response[2])