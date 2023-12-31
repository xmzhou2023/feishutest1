from libs.common.time_ui import sleep
from project.DCR_INDIA.page_object.Center_Component import LoginPage
from project.DCR_INDIA.page_object.AttendanceVisiting_VisitRecord import VisitRecordPage
from public.base.assert_ui import ValueAssert
import datetime
import logging
from public.base.basics import Base
import pytest
import allure

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

@allure.feature("考勤&巡店-巡店记录")
class TestQueryVisitRecord:
    @allure.story("巡店记录")
    @allure.title("巡店记录页面，根据门店ID查询巡店记录列表数据加载")
    @allure.description("巡店记录页面，根据门店ID查询巡店记录列表数据加载，校验数据加载正常")
    @pytest.mark.smoke  # 用例标记
    @allure.severity("blocker")  # 分别为3种类型等级：blocker\critical\normal
    def test_001_001(self, drivers):
        #user.dcr_login(drivers, "testsupervisor", "dcr123456")
        user = LoginPage(drivers)
        """打开考勤与巡店管理-打开巡店记录页面"""
        user.click_menu("Attendance & Visiting", "Visit Record")
        all_visit = VisitRecordPage(drivers)
        all_visit.click_search()
        shop_id = all_visit.get_shop_id_text()
        all_visit.click_unfold()
        all_visit.input_shop_id_query(shop_id)
        all_visit.click_fold()
        all_visit.click_search()
        shop_id2 = all_visit.get_shop_id_text()
        submit_date = all_visit.get_submit_date_text()
        visit_date = all_visit.get_visit_date_text()
        operation = all_visit.get_view_operation_text()
        total = all_visit.get_total_text()
        """断言查询巡店记录列表字段内容是否正确"""
        ValueAssert.value_assert_equal(shop_id, shop_id2)
        ValueAssert.value_assert_IsNoneNot(submit_date)
        ValueAssert.value_assert_IsNoneNot(visit_date)
        ValueAssert.value_assert_In(operation, "View")
        all_visit.assert_total(total)
        all_visit.click_reset()


    @allure.story("巡店记录")
    @allure.title("巡店记录页面，按Shop ID条件筛选，导出筛选后的巡店记录")
    @allure.description("巡店记录页面，按Shop ID条件筛选，导出筛选后的巡店记录，断言导出数据是否正常")
    @allure.severity("blocker")  # 分别为3种类型等级：blocker\critical\normal
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_export_fixture')
    def test_001_002(self, drivers):
        """获取当天日期"""
        user = LoginPage(drivers)
        export = VisitRecordPage(drivers)
        today = export.get_datetime_today()
        user.click_menu("Attendance & Visiting", "Visit Record")
        last_date = export.get_last_day(1)
        """根据提交时间筛选巡店记录"""
        export.input_submit_start_date(last_date)
        export.click_sales_region()
        export.click_search()
        export.click_export()
        export.click_download_more()
        export.input_task_name('Visit Record')
        export.export_record_create_date_query(today)
        """循环点击查询按钮，直到获取到Download Status字段的状态更新为COMPLETE"""
        down_status = export.click_export_search()
        task_name = export.get_task_name_text()
        file_size = export.get_file_size_text()
        task_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        complete_date = export.get_complete_date_text()
        export_time = export.get_export_time_text()
        operation = export.get_export_operation_text()
        """断言导出记录列表字段内容是否正确"""
        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "Visit Record")
        ValueAssert.value_assert_equal(task_id, "testsupervisor")
        ValueAssert.value_assert_equal(create_date, today)
        ValueAssert.value_assert_equal(complete_date, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)


if __name__ == '__main__':
    pytest.main(['AttendanceVisiting_VisitRecord.py'])
