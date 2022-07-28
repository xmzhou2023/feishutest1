from libs.common.time_ui import sleep
from project.DCR_PROD.page_object.Center_Component import DCRLoginPage
from project.DCR_PROD.page_object.AttendanceVisiting_VisitRecord import VisitRecordPage
from public.base.assert_ui import ValueAssert
import datetime
import logging
from public.base.basics import Base
import pytest
import allure


@allure.feature("考勤&巡店-巡店记录")
class TestQueryVisitRecord:
    @allure.story("查询巡店记录")
    @allure.title("巡店记录页面，根据门店ID查询巡店记录列表数据加载")
    @allure.description("巡店记录页面，根据门店ID查询巡店记录列表数据加载，校验数据加载正常")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_001(self, drivers):
        base = Base(drivers)
        base.refresh()
        sleep(4.5)

        menu = DCRLoginPage(drivers)
        #user.dcr_login(drivers, "testsupervisor", "dcr123456")

        """打开考勤与巡店管理-打开巡店记录页面"""
        menu.click_gotomenu("Attendance & Visiting", "Visit Record")
        all_visit = VisitRecordPage(drivers)

        shop_id = all_visit.get_shop_id_text()
        all_visit.click_unfold()
        all_visit.input_shop_id_query(shop_id)
        all_visit.click_fold()
        all_visit.click_search()

        shopid = all_visit.get_shop_id_text()
        submit_date = all_visit.get_submit_date_text()
        visit_date = all_visit.get_visit_date_text()
        operation = all_visit.get_view_operation_text()
        total = all_visit.get_total_text()

        ValueAssert.value_assert_equal(shop_id, shopid)
        ValueAssert.value_assert_IsNoneNot(submit_date)
        ValueAssert.value_assert_IsNoneNot(visit_date)
        ValueAssert.value_assert_In(operation, "View")
        all_visit.assert_total(total)
        all_visit.click_reset()


@allure.feature("考勤&巡店-巡店记录")
class TestExportVisitRecord:
    @allure.story("导出巡店记录")
    @allure.title("巡店记录页面，按Shop ID条件筛选，导出筛选后的巡店记录")
    @allure.description("巡店记录页面，按Shop ID条件筛选，导出筛选后的巡店记录，断言导出数据是否正常")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_002_001(self, drivers):
        """获取当天日期"""
        base = Base(drivers)
        today = base.get_datetime_today()

        export = VisitRecordPage(drivers)
        """根据提交时间筛选巡店记录"""
        export.input_submit_start_date(today)
        export.click_sales_region()
        export.click_search()

        export.click_export()
        export.click_download_more()
        down_status = export.click_export_search()

        task_name = export.get_task_name_text()
        file_size = export.get_file_size_text()
        file_size1 = file_size[0:1]
        task_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        create_date1 = create_date[0:10]
        complete_date = export.get_complete_date_text()
        complete_date1 = complete_date[0:10]
        export_time = export.get_export_time_text()
        export_time1 = export_time[0:1]
        operation = export.get_export_operation_text()

        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "History List")
        ValueAssert.value_assert_equal(task_id, "testsupervisor")
        ValueAssert.value_assert_equal(create_date1, today)
        ValueAssert.value_assert_equal(complete_date1, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size1, export_time1)

        export.click_close_export_record()
        export.click_close_visit_record()


if __name__ == '__main__':
    pytest.main(['AttendanceVisiting_VisitRecord.py'])
