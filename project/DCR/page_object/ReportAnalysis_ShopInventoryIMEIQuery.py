from libs.common.read_element import Element
import logging
from libs.common.time_ui import sleep
from public.base.basics import Base
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class ShopInventoryIMEIQueryPage(Base):
    """ShopInventoryIMEIQueryPage，生产环境，Shop Inventory IMEI Query 页面元素定位"""
    @allure.step("Shop Inventory IMEI Query页面，点击Unfold展开筛选条件")
    def click_unfold(self):
        """Shop Inventory IMEI Query页面，点击Unfold展开筛选条件"""
        self.is_click(user['Unfold'])
        sleep(2)

    @allure.step("Shop Inventory IMEI Query页面，输入shop ID，进行筛选")
    def input_shop_id(self, content):
        self.is_click_dcr(user['筛选门店'])
        sleep(1)
        self.input_text_dcr(user['筛选门店'], txt=content)
        sleep(3)
        self.is_click_dcr(user['选中筛选门店值'], content)

    @allure.step("Shop Inventory IMEI Query页面，输入筛选开始日期")
    def input_inbound_date(self, content):
        self.is_click(user['Inbound Date Start Time'])
        sleep(1)
        self.input_text(user['Inbound Date Start Time'], txt=content)

    @allure.step("Shop Inventory IMEI Query页面，点击Search按钮")
    def click_search(self):
        self.is_click(user['Search'])
        self.element_exist(user['Loading'])

    @allure.step("Shop Inventory IMEI Query页面，点击Search按钮")
    def click_reset(self):
        self.is_click(user['Reset'])
        self.element_exist(user['Loading'])

    @allure.step("Shop Inventory IMEI Query页面，点击Fold收起筛选条件按钮")
    def click_fold(self):
        self.is_click(user['Fold'])
        sleep(1)

    @allure.step("Shop Inventory IMEI Query页面，获取分页功能总条数文本")
    def get_total_text(self):
        self.presence_sleep_dcr(user['获取总条数文本'])
        total = self.element_text(user['获取总条数文本'])
        total1 = total[6:]
        return total1

    @allure.step("Shop Inventory IMEI Query页面，获取列表Shop ID文本")
    def get_shop_id_text(self):
        self.presence_sleep_dcr(user['获取Shop ID文本'])
        shop_id = self.element_text(user['获取Shop ID文本'])
        return shop_id

    @allure.step("Shop Inventory IMEI Query页面，获取Shop Name文本")
    def get_shop_name_text(self):
        shop_name = self.element_text(user['获取Shop Name文本'])
        return shop_name

    @allure.step("Shop Inventory IMEI Query页面，获取Brand文本")
    def get_brand_text(self):
        brand = self.element_text(user['获取Brand文本'])
        return brand

    @allure.step("Shop Inventory IMEI Query页面，获取Series文本")
    def get_series_text(self):
        series = self.element_text(user['获取Series文本'])
        return series

    @allure.step("Shop Inventory IMEI Query页面，获取Model文本")
    def get_model_text(self):
        model = self.element_text(user['获取Model文本'])
        return model

    @allure.step("Shop Inventory IMEI Query页面，点击Export导出按钮")
    def click_export(self):
        self.is_click(user['Export'])
        sleep(2)

    @allure.step("关闭导出记录菜单")
    def click_close_export_record(self):
        self.is_click(user['关闭导出记录菜单'])

    @allure.step("关闭门店库存IMEI菜单")
    def click_close_shop_inventory_imei(self):
        self.is_click(user['关闭门店库存IMEI菜单'])


    # 门店库存IMEI查询记录，导出功能验证
    @allure.step("Visit Record页面，点击Export导出按钮")
    def click_export(self):
        """Visit Record页面，点击Export导出按钮"""
        self.is_click(user['Export'])

    @allure.step("Visit Record页面，点击下载Download Icon->more更多按钮")
    def click_download_more(self):
        self.is_click(user['Download Icon'])
        sleep(1)
        self.presence_sleep_dcr(user['More'])
        self.is_click(user['More'])
        self.element_exist(user['Loading'])

    @allure.step("输入Task Name筛选该任务的导出记录")
    def input_task_name(self, content):
        self.is_click(user['Input Task Name'])
        self.input_text(user['Input Task Name'], txt=content)
        sleep(0.5)
        self.is_click_dcr(user['Task Name value'], content)

    @allure.step("输入Create Date 开始日期筛选该任务的导出记录")
    def export_record_create_date_query(self, start_date):
        self.is_click(user['Export Record Create Date'])
        self.input_text(user['Export Record Create Date'], start_date)
        self.is_click(user['点击筛选项label'], 'Create Date')

    @allure.step("循环点击查询，直到获取到下载状态为COMPLETE")
    def click_export_search(self):
        """循环点击查询，直到获取到下载状态为COMPLETE """
        down_status = self.export_download_status(user['Export Record Search'], user['获取下载状态文本'])
        return down_status

    @allure.step("导出记录页面，获取列表 Download Status文本")
    def get_download_status_text(self):
        status = self.element_text(user['获取下载状态文本'])
        return status

    @allure.step("导出记录页面，获取列表 Task Name文本")
    def get_task_name_text(self):
        task_name = self.element_text(user['获取任务名称文本'])
        return task_name

    @allure.step("导出记录页面，获取列表 Task Name文本")
    def get_file_size_text(self):
        file_size = self.element_text(user['获取文件大小文本'])
        file_size1 = file_size[0:1]
        return file_size1

    @allure.step("导出记录页面，获取列表 User ID文本")
    def get_task_user_id_text(self):
        user_id = self.element_text(user['获取用户ID文本'])
        return user_id

    @allure.step("导出记录页面，获取列表 Create Date文本")
    def get_create_date_text(self):
        self.scroll_into_view(user['获取创建日期文本'])
        create_date = self.element_text(user['获取创建日期文本'])
        create_date1 = create_date[0:10]
        return create_date1

    @allure.step("导出记录页面，获取列表Complete Date文本")
    def get_complete_date_text(self):
        complete_date = self.element_text(user['获取完成日期文本'])
        complete_date1 = complete_date[0:10]
        return complete_date1

    @allure.step("导出记录页面，获取列表 Operation文本")
    def get_export_operation_text(self):
        operation = self.element_text(user['获取操作按钮文本'])
        return operation

    @allure.step("导出记录页面，获取列表导出时间文本")
    def get_export_time_text(self):
        export_time = self.element_text(user['获取导出时间'])
        export_time1 = export_time[0:1]
        return export_time1

    @allure.step("断言分页总数是否存在数据")
    def assert_total(self, total):
        if int(total) > 1000:
            logging.info("查看Shop Inventory IMEI Query列表，加载所有数据正常，分页总条数Total：{}".format(total))
        else:
            logging.info("查看Shop Inventory IMEI Query列表，加载所有数据正常，分页总条数Total：{}".format(total))

    @allure.step("断言分页总数是否存在数据")
    def assert_total2(self, total2):
        if int(total2) > 0:
            logging.info("查看Shop Inventory IMEI Query列表，加载所有数据正常，分页总条数Total：{}".format(total2))
        else:
            logging.info("查看Shop Inventory IMEI Query列表，加载所有数据正常，分页总条数Total：{}".format(total2))

    @allure.step("断言文件或导出时间是否有数据 ")
    def assert_file_time_size(self, file_size, export_time):
        if int(file_size) > 0:
            logging.info("Shop Inventory IMEI Query导出成功，File Size 导出文件大于1KB:{}".format(file_size))
        else:
            logging.info("Shop Inventory IMEI Query导出失败，File Size 导出文件小于1KB:{}".format(file_size))

        if int(export_time) > 0:
            logging.info("Shop Inventory IMEI Query导出成功，Export Time(s)导出时间大于0s:{}".format(export_time))
        else:
            logging.info("Shop Inventory IMEI Query导出失败，Export Time(s)导出时间小于0s:{}".format(export_time))

    @allure.step("断言精确查询结果 Customer PSI列表，字段列、字段内容是否与预期的字段内容值一致，有滚动条")
    def assert_shop_inventory_imei_field(self, header, content):
        DomAssert(self.driver).assert_search_contains_result(user['表格字段'], user['表格指定列内容'], header, content,
                                                             sc_element=user['水平滚动条'])


if __name__ == '__main__':
    pass