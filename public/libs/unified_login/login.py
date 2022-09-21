from public.base.basics import Base
# from libs.common.read_config import ini
from public.libs.unified_login.page_object.login import LoginPage, SrmLoginPage, PopLoginPage, OALoginPage
from public.libs.unified_login.page_object.login import DcrLoginPage

from time import sleep


class Login(Base):
    """登录类"""

    def login(self, drivers, url, username, passwd):
        """统一登录֤"""
        user = LoginPage(drivers)
        user.get_url(url) # 跳转到指定网页
        user.switch_lanuage("中文") # 传参为"中文"，"英文"，"法文"
        user.click_accountlogin() # 点击帐户密码登录
        user.input_account(username) # 输入帐户名
        user.input_passwd(passwd) # 输入密码
        user.click_checkbox()
        user.click_loginsubmit()


    def dcr_login(self, drivers, url, username, passwd):
        user = DcrLoginPage(drivers)
        user.get_url(url)
        sleep(3)
        user.dcr_input_account(username)
        user.dcr_input_passwd(passwd)
        sleep(1.5)
        get_check_class = user.dcr_get_check_box_class()
        if "is-checked" not in str(get_check_class):
            user.dcr_click_check_box()
        user.dcr_click_loginsubmit()

    def crm_login(self, drivers, url, username, passwd):
        """统一登录֤"""
        user = LoginPage(drivers)
        user.get_url(url)  # 跳转到指定网页
        user.switch_lanuage("中文")  # 传参为"中文"，"英文"，"法文"  #夏小珍 2022-9-6
        user.switch_lanuage("英文")  # 传参为"中文"，"英文"，"法文"
        user.click_accountlogin()  # 点击帐户密码登录
        user.input_account(username)  # 输入帐户名
        user.input_passwd(passwd)  # 输入密码
        user.click_checkbox_en()
        user.click_loginsubmit()


    def srm_login(self, drivers, url, elsAccount, elsSubAccount):
        user = SrmLoginPage(drivers)
        user.get_url(url)       # 跳转到指定网页
        user.input_elsAccount(elsAccount)      # 输入帐户名
        user.input_elsSubAccount(elsSubAccount)     # 点击帐户密码登录
        user.input_password()
        # 验证码错误，登录失败重跑
        for i in range(10):
            user.input_code()
            user.click_login()
            import time
            time.sleep(1)
            if 'login' in user.get_current_url():
                continue
            else:
                break


    def pop_login(self,drivers,url,popaccount,poppasswd):
        # 实例化调用public\libs\page_element\login.py里的封装的POP登录的类
        user = PopLoginPage(drivers)
        # 实例化调用PopLoginPage继承的Base类里面的方法：get_url
        user.get_url(url)
        # 输入账号
        user.input_pop_account(popaccount)
        # 输入密码
        user.input_pop_password(poppasswd)
        # 切换语言--默认切换成中文
        user.switch_language()
        # 勾选隐私协议
        user.click_privacy_policy()
        # 点击登录
        user.click_loginsubmit()

    def OA_login(self, drivers, url, username, passwd):
        """统一登录֤"""
        user = LoginPage(drivers)
        pwd = OALoginPage(drivers)
        user.get_url(url)  # 跳转到指定网页
        user.switch_lanuage("中文")  # 传参为"中文"，"英文"，"法文"
        user.click_accountlogin()  # 点击帐户密码登录
        user.input_account(username)  # 输入帐户名
        pwd.input_passwd(passwd)  # 输入密码
        user.input_imgcode()  # 输入验证码
        user.click_checkbox()
        user.click_loginsubmit()
