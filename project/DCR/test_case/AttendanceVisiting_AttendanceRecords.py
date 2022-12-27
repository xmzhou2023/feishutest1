from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.AttendanceVisiting_AttendanceRecords import AttendanceRecordPage
from public.base.assert_ui import ValueAssert, DomAssert
import logging
from libs.common.time_ui import sleep
from public.base.basics import Base
import datetime
import pytest
import allure

"""后置关闭菜单方法"""
@pytest.fixture(scope='function')
def function_export_fixture(drivers):
    yield
    menu = LoginPage(drivers)
    for i in range(2):
        get_menu_class = menu.get_open_menu_class()
        class_value = "tags-view-item router-link-exact-active router-link-active active"
        if class_value == str(get_menu_class):
            menu.click_close_open_menu()
            sleep(1)

@pytest.fixture(scope='function')
def function_menu_fixture(drivers):
    yield
    menu = LoginPage(drivers)
    get_menu_class = menu.get_open_menu_class()
    class_value = "tags-view-item router-link-exact-active router-link-active active"
    if class_value == str(get_menu_class):
        menu.click_close_open_menu()

@allure.feature("考勤&巡店-考勤记录")
class TestQueryAttendanceRecord:
    @allure.story("查询考勤记录")
    @allure.title("考勤记录页面，查询考勤记录列表数据加载")
    @allure.description("考勤记录页面，查询考勤记录列表数据加载，断言数据加载正常")
    @allure.severity("blocker")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """考勤管理-打开考勤记录页面"""
        user.click_gotomenu("Attendance & Visiting", "Attendance Records")
        """查询考勤记录列表，是否存在当天考勤记录"""
        query_all = AttendanceRecordPage(drivers)
        sleep(2)
        picture = query_all.get_photo_text()
        logging.info("获取考勤记录列表的Picture文本内容{}".format(picture))
        date = query_all.get_date_text()
        total = query_all.get_total_text()
        """断言查询的列表数据是否存在，分页下面的总条数是否有数据"""
        ValueAssert.value_assert_equal(picture, "Picture")
        ValueAssert.value_assert_IsNoneNot(date)
        query_all.assert_total2(total)
        #query_all.click_close_atten_record()


    @allure.story("查看考勤照片详情")
    @allure.title("考勤记录页面，查看筛选用户的考勤照片详情")
    @allure.description("考勤记录页面，查询筛选用户的，考勤照片详情")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_002(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """考勤管理-打开考勤记录页面"""
        user.click_gotomenu("Attendance & Visiting", "Attendance Records")
        """查询某个用户的，当天考勤记录用例"""
        picture = AttendanceRecordPage(drivers)
        """ 获取列表User Name """
        user_id = picture.get_user_id_text()
        """ 获取列表User Name """
        user_name = picture.get_user_name_text()
        userid_name = user_id + " " + user_name
        """根据UserID+UserName条件精确筛选数据"""
        picture.input_user_id_query(user_id, userid_name)
        picture.click_search()
        picture.click_view_picture_button()
        DomAssert(drivers).assert_att('Attendance Photo')
        get_photo_user_id = picture.get_attendance_photo_user_id(user_id)
        get_standard = picture.get_standard_photo()
        ValueAssert.value_assert_In(user_id, get_photo_user_id)
        ValueAssert.value_assert_In('Standard Photo', get_standard)
        picture.click_close_attendance_photo()


@allure.feature("考勤&巡店-考勤记录")
class TestExportAttendanceRecord:
    @allure.story("导出考勤记录")
    @allure.title("考勤记录页面，导出筛选用户的当天考勤记录")
    @allure.description("考勤记录页面，查询某个用户的，当天考勤记录，然后导出筛选的考勤记录")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_export_fixture')
    def test_002_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """考勤管理-打开考勤记录页面"""
        user.click_gotomenu("Attendance & Visiting", "Attendance Records")
        """查询某个用户的，当天考勤记录用例"""
        export = AttendanceRecordPage(drivers)
        """获取当天日期"""
        base = Base(drivers)
        today = base.get_datetime_today()
        """ 获取列表User Name """
        user_id = export.get_user_id_text()
        """ 获取列表User Name """
        user_name = export.get_user_name_text()
        userid_name = user_id + " " + user_name
        """根据UserID+UserName条件精确筛选数据"""
        export.input_user_id_query(user_id, userid_name)
        export.click_search()
        picture = export.get_photo_text()
        date = export.get_date_text()
        userid = export.get_user_id_text()
        username = export.get_user_name_text()
        total = export.get_total_text()
        """断言查询的列表数据是否存在，分页下面的总条数是否有数据"""
        ValueAssert.value_assert_In(picture, "Picture")
        ValueAssert.value_assert_equal(user_id, userid)
        ValueAssert.value_assert_equal(user_name, username)
        ValueAssert.value_assert_equal(today, date)
        export.assert_total(total)
        """点击导出"""
        export.click_export()
        export.click_download_more()
        export.input_task_name("Attendance Records")
        """循环点击查询按钮，直到获取到Download Status字段的状态更新为COMPLETE"""
        down_status = export.click_export_search()
        task_name = export.get_task_name_text()
        file_size = export.get_file_size_text()
        task_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        complete_date = export.get_complete_date_text()
        export_time = export.get_export_time_text()
        operation = export.get_operation_text()
        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "Attendance Records")
        ValueAssert.value_assert_equal(task_id, "lhmadmin")
        ValueAssert.value_assert_equal(create_date, today)
        ValueAssert.value_assert_equal(complete_date, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)
        #export.click_close_export_record()
        #export.click_close_atten_record()


if __name__ == '__main__':
    pytest.main(['AttendanceVisiting_AttendanceRecords.py'])
