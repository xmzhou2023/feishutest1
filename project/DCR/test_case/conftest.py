import pytest
import logging
from public.data.unified_login.unified import *
from public.base.assert_ui import *
from public.libs.unified_login.login import Login
from libs.common.read_config import *

pro_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@pytest.fixture(scope='session',autouse=True)
def __init__(drivers, env_name):
    """初始化"""
    global pro_env
    pro_env = env_name
    logging.info("【{}】项目【{}】环境- UI自动化开始执行".format(pro_name, pro_env))
    ini = ReadConfig(pro_name, pro_env)

    logging.info("前置条件：传音统一登录开始")
    user = Login(drivers)
    user.dcr_login(drivers, ini.url, "lhmadmin", "dcr123456")
    DomAssert(drivers).assert_att("lhmadmin")
    logging.info("前置条件：传音统一登录成功")
