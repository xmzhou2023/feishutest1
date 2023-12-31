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
        for i in range(len(content)):
            navstr = navstr + '->' + content[i]
            level.append(navstr[2:])
        for i in range(len(content)):
            self.scroll_into_view_CRM(user[level[i]])
        sleep(2)

    @allure.step("前往菜单")
    def click_gotonav_CRM(self, *content,):
        """前往菜单"""
        level = []
        navstr = ""
        for i in range(len(content)):
            navstr = navstr + '->' + content[i]
            level.append(navstr[2:])
        for i in range(len(content)):
            self.is_click_tbm(user[level[i]])
        sleep(2)

    @allure.step("刷新菜单")
    def refresh_page(self):
        self.is_click(user["Dashboard"])
        self.refresh()
        self.wait.until(EC.presence_of_element_located(user["Dashboard"]), message="页面刷新失败")

    @allure.step("菜单搜索")
    def list_search(self, content):
        self.is_click(user["菜单搜索框"])
        sleep(2)
        self.input_text(user["菜单搜索框"], txt=content)
        self.hover(user["菜单搜索下拉框"])
        self.is_click(user["菜单搜索下拉框"])
        sleep(1)

    @allure.step("获取列表total数据值")
    def get_total(self):
        sleep(0.5)
        total = self.element_text(user["total数量"])
        logging.info("获取total文本{}".format(total))
        num = total.split(" ",1)
        number = num[1]
        return number

    @allure.step("获取网点以及网点国家")
    def get_shop(self):
        sleep(0.5)
        shop_name = self.element_text(user["Shop_Name"])
        logging.info("获取网点名称:{}".format(shop_name))
        shop_country = shop_name[0:2]
        logging.info("获取网点国家:{}".format(shop_country))
        return shop_name, shop_country

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


if __name__ == '__main__':
    pass
