import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class UserPage(Base):
    """用户类"""

    @allure.step("点击菜单")
    def click_menu(self, metatitle, nestmenu):
        self.is_click_tbm(user['一级菜单'], metatitle)
        logging.info(f'点击一级菜单：{metatitle}')
        self.is_click_tbm(user['二级菜单'], nestmenu)
        logging.info(f'点击二级菜单：{nestmenu}')
        sleep(1)
        self.refresh()

    @allure.step("点击新增")
    def click_add(self):
        self.is_click_tbm(user["新增"])
        sleep(2)

    @allure.step("选择Bom信息-制作类型")
    def click_lx(self):
        self.is_click_tbm(user["Bom信息-制作类型"])
        self.is_click_tbm(user["Bom信息-单机头BOM制作"])
        sleep(1)

    @allure.step("选择Bom信息-品牌")
    def click_pp(self):
        self.is_click_tbm(user["Bom信息-品牌"])
        self.is_click_tbm(user["Bom信息-itel"])
        sleep(1)

    @allure.step("选择Bom信息-机型")
    def click_jx(self):
        self.is_click_tbm(user["Bom信息-机型"])
        self.input_text(user["Bom信息-机型"],txt='C6769')
        self.is_click_tbm(user["Bom信息-C6769"])
        sleep(1)

    @allure.step("选择Bom信息-阶段")
    def click_jd(self):
        self.is_click_tbm(user["Bom信息-阶段"])
        self.is_click_tbm(user["Bom信息-试产阶段"])
        sleep(1)

    @allure.step("选择Bom信息-市场")
    def click_sc(self):
        self.is_click_tbm(user["Bom信息-市场"])
        self.is_click_tbm(user["Bom信息-孟加拉"])
        sleep(1)

    @allure.step("选择Bom信息-衍生")
    def click_ys(self):
        self.is_click_tbm(user["Bom信息-衍生"])
        self.is_click_tbm(user["Bom信息-否"])
        sleep(1)

    @allure.step("点击新增BOM")
    def click_add_bom(self):
        self.is_click_tbm(user["新增Bom"])
        self.is_click_tbm(user["新增Bom-编辑"])
        sleep(1)

    # @allure.step("选择新增Bom-Bom类型")
    # def click_bomlx(self):
    #     self.is_click_tbm(user["新增Bom-Bom类型"])
    #     self.is_click_tbm(user["新增Bom-国内生产BOM"])
    #     sleep(1)

    @allure.step("选择新增Bom-Bom状态")
    def click_bomzt(self):
        self.is_click_tbm(user["新增Bom-Bom状态"])
        self.is_click_tbm(user["新增Bom-试产"])
        sleep(1)

    @allure.step("选择新增Bom-物料编码")
    def click_bom_code(self):
        self.is_click_tbm(user["新增Bom-物料编码"])
        self.input_text(user["新增Bom-物料编码"], txt='12000001')
        self.is_click_tbm(user["新增Bom-12000001"])
        sleep(1)

    @allure.step("选择新增Bom-用量")
    def click_yl(self):
        self.is_click_tbm(user["新增Bom-用量"])
        self.input_text(user["新增Bom-用量"], txt='1000')
        self.is_click_tbm(user["新增Bom-确定"])
        sleep(1)

    @allure.step("审核人设置-MPM")
    def click_mpm(self):
        self.is_click_tbm(user["审核人设置-MPM"])
        self.is_click_tbm(user["审核人设置-成员列表输入"])
        self.input_text(user["审核人设置-成员列表输入"],txt="李小素")
        self.is_click_tbm(user["审核人设置-18645960"])
        self.is_click_tbm(user["审核人设置-确定"])
        sleep(1)

    @allure.step("审核人设置-采购部")
    def click_cg(self):
        self.is_click_tbm(user["审核人设置-采购部"])
        self.is_click_tbm(user["审核人设置-成员列表输入"])
        self.input_text(user["审核人设置-成员列表输入"], txt="李小素")
        self.is_click_tbm(user["审核人设置-18645960"])
        self.is_click_tbm(user["审核人设置-确定"])
        sleep(1)

    @allure.step("点击提交")
    def click_submit(self):
        self.is_click_tbm(user["提交"])
        sleep(1)

    @allure.step("查询")
    def click_search(self):
        self.is_click_tbm(user['查询'])

    @allure.step("流程编码")
    def get_code(self):
        code = self.element_text(user['流程编码'])
        return code

    @allure.step("点击列表")
    def click_menu1(self, metatitle, nestmenu):
        self.is_click_tbm(user['待办列表'], metatitle)
        logging.info(f'点击待办列表：{metatitle}')
        self.is_click_tbm(user['我申请的'], nestmenu)
        logging.info(f'点击我申请的：{nestmenu}')
        sleep(1)
        self.refresh()
        self.frame_enter(user['iframe'])

    @allure.step("点击查看详情")
    def click_xq(self, code):
        self.is_click_tbm(user["查看详情"], code)
        self.switch_window(1)
        sleep(2)

    @allure.step("撤回")
    def click_ch(self):
        self.is_click_tbm(user["撤回"])
        self.is_click_tbm(user["撤回确定"])
        self.close_switch(1)
        sleep(1)

    @allure.step("删除")
    def click_delete(self, code):
        self.is_click_tbm(user['查询'])
        self.is_click_tbm(user['删除'], code)
        self.is_click_tbm(user['撤回确定'])
if __name__ == '__main__':
    pass
