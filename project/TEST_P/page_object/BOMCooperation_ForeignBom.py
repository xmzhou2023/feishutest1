import logging
from time import sleep
from selenium.webdriver import Keys
from libs.common.read_element import Element
from libs.config.conf import BASE_DIR
from project.TBM.page_object.Center_Component import CenterComponent
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class ForeignBom(CenterComponent):
    """用户类"""

    @allure.step("初始化页面")
    def refresh_webpage_click_menu(self):
        self.refresh_webpage()
        self.click_menu("BOM协作", "外研BOM协作")

    @allure.step("外研BOM协作新增页面-输入BOM信息")
    def input_add_bom_info(self, info, select):
        """
        外研BOM协作新增页面-输入BOM信息
        :param info: 选择要输入的信息
        :param select: 选择信息内容
        """
        if info == '机型':
            self.input_text(user['BOM信息输入框'], select, info)
            sleep(1)
            self.is_click_tbm(user['BOM信息输入框机型选择'], select)
            logging.info('选择点击Bom信息:{}'.format(select))
        else:
            self.is_click_tbm(user['BOM信息输入框'], info)
            logging.info('点击Bom信息:{}输入框'.format(info))
            sleep(0.5)
            self.scroll_into_view(user['BOM信息输入框选择'], select)
            sleep(1)
            self.is_click_tbm(user['BOM信息输入框选择'], select)
            logging.info('选择点击Bom信息:{}'.format(select))

    @allure.step("外研BOM协作新增页面-输入BOM信息组合")
    def add_bom_info(self):
        self.click_add()
        self.input_add_bom_info('制作类型', '客供BOM制作')
        self.input_add_bom_info('品牌', 'itel')
        self.input_add_bom_info('机型', 'JMB-01')
        self.input_add_bom_info('阶段', '量产阶段')
        self.input_add_bom_info('市场', '埃塞本地')
        self.input_add_bom_info('模式', '零价值客供')
        self.base_get_img()

    @allure.step("外研BOM协作新增页面-输入BOMtree组合")
    def add_bomtree_info(self):
        self.click_add_bomtree()
        self.input_bomtree('客供BOM','BOM状态', '量产')
        self.input_bomtree('客供BOM','物料编码', '12004871')
        self.input_bomtree('客供BOM','用量', '1000')
        self.click_optional_material()
        self.input_optional_material('12004871', '物料编码', '12800002')
        self.input_optional_material('12004871', '用量', '1000')
        self.base_get_img()

    @allure.step("点击提交")
    def click_add_submit(self):
        self.scroll_into_view(user['提交'])
        sleep(0.5)
        self.is_click_tbm(user['提交'])
        logging.info('点击提交')

    @allure.step("点击保存")
    def click_add_save(self):
        self.scroll_into_view(user['保存'])
        sleep(0.5)
        self.is_click_tbm(user['保存'])
        logging.info('点击保存')

    @allure.step("点击刷新")
    def click_refresh(self):
        self.scroll_into_view(user['刷新'])
        self.is_click_tbm(user['刷新'])
        logging.info('点击刷新')

    @allure.step("点击编辑")
    def click_edit(self, code):
        self.is_click_tbm(user['编辑'], code)
        logging.info('点击编辑')

    @allure.step("输入查询条件")
    def input_search_info(self, type, info):
        input_type = ['标题', '流程编码', 'BOM编码']
        select_type = ['制作类型', '品牌', '阶段', '市场', '单据状态', '同步状态']
        if type in input_type:
            self.readonly_input_text(user['查询条件'], info, type)
        elif type in select_type:
            self.is_click_tbm(user['查询条件'], type)
            self.is_click_tbm(user['查询选择'], info)
        logging.info('输入框：{}，输入内容：{}'.format(type, info))
    @allure.step("点击查询")
    def click_search(self):
        self.is_click_tbm(user['查询'])
        logging.info('点击查询')

    @allure.step("断言：查询结果")
    def assert_search_result(self, header, content):
        DomAssert(self.driver).assert_search_result(user['表格字段'], user['表格指定列内容'], header, content)

    @allure.step("点击新增bom")
    def click_add_bomtree(self):
        self.is_click_tbm(user['新增BomTree'])
        logging.info('点击新增Bom')
        sleep(0.5)

    @allure.step("BomTree信息根据Tree在指定列输入内容")
    def input_bomtree(self, tree, header, content):
        """
        BomTree信息根据Tree在指定列表输入内容
        @param tree:输入选择
        @param header: BomTree要输入的表头；【BOM类型， BOM状态， 物料编码， 用量， 替代组， 份额】
        @param content:输入的内容
        """
        if header == '物料编码':
            self.is_click_tbm(user['BOMTree编辑'], tree)
            self.readonly_input_text(user['BOMTree物料编码'], content, tree)
            sleep(1)
            self.is_click_tbm(user['物料编码选择'], content)
            self.is_click_tbm(user['BOMTree确定'], tree)
        elif header == 'BOM状态':
            self.is_click_tbm(user['BOMTreeBOM状态'], tree)
            sleep(0.5)
            self.is_click_tbm(user['BOMTree输入框选择'], content)
        elif header == '用量':
            self.is_click_tbm(user['BOMTree编辑'], tree)
            self.readonly_input_text(user['BOMTree用量'], content, tree)
            self.is_click_tbm(user['BOMTree确定'], tree)
        elif header == '替代组':
            self.is_click_tbm(user['BOMTree编辑'], tree)
            self.readonly_input_text(user['BOMTree替代组'], content, tree)
            self.is_click_tbm(user['BOMTree确定'], tree)
        elif header == '份额':
            self.is_click_tbm(user['BOMTree编辑'], tree)
            self.readonly_input_text(user['BOMTree份额'], content, tree)
            self.is_click_tbm(user['BOMTree确定'], tree)
        else:
            logging.info("输入需要操作的表头：('BOM类型','BOM状态','物料编码','用量','替代组','份额',)")

    @allure.step("点击新增物料")
    def click_optional_material(self):
        self.is_click_tbm(user['新增物料'])
        logging.info('点击新增物料')

    @allure.step("新增物料对焦")
    def material_focus(self, tree):
        """
        新增物料后，根据上级物料 点击新增加的物料列进行对焦
        """
        self.is_click_tbm(user['BOMTree物料对焦'], tree)

    @allure.step("新增物料输入内容")
    def input_optional_material(self, tree, header, content):
        """
        新增物料后，模版信息根据条件在新增的物料输入内容并且点击
        @param content:输入的内容
        @param header: BomTree要输入的表头；{'BOM类型':'2','BOM状态':'3','物料编码':'6','用量':'9','替代组':'10','份额':'11',}
        """
        if header == '物料编码':
            self.is_click_tbm(user['BOMTree新增物料编辑'], tree)
            self.readonly_input_text(user['BOMTree新增物料物料编码'], content, tree)
            sleep(1)
            self.is_click_tbm(user['物料编码选择'], content)
            self.is_click_tbm(user['BOMTree新增物料确定'], tree)
        elif header == '用量':
            self.is_click_tbm(user['BOMTree新增物料编辑'], tree)
            self.readonly_input_text(user['BOMTree新增物料用量'], content, tree)
            self.is_click_tbm(user['BOMTree新增物料确定'], tree)
        elif header == '替代组':
            self.is_click_tbm(user['BOMTree新增物料编辑'], tree)
            self.readonly_input_text(user['BOMTree新增物料替代组'], content, tree)
            self.is_click_tbm(user['BOMTree新增物料确定'], tree)
        elif header == '份额':
            self.is_click_tbm(user['BOMTree新增物料编辑'], tree)
            self.readonly_input_text(user['BOMTree新增物料份额'], content, tree)
            self.is_click_tbm(user['BOMTree新增物料确定'], tree)
        else:
            logging.info("输入需要操作的表头：('BOM类型','BOM状态','物料编码','用量','替代组','份额',)")

    @allure.step("审核人设置")
    def select_business_review(self, audit, type='all'):
        """
        审核人设置-业务评审-：选择用户
        @param type:选择的类别
        @param audit:输入的用户名
        """
        self.scroll_into_view(user['审核人设置'])
        if type == 'all':
            info = self.find_elements_tbm(user['审核人名单'])
            infolist = []
            for i in info:
                infolist.append(i.text)
                self.is_click_tbm(user['审核人类别'], i.text)
                self.input_text(user['成员列表输入框'], audit)
                sleep(1)
                self.is_click_tbm(user['成员选择'], audit)
                self.is_click_tbm(user['成员确定'])
            self.base_get_img()
            logging.info('获取表格搜索结果的所有信息文本{}'.format(infolist))
        else:
            self.is_click_tbm(user['审核人类别'], type)
            self.input_text(user['成员列表输入框'], audit)
            sleep(1)
            self.is_click_tbm(user['成员选择'], audit)
            self.is_click_tbm(user['成员确定'])

    @allure.step("获取外研BOM协作第一列内容")
    def get_info(self):
        """
        获取外研BOM协作第一列内容
        @return:返回文本及索引位置分别是'流程编码':2; '制作类型':2; '机型'：3; '品牌':4; '市场':5; '阶段':6; '单据状态':7; '同步状态':8; '申请人':9; '创建时间':10;
        """
        self.click_menu("BOM协作", "外研BOM协作")
        sleep(1)
        info = self.find_elements_tbm(user['表格内容'])
        infolist = []
        for i in info:
            infolist.append(i.get_attribute('innerText'))
        logging.info('获取表格搜索结果的所有信息文本{}'.format(infolist))
        return infolist

    def get_col_info(self, header):
        """
        获取外研BOM协作指定内容
        @return:返回文本及索引位置分别是'流程编码':2; '制作类型':2; '机型'：3; '品牌':4; '市场':5; '阶段':6; '单据状态':7; '同步状态':8; '申请人':9; '创建时间':10;
        """

        self.click_menu("BOM协作", "外研BOM协作")
        sleep(1)
        column = self.get_table_info(user['表格字段'], header)
        contents = self.find_element(user['表格指定列内容'], column).text
        return contents


    def click_delete(self, code):
        """
        根据流程编码点击删除 进行删除操作
        @param code:流程编码
        """
        self.is_click_tbm(user['删除'], code)

    def click_delete_confirm(self):
        self.is_click_tbm(user['同意确定'])

    def click_delete_cancel(self):
        self.is_click_tbm(user['同意取消'])

    @allure.step("新建流程后的后置删除处理")
    def delete_flow(self, code):
        self.recall_process(code)
        self.click_menu("BOM协作", "外研BOM协作")
        self.click_delete(code)
        self.click_delete_confirm()
        self.assert_toast('删除成功')

    @allure.step("断言单机头BOM协作新增成功后，页面表格内容是否正确")
    def assert_add_result(self, *content):
        """
        断言单机头BOM协作新增成功后，页面表格内容是否正确
        :param content: 需要，可以一次传入多个
        """
        try:
            contents = self.get_info()
            assert set(content) <= set(contents)
            logging.info('断言成功，选项值包含：{}'.format(content))
        except:
            logging.error('断言失败，选项值不包含：{}'.format(content))
            raise

    def click_one_press(self):
        """
        点击一键填写
        """
        self.is_click_tbm(user['BOM信息一键填写'])

    @allure.step("BOM信息一键填写")
    def input_one_press(self, key, value):
        """
        一键填写-根据key选择字段名称，根据value输入字段值
        @param key:字段名称
        @param value:字段值
        """
        self.click_one_press()
        sleep(0.5)
        self.is_click_tbm(user['BOM信息一键填写-字段名称'])
        sleep(0.5)
        self.is_click_tbm(user['BOM信息一键填写-字段名称选择'], key)
        sleep(0.5)
        if key == '用量':
            if value == '':
                self.find_element(user['BOM信息一键填写-字段值默认']).send_keys(Keys.CONTROL + 'a')
                self.find_element(user['BOM信息一键填写-字段值默认']).send_keys(Keys.BACKSPACE)
            self.input_text(user['BOM信息一键填写-字段值默认'], value)
        else:
            if value == '':
                self.find_element(user['BOM信息一键填写-字段值']).send_keys(Keys.CONTROL + 'a')
                self.find_element(user['BOM信息一键填写-字段值']).send_keys(Keys.BACKSPACE)
            self.input_text(user['BOM信息一键填写-字段值'], value)
        sleep(0.5)
        self.is_click_tbm(user['确定'])
        sleep(0.5)

    def click_one_press_cancel(self):
        """
        点击取消
        """
        self.is_click_tbm(user['BOM信息一键填写取消'])
        sleep(0.5)
        logging.info('点击取消')

    @allure.step("获取BOMTREE指定列内容")
    def get_bomtree_info(self, material):
        """
        获取单机头BOM协作-BOMTREE指定列内容
        @param material:物料名
        @return:返回文本及索引位置分别是  1:'BOM状态'; 2:'Tree';4:'物料编码'; 5:'物料描述'; 6:'物料属性'; 7:'用量'; 8:'替代组'; 9:'份额';
        """
        info = self.find_elements_tbm(user['BomTree内容'], material)
        infolist = []
        for i in info:
            infolist.append(i.get_attribute('innerText'))
        logging.info('获取表格搜索结果的所有信息文本{}'.format(infolist))
        return infolist

    @allure.step("点击复选框")
    def click_checkbox(self, material='all'):
        """
        TOM Tree根据material点击指定复选框，默认全选
        @param material:物料名，传入BomTree的物料名称；默认‘all’表示点击全选复选框
        """
        if material == 'all':
            self.is_click_tbm(user['复选框全选'])
        else:
            self.is_click_tbm(user['复选框单选'], material)
        sleep(0.5)

    @allure.step("断言：文本是否包含")
    def assert_value_in(self, value, content):
        try:
            assert value in content
        except:
            raise

    @allure.step("断言：判断是否存在批量删除")
    def assert_batch_delete(self, result):
        DomAssert(self.driver).assert_control(user['批量删除'], result)

    @allure.step("根据Tree点击删除按钮")
    def click_bomtree_delete(self, tree, type='Tree'):
        if type == 'Tree':
            self.is_click_tbm(user['BOMTree指定Tree删除'], tree)
        else:
            self.is_click_tbm(user['BOMTree删除'], tree)
        self.click_batch_confirm()

    def assert_bomtree(self, tree):
        DomAssert(self.driver).assert_control(user['BOMTree新增物料物料编码'], False, tree)

    @allure.step("点击确定")
    def click_batch_confirm(self):
        self.is_click_tbm(user['确定'])
        logging.info('确定')
        sleep(0.5)

    @allure.step("点击导入BOM")
    def click_bom_import(self):
        self.is_click_tbm(user['导入BOM'])
        logging.info('点击导入BOM')

    @allure.step("导入-上传文件")
    def upload_import(self, file):
        ele = self.driver.find_element(By.XPATH,
                                       "//div[not(contains(@style,'display: none')) and @class='el-dialog__wrapper']/div/div[2]/div[1]/div/input")
        ele.send_keys(file)
        logging.info('点击导入-上传文件')

    @allure.step("导入BOM-上传正确文件")
    def upload_true_file(self):
        path = os.path.join(BASE_DIR, 'project', 'TBM', 'data', '外研客供BOM导入模板.xlsx')
        self.upload_import(path)
        DomAssert(self.driver).assert_control(user['导入BOM校验结果成功状态'])

    @allure.step("导入BOM-上传错误文件")
    def upload_wrong_file(self):
        path = os.path.join(BASE_DIR, 'project', 'TBM', 'data', 'worng_file_text.txt')
        self.upload_import(path)

    @allure.step("导入BOM-上传错误内容文件")
    def upload_wrongcontent_file(self):
        path = os.path.join(BASE_DIR, 'project', 'TBM', 'data', '外研客供BOM导入模板错误内容.xlsx')
        self.upload_import(path)
        sleep(2)
        DomAssert(self.driver).assert_att('外购单机头_TECNO_W1_B40030_埃塞_新客供')

    @allure.step("断言导入错误内容后，页面状态是否正确")
    def assert_wrongcontent_upload_result(self):
        try:
            apply = self.find_element(user['导入BOM应用状态'])
            check = self.find_element(user['导入BOM导出校验状态'])
            assert 'is-disabled' in apply.get_attribute('class')
            assert 'is-disabled' not in check.get_attribute('class')
            logging.info('断言成功，导出校验可点击，应用不可点击')
        except:
            self.base_get_img()
            logging.error('断言失败，请检查按钮状态')
            raise

    def get_bomtree_upload_info(self):
        """
        获取导入BOM-结果内容
        """
        info = self.find_elements_tbm(user['导入BOM内容'])
        infolist = []
        for i in info:
            infolist.append(i.text.split('\n'))
        logging.info('获取BOM导入结果{}'.format(infolist))
        return infolist

    @allure.step("断言导入后，页面表格内容是否正确")
    def assert_upload_result(self, *content):
        """
        断言导入后，页面表格内容是否正确
        :param content: 需要断言的内容，可以一次传入多个
        """
        try:
            contents = self.get_bomtree_upload_info()
            content_list = []
            for i in contents:
                content_list.append(tuple(i))
            logging.info(content_list)
            assert set(content) <= set(content_list)
            logging.info('断言成功，选项值包含：{}'.format(content))
        except:
            self.base_get_img()
            logging.error('断言失败，选项值不包含：{}'.format(content))
            raise

    @allure.step("点击应用")
    def click_apply(self):
        self.is_click_tbm(user['应用'])
        logging.info('点击应用')

    @allure.step("点击展开+图标")
    def click_tree(self, tree):
        """
        点击展开+图标
        :param tree: 物料名称
        """
        self.is_click_tbm(user['展开'], tree)
        logging.info('点击展开')

    def get_bomtree_tree_info(self):
        """
        获取BOMTree所有内容
        """
        info = self.find_elements_tbm(user['BomTree全部内容'])
        infolist = []
        for i in info:
            infolist.append(i.text.split('\n'))
        logging.info('获取BOMTree所有内容{}'.format(infolist))
        return infolist


    @allure.step("断言导入BOM-导入后，页面表格内容是否正确")
    def assert_tree_result(self, *content):
        """
        断言导入BOM-导入后，页面表格内容是否正确
        :param content: 需要断言的内容，可以一次传入多个
        """
        try:
            contents = self.get_bomtree_tree_info()
            content_list = []
            for i in contents:
                content_list.append(tuple(i))
            assert set(content) <= set(content_list)
            logging.info(content_list)
            logging.info('断言成功，选项值包含：{}'.format(content))
        except:
            self.base_get_img()
            logging.error('断言失败，选项值不包含：{}'.format(content))
            raise

    @allure.step("断言：页面表格内容是否正确")
    def assert_oneworks_bomtree_result(self, *content):
        """
        断言导入BOM-简易导入后，页面表格内容是否正确
        :param content: 需要断言的内容，可以一次传入多个
        """
        try:
            self.click_tree('客供BOM')
            contents = self.get_oneworks_bomtree_info()
            content_list = []
            for i in contents:
                content_list.append(tuple(i))
            assert set(content) <= set(content_list)
            logging.info(content_list)
            logging.info('断言成功，选项值包含：{}'.format(content))
        except:
            self.base_get_img()
            logging.error('断言失败，选项值不包含：{}'.format(content))
            raise
if __name__ == '__main__':
    pass