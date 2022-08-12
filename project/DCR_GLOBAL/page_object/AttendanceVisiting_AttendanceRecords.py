import time

from libs.common.read_element import Element
from libs.common.time_ui import sleep
from public.base.basics import Base
import datetime
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class AttendanceRecordPage(Base):
    """ AttendanceRecord类，生产环境，Attendance Records考勤记录页面元素定位"""
    def input_user_id_query(self, content, content1):
        """Attendance Records页面，输入User ID筛选用户的考勤记录"""
        self.is_click_dcr(user['筛选用户'])
        sleep(1)
        self.input_text_dcr(user['筛选用户'], txt=content)
        sleep(3)
        self.is_click_dcr(user['Select User Value'], content1)

    def input_query_date(self, content):
        self.is_click(user['筛选开始日期'])
        sleep(1)
        self.input_text(user['筛选开始日期'], txt=content)

    def click_search(self):
        """Attendance Records页面，点击Seasrch筛选考勤记录"""
        self.is_click(user['Search'])

    def click_reset(self):
        """Attendance Records页面，点击Reset重置筛选条件"""
        self.is_click(user['Reset'])
        sleep(5)


    def get_photo_text(self):
        """Attendance Records页面，获取列表Picture文本"""
        Base.presence_sleep_dcr(self, user['获取列表photo文本'])
        photo = self.element_text(user['获取列表photo文本'])
        return photo

    def get_date_text(self):
        """Attendance Records页面，获取列表Date日期文本"""
        date = self.element_text(user['获取列表日期文本'])
        return date

    def get_user_id_text(self):
        """Attendance Records页面，获取列表User ID文本"""
        Base.presence_sleep_dcr(self, user['获取列表UserID文本'])
        userid = self.element_text(user['获取列表UserID文本'])
        return userid

    def get_total_text(self):
        """Attendance Records页面，获取列表Total总条数文本"""
        total = self.element_text(user['获取总条数文本'])
        return total

    def click_close_export_record(self):
        """关闭导出记录菜单"""
        self.is_click(user['关闭导出记录菜单'])
        sleep(1)

    def click_close_atten_record(self):
        """关闭考勤记录菜单"""
        self.is_click(user['关闭考勤记录菜单'])
        sleep(2)

    def get_home_page_cust(self):
        homepage = self.element_text(user['Get Home Page Customer'])
        return homepage


    """导出考勤记录功能"""
    def click_export(self):
        """Attendance Records页面，点击Export 导出考勤记录"""
        self.is_click(user['Export'])
        sleep(2)

    def click_download_more(self):
        """导出操作后，点击右上角下载图标,点击右上角more..."""
        self.is_click(user['Download Icon'])
        sleep(1)
        Base.presence_sleep_dcr(self, user['More'])
        self.is_click(user['More'])
        sleep(4)

    def click_export_search(self):
        """循环点击查询，直到获取到下载状态为COMPLETE """
        down_status = Base.export_download_status(self, user['Export Record Search'], user['获取下载状态文本'])
        return down_status


    def get_download_status_text(self):
        """导出记录页面，获取列表 Download Status文本"""
        status = self.find_element(user['获取下载状态文本'])
        while status != "COMPLETE":
            status1 = self.element_text(user['获取下载状态文本'])
            return status1

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

    def get_operation_text(self):
        """导出记录页面，获取列表 Operation文本"""
        operation = self.element_text(user['获取操作按钮文本'])
        return operation

    def get_export_time_text(self):
        """导出记录页面，获取列表导出时间文本"""
        export_time = self.element_text(user['获取导出时间'])
        return export_time

    def assert_total(self, total):
        """断言分页总数是否存在数据"""
        if int(total) > 0:
            logging.info("筛选考勤记录列表，分页总条数大于0，能查询到考勤记录数Total:{}".format(total))
        else:
            logging.info("筛选考勤记录列表，分页总条数为0，未查询到考勤记录数Total:{}:".format(total))

    def assert_total2(self, total):
        """断言分页总数是否存在数据"""
        if int(total) > 1000:
            logging.info("查看考勤记录列表，分页总条数大于1000，能查询到考勤记录Total：{}".format(total))
        else:
            logging.info("查看考勤记录列表，分页总条数为1000，未查询到考勤记录Total：{}".format(total))
        sleep(1)

    def assert_file_time_size(self, file_size, export_time):
        """断言文件或导出时间是否有数据 """
        if int(file_size) > 0:
            logging.info("Attendance Records导出成功，File Size导出文件大于M:{}".format(file_size))
        else:
            logging.info("Attendance Records导出失败，File Size导出文件小于M:{}".format(file_size))

        if int(export_time) > 0:
            logging.info("Attendance Records导出成功，Export Time(s)导出时间大于0s:{}".format(export_time))
        else:
            logging.info("Attendance Records导出失败，Export Time(s)导出时间小于0s:{}".format(export_time))


if __name__ == '__main__':
    pass



