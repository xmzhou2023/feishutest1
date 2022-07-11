from libs.common.read_element import Element
from public.base.basics import Base
from libs.common.time_ui import sleep
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class UserShopAssociaPage(Base):
    """ User and Shop Association 菜单定位元素类"""
    def input_user_query(self, content):
        """进入User and Shop Association页面，根据User筛选品牌、客户等数据"""
        self.is_click_dcr(user['Input User'])
        self.input_text_dcr(user['Input User'], txt=content)
        sleep(2)
        self.is_click(user['User Select Value'])

    def click_search(self):
        """ 点击Search按钮筛选数据 """
        self.is_click(user['Search'])
        sleep(2)

    def get_total_text(self):
        """ 获取分页总条数文本 """
        get_total = self.element_text(user['Get Total Text'])
        return get_total

    def get_list_user_id(self):
        """ 获取列表User ID文本 """
        get_userid = self.element_text(user['Get list User ID'])
        return get_userid

    def get_list_user_name(self):
        """ 获取列表User Name文本 """
        get_username = self.element_text(user['Get list User Name'])
        return get_username

    def get_list_position(self):
        """ 获取列表Position文本 """
        get_position = self.element_text(user['Get list Position'])
        return get_position

    def get_list_shop_id(self):
        """ 获取列表Shop ID文本 """
        shop_id = self.element_text(user['Get list Shop ID'])
        return shop_id

    def get_list_shop_name(self):
        """ 获取列表Shop Name文本 """
        shop_name = self.element_text(user['Get list Shop Name'])
        return shop_name

    def click_export(self):
        """ 点击Export导出按钮 """
        self.is_click(user['Export'])


    # User and Shop Association列表数据筛选后，导出操作成功后验证
    def click_download_icon(self):
        self.is_click(user['Download Icon'])

    def click_more(self):
        """点击more更多按钮"""
        self.is_click(user['More'])
        sleep(3)

    def click_export_search(self):
        """导出页面，点击Search按钮"""
        self.is_click(user['Export Record Search'])
        sleep(3)

    def get_download_status_text(self):
        """导出记录页面，获取列表 Download Status文本"""
        status = self.element_text(user['获取下载状态文本'])
        return status

    def get_task_name_text(self):
        """导出记录页面，获取列表 Task Name文本"""
        task_name = self.element_text(user['获取任务名称文本'])
        return task_name

    def get_file_size_text(self):
        """导出记录页面，获取列表 Task Name文本"""
        file_size = self.element_text(user['获取文件大小文本'])
        return file_size

    def get_task_user_id_text(self):
        """导出记录页面，获取列表 User ID文本"""
        user_id = self.element_text(user['获取用户ID文本'])
        return user_id

    def get_create_date_text(self):
        """导出记录页面，获取列表 Create Date文本"""
        create_date = self.element_text(user['获取创建日期文本'])
        return create_date

    def get_complete_date_text(self):
        """导出记录页面，获取列表Complete Date文本"""
        complete_date = self.element_text(user['获取完成日期文本'])
        return complete_date

    def get_export_operation_text(self):
        """导出记录页面，获取列表 Operation文本"""
        operation = self.element_text(user['获取操作按钮文本'])
        return operation

    def get_export_time_text(self):
        """导出记录页面，获取列表导出时间文本"""
        export_time = self.element_text(user['获取导出时间'])
        return export_time


if __name__ == '__main__':
    pass