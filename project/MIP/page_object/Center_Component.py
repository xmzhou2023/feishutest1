import logging

import allure
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name,object_name)

class NavPage(Base):

    @allure.step("前往菜单")
    def click_gotonav(self, *content,):
        """前往菜单"""
        level = []
        navstr = ""
        print(content)
        for i in range(len(content)):
            navstr = navstr + '->' + content[i]
            level.append(navstr[2:])
        for i in range(len(content)):
            self.is_click(user[level[i]])
        sleep(2)

    @allure.step("返回首页")
    def back_homepage(self):
        get_url = self.driver.current_url
        if "/dashboard" not in get_url:
            self.is_click(user['返回首页'])
            self.is_click(user['收起二级菜单'])
            logging.info("返回首页 完成")
        else:
            pass



if __name__ == '__main__':
    pass
