from public.base.basics import Base
from libs.common.read_element import Element
from libs.common.time_ui import sleep
from libs.common.read_config import *
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)
pro_env = "test"
ini = ReadConfig(pro_name, pro_env)


class LoginPage(Base):
    """DCR登录类"""
    @allure.step("输入工号")
    def input_account(self, content):
        self.input_text(user['工号输入框'], txt=content)

    @allure.step("输入密码")
    def input_passwd(self, content):
        self.input_text(user['密码输入框'], txt=content)

    @allure.step("语言切换")
    def switch_lanuage(self, content):
        self.is_click(user['语言切换'])
        self.is_click(user['选择英文'], content)

    @allure.step("判断是否被选中")
    def click_check_box(self):
        self.is_click(user['隐私保护勾选'])

    @allure.step("获取复选框对应的 Class属性是否包含is-checked")
    def get_check_box_class(self):
        ss = self.find_element(user['隐私保护勾选'])
        get_check_state = ss.get_attribute('class')
        return get_check_state

    @allure.step("判断是否被选中")
    def check_box(self):
        checkbox = self.select_state(user['隐私保护勾选'])
        return checkbox

    @allure.step("点击帐号密码登录")
    def click_loginsubmit(self):
        self.is_click(user['登录'])

    @allure.step("点击退出登录")
    def click_loginOut(self):
        self.is_click(user['退出登录'])
        sleep(1.5)

    @allure.step("获取页面已登录的账号")
    def get_login_account(self):
        get_login_account = self.element_text(user['获取登录账号'])
        return get_login_account

    @allure.step("关闭当天打开状态的菜单")
    def click_close_open_menu(self):
        self.is_click(user['关闭当前打开的菜单'])
        sleep(1)

    @allure.step("获取当前打开状态的菜单class值")
    def get_open_menu_class(self):
        ss = self.find_element(user['打开状态的菜单'])
        get_menu_class = ss.get_attribute('class')
        return get_menu_class


    @allure.step("登录方法")
    def dcr_login(self, drivers, account, passwd):
        user = LoginPage(drivers)
        user.get_url(ini.url)
        sleep(3)
        user.input_account(account)
        user.input_passwd(passwd)
        get_check_class = user.get_check_box_class()
        if "is-checked" not in str(get_check_class):
            user.click_check_box()
        user.click_loginsubmit()
        sleep(4)


    @allure.step("退出重新登录，去掉打开登录地址")
    def dcr_again_login(self, drivers, account, passwd):
        user = LoginPage(drivers)
        user.input_account(account)
        user.input_passwd(passwd)
        get_check_class = user.get_check_box_class()
        if "is-checked" not in str(get_check_class):
            user.click_check_box()
        user.click_loginsubmit()
        sleep(4)


    @allure.step("查找菜单")
    def click_gotomenu(self, *content):
        sleep(2)
        level = []
        navstr = ""
        for i in range(len(content)):
            navstr = navstr + '->' + content[i]
            level.append(navstr[2:])
        for i in range(len(content)):
            logging.info(user[level[i]])
            sleep(3.5)
            self.scroll_into_view(user[level[i]])
            sleep(3.5)
            self.is_click(user[level[i]])
        sleep(6)

    @allure.step("初始化登录方法")
    def initialize_login(self, drivers, account1, password):
        get_account = self.get_login_account()
        if account1 != get_account:
            self.click_loginOut()
            self.dcr_again_login(drivers, account1, password)
        else:
            ref = Base(drivers)
            ref.refresh()


if __name__ == '__main__':
    pass