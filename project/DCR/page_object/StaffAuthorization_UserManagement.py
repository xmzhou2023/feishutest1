from libs.common.read_element import Element
from public.base.basics import Base
from libs.common.time_ui import sleep
from ..test_case.conftest import *
import random

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class UserManagementPage(Base):
    """UserManagementPage 页面元素类"""

    @allure.step("user management页面，点击Add新增按钮")
    def click_add_user(self):
        self.is_click(user['Add'])
        sleep(2.5)

    @allure.step("进入Add user页面， 选择传音员工类型")
    def click_staff_type_value(self, type1):
        self.presence_sleep_dcr(user['Staff Type'])
        self.is_click(user['Staff Type'])
        sleep(1)
        self.is_click(user['Transsion Staff'], type1)

    @allure.step("Add user页面， 输入user ID字段")
    def input_user_id(self, content):
        self.is_click(user['User ID'])
        self.input_text_dcr(user['User ID'], txt=content)

    @allure.step("Add user页面， 输入user Name字段")
    def input_user_name(self, content):
        self.presence_sleep_dcr(user['User Name'])
        self.is_click(user['User Name'])
        self.input_text(user['User Name'], txt=content)

    @allure.step("Add user页面，点击user Name属性，释放光标")
    def click_user_name(self):
        self.is_click(user['User Name'])

    @allure.step("Add user页面， 输入销售区域，然后选中输入的销售区域")
    def input_sales_region(self, content):
        self.is_click(user['Sales Region'])
        self.input_text(user['Sales Region'], txt=content)
        sleep(2)
        self.is_click(user['Sales Region Value'])

    @allure.step("Add user页面， 输入国家城市，然后选中输入的国家城市")
    def input_country_city(self, content):
        self.is_click(user['Country City'])
        self.input_text(user['Country City'], txt=content)
        sleep(2)
        self.is_click(user['Country City Value'])

    @allure.step("Add user页面，选择点击品牌")
    def click_select_brand(self):
        self.is_click(user['Add Select Brand'])
        sleep(1)
        self.presence_sleep_dcr(user['Select Brand Value'], 'Infinix')
        self.is_click(user['Select Brand Value'], 'Infinix')
        self.is_click(user['Select Brand Value'], 'TECNO')
        self.is_click(user['Select Brand Value'], 'itel')


    @allure.step("关闭User Management菜单")
    def click_close_user_mgt(self):
        self.is_click(user['关闭用户管理菜单'])
        sleep(1)

    @allure.step("Edit user页面，选择点击品牌")
    def click_edit_trans_brand(self):
        self.is_click(user['Edit Select Brand'])
        sleep(1)
        self.presence_sleep_dcr(user['Select Brand Value'], 'oraimo')
        self.is_click(user['Select Brand Value'], 'oraimo')

    @allure.step("Edit user页面，选择点击品牌")
    def click_edit_dealer_brand(self):
        self.is_click(user['Edit Select Brand'])
        sleep(1)
        self.presence_sleep_dcr(user['Select Brand Value'], 'Infinix')
        self.is_click(user['Select Brand Value'], 'Infinix')

    @allure.step("Add user页面，输入职位，选中输入的职位")
    def input_position_transsion(self, content):
        self.is_click(user['Position'])
        self.input_text(user['Position'], txt=content)
        sleep(1)
        self.presence_sleep_dcr(user['Position Value Transsion'], content)
        self.is_click(user['Position Value Transsion'], content)

    @allure.step("Add user页面，输入上级领导，选中输入的上级领导")
    def input_superior(self, content):
        self.is_click(user['Superior'])
        self.input_text(user['Superior'], txt=content)
        sleep(2.5)
        self.presence_sleep_dcr(user['Superior Value'], "lhmadmin lhmadmin")
        self.is_click(user['Superior Value'], "lhmadmin lhmadmin")

    @allure.step("Add user页面，输入邮箱")
    def input_email(self, content):
        self.is_click(user['Email'])
        self.input_text(user['Email'], txt=content)

    @allure.step("Add user页面，输入联系电话")
    def input_contact_no(self, content):
        self.input_text(user['Contact No'], txt=content)

    @allure.step("Add user页面，选择性别")
    def click_gender_female(self, context):
        self.is_click(user['Gender'])
        sleep(1)
        self.presence_sleep_dcr(user['Gender Female'], context)
        self.is_click(user['Gender Female'], context)

    @allure.step("Add user页面，点击Submit提交按钮")
    def click_add_user_submit(self):
        self.is_click(user['Add User Submit'])
        sleep(1.5)

    @allure.step("获取列表User ID文本内容")
    def get_text_user_id(self):
        self.presence_sleep_dcr(user['获取列表文本User ID'])
        userid = self.element_text(user['获取列表文本User ID'])
        return userid

    @allure.step("'获取列表User Name文本内容")
    def get_text_user_name(self):
        username = self.element_text(user['获取列表文本User Name'])
        return username

    @allure.step("输入user ID属性筛选")
    def input_query_userid(self, content1):
        self.is_click(user['Input User ID'])
        self.input_text(user['Input User ID'], txt=content1)
        sleep(1)
        self.is_click(user['User ID Value'])

    @allure.step("点击搜索功能")
    def click_search(self):
        self.is_click(user['Search'])
        sleep(4)

    @allure.step("点击重置按钮")
    def click_reset(self):
        self.is_click(user['Reset'])
        sleep(3)


    """编辑用户时，筛选用户"""
    @allure.step("用户管理列表页面，筛选User，进行编辑或者删除")
    def input_query_User(self, content):
        self.is_click_dcr(user['点击筛选用户输入框'])
        self.input_text_dcr(user['点击筛选用户输入框'], txt=content)
        sleep(3)
        self.is_click(user['Input User ID Value'], content)

    @allure.step("点击编辑功能")
    def click_edit(self):
        self.presence_sleep_dcr(user['修改第一个Edit'])
        self.is_click_dcr(user['修改第一个Edit'])
        sleep(2)

    @allure.step("点击第一个checkbox,对用户进行辞职操作")
    def click_first_checkbox(self):
        self.is_click(user['勾选第一个复选框'])

    @allure.step("编辑用户提交成功提示语")
    def get_set_up_successfully(self):
        set_up_success = self.element_text(user['Set Up Successfully'])
        return set_up_success

    @allure.step("点击更多操作,点击离职功能")
    def click_more_option_quit(self):
        self.is_click(user['More Option'])
        sleep(2)
        self.presence_sleep_dcr(user['Quit'])
        self.is_click(user['Quit'])
        sleep(3)
        self.is_click(user['确认删除Yes'])

    @allure.step("获取无数据文本")
    def get_text_nodata(self):
        nodata = self.element_text(user['No Data'])
        return nodata

    @allure.step("获取删除成功提示语文本内容")
    def get_text_delete_success(self):
        del_success = self.element_text(user['Disabled Successfully'])
        return del_success

    # @allure.step("进入Add user页面， 选择代理员工类型")
    # def click_dealer_staff(self):
    #     self.is_click(user['Staff Type'])
    #     sleep(0.5)
    #     self.is_click(user['Dealer Staff'])

    @allure.step("进入Add user页面， 输入客户ID")
    def input_belong_to_cust(self, content):
        self.is_click(user['Belong To Customer'])
        self.input_text(user['Belong To Customer'], txt=content)
        sleep(2)
        self.is_click(user['Belong To Customer Value'], "UG4019912")

    @allure.step("随机生成userid")
    def user_id_random(self):
        num = str(random.randint(100, 999))
        userid = '19851' + num
        return userid

    @allure.step("随机生成username")
    def user_name_random(self):
        num = str(random.randint(100, 999))
        username = "user_test" + num
        return username

    @allure.step("随机生成电话号码尾号")
    def number_radom(self):
        num = str(random.randint(100, 999))
        return num

    @allure.step("Add user页面，输入职位，选中输入的职位")
    def input_position_dealer(self, content):
        self.is_click(user['Position'])
        self.input_text(user['Position'], txt=content)
        sleep(1)
        self.is_click(user['Position Value Dealer'], content)


    """查询列表用户"""
    @allure.step("用户管理页面，获取列表文本内容方法")
    def input_get_data(self, data):
        self.presence_sleep_dcr(user[data])
        get_data = self.element_text(user[data])
        return get_data

    @allure.step("用户管理页面，获取列表Total分页总数")
    def get_total(self):
        get_total = self.element_text(user['Get Total'])
        get_total1 = get_total[6:]
        return get_total1

    @allure.step("断言分页总数是否存在数据")
    def assert_total(self, total):
        if int(total) > 1000:
            logging.info("查看用户管理列表，分页总条数大于1000，用户总记录Total：{}".format(total))
        else:
            logging.info("查看用户管理列表，分页总条数小于1000，用户总记录Total：{}".format(total))


    """用户重置密码"""
    @allure.step("点击重置密码及重置密码确认功能")
    def click_more_reset_password(self):
        self.is_click(user['More Option'])
        sleep(2)
        self.presence_sleep_dcr(user['Reset Password'])
        self.is_click(user['Reset Password'])
        sleep(1.4)
        self.presence_sleep_dcr(user['Reset Password Yes'])
        self.is_click(user['Reset Password Yes'])

    @allure.step("登录时，弹出设置新密码窗口，获取New Password 标签")
    def get_new_password_label(self):
        get_new_password = self.element_text(user['Get New Password'])
        return get_new_password


    @allure.step("重置密码成功后，该用户登录时，弹出设置新密码窗口，输入新密码与确认新密码，并点击保存按钮")
    def input_new_password_save(self, new_password):
        self.is_click(user['Input New Password'])
        self.input_text(user['Input New Password'], txt=new_password)
        sleep(1)
        self.is_click(user['Input Confirm Password'])
        self.input_text(user['Input Confirm Password'], txt=new_password)
        sleep(0.5)
        self.is_click(user['New Password Save'])

    @allure.step("输入新密码登录，点击OK")
    def click_save_successfully_ok(self):
        self.is_click(user['Save successfully OK'])
        sleep(2)

    @allure.step("登录页面，输入新设置的密码")
    def input_login_password(self, password):
        self.is_click(user['login Input Password'])
        self.input_text(user['login Input Password'], txt=password)

    @allure.step("登录页面，点击Login登录按钮")
    def click_login(self):
        self.is_click(user['Click Login'])
        sleep(3.5)


    """导出用户"""
    @allure.step("User Management页面，点击Export 导出用户记录")
    def click_export(self):
        self.is_click(user['Export'])
        sleep(1.5)

    @allure.step("Attendance Records页面，导出操作后，点击右上角下载图标,点击右上角more...")
    def click_download_more(self):
        self.is_click(user['Download Icon'])
        sleep(2)
        self.presence_sleep_dcr(user['More'])
        self.is_click(user['More'])
        sleep(3)

    @allure.step("输入Task Name筛选该任务的导出记录")
    def input_task_name(self, content):
        self.is_click(user['Input Task Name'])
        self.input_text(user['Input Task Name'], txt=content)
        sleep(2)
        self.is_click(user['Task Name value'], content)

    @allure.step("循环点击查询，直到获取到下载状态为COMPLETE")
    def click_export_search(self):
        download_status = self.export_download_status(user['Export Record Search'], user['获取下载状态文本'])
        return download_status

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
    def get_operation_text(self):
        operation = self.element_text(user['获取操作按钮文本'])
        return operation

    @allure.step("导出记录页面，获取列表导出时间文本")
    def get_export_time_text(self):
        export_time = self.element_text(user['获取导出时间'])
        export_time1 = export_time[0:1]
        return export_time1

    @allure.step("断言分页总数是否存在数据")
    def assert_total(self, total):
        if int(total) > 0:
            logging.info("筛选考勤记录列表，分页总条数大于0，能查询到考勤记录数Total:{}".format(total))
        else:
            logging.info("筛选考勤记录列表，分页总条数为0，未查询到考勤记录数Total:{}:".format(total))

    @allure.step("断言分页总数是否存在数据")
    def assert_total2(self, total):
        if int(total) > 1000:
            logging.info("查看考勤记录列表，分页总条数大于1000，能查询到考勤记录Total：{}".format(total))
        else:
            logging.info("查看考勤记录列表，分页总条数为1000，未查询到考勤记录Total：{}".format(total))

    @allure.step("断言文件或导出时间是否有数据")
    def assert_file_time_size(self, file_size, export_time):
        if int(file_size) > 0:
            logging.info("Attendance Records导出成功，File Size导出文件大于M:{}".format(file_size))
        else:
            logging.info("Attendance Records导出失败，File Size导出文件小于M:{}".format(file_size))

        if int(export_time) > 0:
            logging.info("Attendance Records导出成功，Export Time(s)导出时间大于0s:{}".format(export_time))
        else:
            logging.info("Attendance Records导出失败，Export Time(s)导出时间小于0s:{}".format(export_time))
        sleep(1)

    @allure.step("关闭导出记录菜单")
    def click_close_export_record(self):
        """关闭导出记录菜单"""
        self.is_click(user['关闭导出记录菜单'])
        sleep(1)


if __name__ == '__main__':
    pass