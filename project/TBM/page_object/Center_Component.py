from libs.common.read_element import Element
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name,object_name)


class CenterComponent(Base, APIRequest):
    """用户类"""

    @allure.step("点击菜单")
    def click_menu(self, metatitle, nestmenu):
        """点击菜单"""
        ele = self.element_text(user['当前菜单']).strip()
        if ele != nestmenu:
            try:
                self.is_click_tbm(user['meta-title'], metatitle)
                logging.info(f'点击一级菜单:{metatitle}')
                self.is_click_tbm(user['nest-menu'], nestmenu)
                logging.info(f'点击二级菜单:{nestmenu}')
                sleep(1)
                self.refresh()
            except Exception as e:
                self.base_get_img()
                self.refresh()
                self.is_click_tbm(user['meta-title'], metatitle)
                logging.info(f'点击一级菜单:{metatitle}')
                self.is_click_tbm(user['nest-menu'], nestmenu)
                logging.info(f'点击二级菜单:{nestmenu}')
                sleep(1)
                self.refresh()

    @allure.step("初始化浏览器")
    def refresh_webpage(self):
        self.refresh()
        self.driver.switch_to.default_content()
        handles = self.driver.window_handles
        logging.info('当前窗口：{}'.format(handles))
        if len(handles) != 1:
            for i in range(1, len(handles)):
                self.close_switch(1)
        else:
            self.switch_window(0)

    @allure.step("进入框架")
    def enter_oneworks_iframe(self):
        self.frame_enter(user['待办列表-iframe'])

    @allure.step("退出oneworks查看流程页面")
    def quit_oneworks(self):
        self.frame_exit()
        self.close_switch(1)
        self.refresh()
        self.frame_exit()

    @allure.step("进入框架")
    def refresh_todo_list(self):
        """进入待办列表 刷新单据页面"""
        try:
            self.refresh()
            self.frame_enter(user['待办列表-iframe'])
            self.is_click_tbm(user['待办列表-刷新'])
        except:
            self.refresh()
            self.frame_enter(user['待办列表-iframe'])
            self.is_click_tbm(user['待办列表-刷新'])

    @allure.step("待办列表 根据单据号 筛选")
    def screening_code(self, code):
        """
        待办列表 根据单据号 筛选
        @param code:流程编码
        """
        self.is_click_tbm(user['待办列表-筛选框'])
        self.input_text(user['待办列表-筛选框-单据号'], code)
        self.is_click_tbm(user['待办列表-筛选框-筛选'])
        for i in range(20):
            all_text = self.element_text(user['所有文本'])
            text = all_text.replace("\n", "|")
            if code not in text:
                self.is_click(user['待办列表-刷新'])
                sleep(1)
            else:
                break

    @allure.step("进入 我的待办 页面")
    def enter_my_todo(self):
        ele = self.element_text(user['当前菜单']).strip()
        if ele == '我的待办':
            self.refresh_todo_list()
        else:
            self.click_menu('待办列表', '我的待办')
            sleep(1)
            self.refresh_todo_list()

    @allure.step("进入 我申请的 页面")
    def enter_my_application(self):
        ele = self.element_text(user['当前菜单']).strip()
        if ele == '我申请的':
            self.refresh_todo_list()
        else:
            self.click_menu('待办列表', '我申请的')
            self.refresh_todo_list()

    @allure.step("点击 查看详情 进入 oneworks 页面")
    def enter_oneworks_edit(self, code, node=None):
        """
        点击 查看详情 进入 oneworks 页面
        输入流程编码过滤后，根据当前节点名称点击查看详情进入详情页面
        @param code:流程编码
        @param node:节点名称
        """
        self.enter_my_todo()
        self.screening_code(code)
        if node is not None:
            self.is_click_tbm(user['待办列表-我申请的-查看详情(节点名称)'], node)
        else:
            self.is_click_tbm(user['待办列表-我申请的-查看详情'], code)
        logging.info('点击查看详情')
        self.frame_exit()
        logging.info('跳出框架')
        self.switch_window(1)
        logging.info('切换窗口')
        sleep(5)
        logging.info('强制等待')
        self.frame_enter(user['待办列表-iframe'])
        logging.info('进入框架')
        DomAssert(self.driver).assert_att('基本信息')

    @allure.step("断言审核流程")
    def assert_approve_flow(self):
        att = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'成功')]"))).text
        logging.info(att)
        try:
            if '请求成功' in att or '审核通过' in att or '操作成功' in att:
                return True
            else:
                return False
        except:
            raise

    @allure.step("我的待办页面-断言：我的待办中存在/不存在该条单据在指定审核节点")
    def assert_my_todo_node(self, code, node, exist=False):
        """
        我的待办页面-断言：成功处理了流程后，我的待办中存在/不存在该条单据在指定审核节点
        @param code:流程编码
        @param node:节点名称
        @param exist:断言存在或者不存在
        """
        self.enter_my_todo()
        self.screening_code(code)
        actual_node = self.element_text(user['待办列表-我的待办-当前节点'], code)
        if exist is False:
            try:
                assert actual_node != node
                logging.info('断言成功，我的待办中该条单据不存在:{}节点，实际在:{}节点'.format(node, actual_node))
            except:
                self.base_get_img()
                logging.error('断言失败，我的待办中存在该条单据在:{}审核节点'.format(actual_node))
                raise
            finally:
                self.frame_exit()
        else:
            try:
                assert actual_node == node
                logging.info('断言成功，我的待办中存在该条单据在:{}审核节点'.format(actual_node))
            except:
                self.base_get_img()
                logging.error('断言失败，我的待办中该条单据不存在:{}节点，实际在:{}节点'.format(node, actual_node))
                raise
            finally:
                self.frame_exit()

    @allure.step("我申请的页面-断言：我的待办中存在/不存在该条单据在指定审核节点")
    def assert_my_application_node(self, code, node, exist=False):
        """
        我申请的页面-断言：成功处理了流程后，我申请的中存在/不存在该条单据在指定审核节点
        @param code:流程编码
        @param node:节点名称
        @param exist:断言存在或者不存在
        """
        self.enter_my_application()
        self.screening_code(code)
        actual_node = self.element_text(user['待办列表-我申请的-当前节点'], code)
        if exist is False:
            try:
                assert actual_node != node
                logging.info('断言成功，我申请的中该条单据不存在:{}节点，实际在:{}节点'.format(node, actual_node))
            except:
                self.base_get_img()
                logging.error('断言失败，我申请的中存在该条单据在:{}节点'.format(actual_node))
                raise
            finally:
                self.frame_exit()
        else:
            try:
                assert actual_node == node
                logging.info('断言成功，我申请的中存在该条单据在:{}审核节点'.format(actual_node))
            except:
                self.base_get_img()
                logging.error('断言失败，我申请的中不存在该条单据在:{}审核节点'.format(actual_node))
                raise
            finally:
                self.frame_exit()

    @allure.step("我申请的页面-断言：我的待办中存在/不存在该条单据在指定流程")
    def assert_my_application_flow(self, code, flow, exist=True):
        """
        我申请的页面-断言：成功处理了流程后，我申请的中存在/不存在该条单据在指定流程中
        @param code:流程编码
        @param flow:流程名称
        @param exist:断言存在或者不存在
        """
        self.enter_my_application()
        self.screening_code(code)
        actual_flow = self.element_text(user['待办列表-我申请的-当前流程'], code)
        if exist is True:
            try:
                assert actual_flow == flow
                logging.info('断言成功，我申请的中该条单据在:{}流程'.format(actual_flow))
            except:
                self.base_get_img()
                logging.error('断言失败，我申请的中该条单据不在:{}流程，实际在:{}流程'.format(flow, actual_flow))
                raise
            finally:
                self.frame_exit()
        elif exist is False:
            try:
                assert actual_flow != flow
                logging.info('断言成功，我申请的中该条单据不在:{}流程，实际在:{}流程'.format(flow, actual_flow))
            except:
                self.base_get_img()
                logging.error('断言失败，我申请的中该条单据在:{}流程'.format(actual_flow))
                raise
            finally:
                self.frame_exit()

    @allure.step("在待办列表-我申请的 根据流程编码对流程进行撤回操作")
    def recall_process(self, code):
        """
        提交流程申请后，在待办列表-我申请的 根据流程编码对流程进行撤回操作
        @param code:流程编码
        """
        self.enter_my_application()
        try:
            self.is_click_tbm(user['待办列表-我申请的-查看详情'], code)
        except:
            self.refresh()
            self.frame_enter(user['待办列表-iframe'])
            self.is_click_tbm(user['待办列表-我申请的-查看详情'], code)
        self.switch_window(1)
        try:
            self.is_click_tbm(user['撤回'])
            self.is_click_tbm(user['撤回确定'])
        except:
            self.base_get_img()
            self.refresh()
            self.is_click_tbm(user['撤回'])
            self.is_click_tbm(user['撤回确定'])
        self.frame_exit()
        self.switch_window(0)
        self.frame_exit()

    @allure.step("断言：校验转交流程在转交人")
    def assert_flow_deliver(self, code, name):
        """
        断言：BOM工程师审批页面 确认转交后，校验流程移交到转交人上
        @param code:流程编码
        @param name:审批人名称
        """
        self.enter_my_application()
        self.screening_code(code)
        approver = self.element_text(user['待办列表-我申请的-审批人'], code)
        try:
            assert approver == name
            logging.info('断言成功，审批人为:{}'.format(approver))
        except:
            self.base_get_img()
            logging.error('断言失败，审批人为:{}'.format(approver))
            raise
        finally:
            self.frame_exit()

    @allure.step("oneworks点击同意")
    def click_oneworks_agree(self):
        self.frame_exit()
        self.is_click_tbm(user['同意'])
        logging.info('点击同意')

    @allure.step("oneworks点击确定")
    def click_oneworks_confirm(self):
        self.is_click_tbm(user['同意确定'])
        logging.info('点击确定')

    @allure.step("oneworks点击转交")
    def click_oneworks_refer(self):
        self.frame_exit()
        self.is_click_tbm(user['转交'])
        logging.info('点击转交')

    @allure.step("oneworks转交 点击确认")
    def click_oneworks_refer_comfirm(self):
        self.is_click_tbm(user['转交-确定'])
        logging.info('点击转交确定')

    @allure.step("断言：是否存在确定转交按钮")
    def assert_oneworks_comfirmrefer_exist(self, result):
        DomAssert(self.driver).assert_control(user['确定转交'], result)

    @allure.step("转交 输入转交人")
    def input_oneworks_refer(self, referrer):
        """
        转交 输入转交人
        @param referrer:转交人
        """
        self.input_text(user['转交-转交人输入'], referrer)
        logging.info('输入转交人：{}'.format(referrer))
        self.is_click_tbm(user['转交-查询'])
        logging.info('点击查询')

    @allure.step("转交 选择转交人")
    def select_oneworks_refer(self, referrer):
        """
        BOM工程师审批页面 转交 选择转交人
        @param referrer:转交人
        """
        self.is_click_tbm(user['转交-转交人选择'], referrer)
        logging.info('点击转交人')

    @allure.step("选择转交后 点击取消")
    def click_oneworks_refer_cancel(self):
        self.is_click_tbm(user['转交取消'])
        logging.info('点击转交取消')

    @allure.step("选择转交后 点击确认转交")
    def click_oneworks_refer_comfirmrefer(self):
        self.is_click_tbm(user['确定转交'])
        logging.info('点击确认转交')

    @allure.step("断言： 是否存在转交，回退按钮")
    def assert_oneworks_rollback_refer_exist(self, result):
        DomAssert(self.driver).assert_control(user['回退'], result)
        DomAssert(self.driver).assert_control(user['转交'], result)


if __name__ == '__main__':
    pass
