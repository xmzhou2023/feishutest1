'''项目管理-创建项目'''
import logging

from project.IPM.page_base.basics_IPM import PubicMethod
from libs.common.time_ui import *
from project.IPM.page_base.assert_pubic import *
from project.IPM.api.APIRequest import *
import random
from project.IPM.page_object.ipm_publiclibrary import *
from project.IPM.page_object.ApplicationCenter import ApplicationCenter





now_times = strftime('%Y-%m-%d%H:%M:%S')
now_t = strftime('%Y-%m-%d')
time_ipm=f'ipm自动化{now_times}'

class CreateProject(ipm_publiclibrary):

    def __init__(self,driver,env_name,element_yaml='ProjectManagement',expect='ProjectManagement.yaml'):
        super().__init__(driver, element_yaml,expect=expect)
        self.Api = APIRequest(env_name)
        self.ini = ReadConfig(pro_name, env_name)
    @allure.step("鼠标悬停")
    def mouse_hover__IPM(self,element,choice=None):
        self.mouse_hover_IPM(element,choice)

    @allure.step("项目管理_url")
    def get_url_project(self):
        # self.get_url(f"http://ipm-uat.transsion.com/#/project-manage")
        self.get_url(f"{self.ini._get('HOST', 'url_ipm')}/#/project-manage")
        sleep(2)

    @allure.step("项目管理")
    def click_project(self):
        '''
        点击项目管理
        '''
        self.click_IPM('项目管理')
        sleep(2)

    @allure.step("项目管理_新增")
    def click_add(self):
        '''点击新增'''
        self.click_IPM('新增')
        sleep(2)

    @allure.step("项目管理_新增_选择模板")
    def Select_Template(self,choice):
        '''
        选择模板
        :param choice：模板名字（IT项目模板，IT需求项目模板等）
        '''
        self.click_IPM('选择模板',choice=choice)
        sleep(2)

    @allure.step("项目管理_新增_项目名称")
    def projecy_name(self,nametext):
        '''项目名字'''
        self.input_text_IPM('项目名称',nametext)
        sleep(2)

    @allure.step("项目管理_新增_项目描述")
    def projecy_Description(self,Descriptiontext=None):
        '''项目描述'''
        self.input_text_IPM('项目描述',text=Descriptiontext)
        sleep(2)
    @allure.step("项目管理_新增_保存")
    def projecy_preservation(self):
        '''保存'''
        self.click_IPM('保存')

    @allure.step("项目管理_新增_取消")
    def projecy_cancel(self):
        '''取消'''
        self.click_IPM('取消')

    @allure.step("项目管理_进入详情")
    def click_project_entrance(self,projectname):
        '''点击卡片进入项目'''
        self.click_IPM('进入项目',projectname)


    @allure.step("项目管理_卡片_展开编辑/删除按钮")
    def click_project_entrance_ch(self,projectname):
        '''点击...展开编辑/删除按钮'''
        self.mouse_hover_IPM('卡片展开按钮',projectname)

    @allure.step("项目管理_卡片_展开编辑")
    def entrance_ch(self,):
        '''项目编辑按钮'''
        self.click_IPM('项目编辑按钮')

    @allure.step("项目管理_卡片_删除按钮")
    def delete_project(self,):
        '''项目编辑按钮'''
        self.click_IPM('项目删除按钮')

    @allure.step("项目管理_卡片_展开删除按钮_删除询问窗口_点击确认")
    def delete_project_determine(self, ):
        '''删除项目点击确认'''
        self.click_IPM('删除确定')

    @allure.step("项目管理_卡片_展开删除按钮_删除询问窗口_点击取消")
    def delete_project_cancel(self, ):
        '''删除项目点击取消'''
        self.click_IPM('删除取消')

    @allure.step("项目管理_项目详情_编辑")
    def click_edit(self):
        '''编辑'''
        self.click_IPM('编辑')
    @allure.step("项目管理_项目详情_编辑_保存")
    def perject_field_editing_save(self):

        '''基本信息编辑保存'''
        self.click_IPM('基本信息保存')
    @allure.step("项目管理_项目详情_启动项目")
    def Start_project(self):
        '''启动项目'''
        self.click_IPM('启动项目')


    @allure.step("项目管理_项目详情_编辑_获取项目状态是否可编辑")
    def project_stu(self):
        '''获取项目状态是否可编辑'''
        sleep(2)
        res=self.find_element_IPM_yaml('字段名称', choice="项目状态")
        sleep(2)
        a =res.get_attribute("disabled")
        return a


    def get_Single_attribute(self,proname,domainbid=None):
        '''
        获取单个字段属性

        '''

        field_att = self.Api.Api_project_field(proname,domainbid)
        for i in field_att:
            if i.get("字段名称") == '项目状态':
                return i.get('是否可读')

    @allure.step("人员列表")
    def personnel_list(self,text,Confirm_or_Cancel=None):
        '''
        人员列表
        人员选择
        '''
        sleep(2)
        self.input_text_IPM("请输入姓名或工号",text)
        self.click_IPM("选择人员",text)
        if Confirm_or_Cancel == None or Confirm_or_Cancel == "确定":
            self.click_IPM("人员列表_确定")
        else:
            self.click_IPM("人员列表_取消")

    @allure.step("项目管理_项目详情_项目tab应用")
    def project_tab(self,tabname):
        '''
        点击项目tab应用
        :param tabname: 基本信息，计划，存储域，团队等
        '''
        self.click_IPM("tab应用",tabname)

    @allure.step("项目管理_项目详情_项目tab应用_计划_任务选择")
    def project_Task_selection(self,taskname):
        '''
        计划_任务选择
        :param taskname: 任务名称
        '''
        self.click_IPM("计划任务选择",taskname)
    @allure.step("项目管理_项目详情_项目tab应用_计划_任务展开")
    def project_Task_expansion(self,taskname):
        '''
        计划_任务展开
        :param taskname: 任务名称
        '''
        self.click_IPM("计划任务展开",taskname)
    @allure.step("项目管理_项目详情_项目tab应用_计划_计划任务更多操作")
    def project_more_actions(self,taskname,function):
        '''
        计划_计划任务更多操作/新增任务/打开任务抽屉
        :param taskname: 任务名称
        :param function: 子功能为（查看，新增，删除，取消阶段，设置里程碑，置灰等）
        '''
        self.mouse_hover_IPM("计划任务_任务名称",taskname)
        if function == '查看':
            self.click_IPM("计划任务_查看(打开任务抽屉)", taskname)

        if function == '新增':
            self.click_IPM("计划任务_新增", taskname)
        if function == '更多操作':
            self.mouse_hover_IPM("计划任务_更多操作", taskname)
            self.click_IPM("计划任务更多操作_子功能", function)


    @allure.step("项目管理_项目详情_项目tab应用_计划任务_保存")
    def project_Planned_Task_Save(self):
        '''
        计划任务_保存
        '''
        self.click_IPM("计划任务_保存")
        sleep(3)
    @allure.step("项目管理_项目详情_项目tab应用_计划任务_发起评审")
    def project_Scheduled_Tasks_Initiate_review(self):
        '''
        计划任务_发起评审
        '''
        self.click_IPM("计划任务_发起评审")
        sleep(0.5)
    @allure.step("项目管理_项目详情_项目tab应用_计划任务_预约上会")
    def project_Scheduled_Tasks_Make_an_appointment_for_a_meeting(self):
        '''
        计划任务_预约上会
        '''
        self.click_IPM("计划任务_预约上会")
    @allure.step("项目管理_项目详情_项目tab应用_计划任务_撤回预约")
    def project_Scheduled_Tasks_Withdrawal_of_appointment(self):
        '''
        计划任务_撤回预约
        '''
        self.click_IPM("计划任务_撤回预约")
    @allure.step("项目管理_项目详情_项目tab应用_计划任务_上会_可预约日期选择")
    def project_Reservable(self):
        '''
        计划任务_上会_可预约日期选择
        '''
        element_res=self.find_elemens_ipm_yaml_get_attribute('上会预约_获取可预约')
        if "可预约" in element_res:
            self.click_IPM("上会_预约")
        else:
            element_res6_01 = self.find_elemens_ipm_yaml_get_attribute('上会预约_获取下月6')
            element_res5_01 = self.find_elemens_ipm_yaml_get_attribute('上会预约_获取下月5')
            print(element_res5_01)
            if "01" in element_res5_01:
                self.click_IPM("上会预约_5_01")
                self.click_IPM("上会_预约")
            elif "01" in element_res6_01:
                self.click_IPM("上会预约_6_01")
                self.click_IPM("上会_预约")
            else:
                print('当前可查询的日历中不存01号，请继续在project_Reservable中扩展')
        sleep(2)



    @allure.step("项目管理_项目详情_项目tab应用_计划任务_上会_提交预约")
    def project_make_an_appointment(self):
        '''
        计划任务_上会_提交预约
        '''
        self.click_IPM("提交预约")
    @allure.step("项目管理_项目详情_项目tab应用_计划任务_上会_上会预约_取消")
    def project_Cancellation_of_meeting_appointment(self):
        '''
        计划任务_上会_上会预约_取消
        '''
        self.click_IPM("上会预约_取消")

    @allure.step("项目管理_项目详情_项目tab应用_计划任务_上会_上会预约_设置通知内容_发送通知")
    def project_SetNotificationContent_SendNotification(self):

        '''
        计划任务_上会_上会预约_设置通知内容_发送通知
        '''

        self.click_IPM("设置通知内容_发送通知")
    @allure.step("项目管理_项目详情_项目tab应用_计划任务_上会_上会预约_设置通知内容_取消")
    def project_SetNotificationContent_cancel(self):

        '''
        计划任务_上会_上会预约_设置通知内容_取消
        '''

        self.click_IPM("设置通知内容_取消")

    @allure.step("项目管理_项目详情_项目tab应用_计划任务_上会_上会预约")
    def project_Make_an_appointment_at_the_meeting(self,Appointment_or_cancellation=None):
        '''
        计划任务_上会预约，根据Appointment_or_cancellation传的值点击确认或取消
        '''

        self.project_Reservable()
        if Appointment_or_cancellation == "预约" or Appointment_or_cancellation ==None:
            self.project_make_an_appointment()

        else:
            self.project_Cancellation_of_meeting_appointment()

    @allure.step("项目管理_项目详情_项目tab应用_计划任务_发起评审_评审流程确认页_发起流程")
    def project_ReviewProcessConfirmationPage_InitiationProcess(self):
        '''
        评审流程确认页_发起流程
        '''

        self.click_IPM("评审流程确认页_发起流程")
    @allure.step("项目管理_项目详情_项目tab应用_计划任务_发起评审_评审流程确认页_发起流程关联任务_提示_确认")
    def project_ReviewProcessConfirmationPage_InitiationProcess_determine(self):
        '''
        评审流程确认页_发起流程
        '''

        self.click_IPM("评审流程确认页_发起流程_关联任务_提示_确认")
    @allure.step("项目管理_项目详情_项目tab应用_计划任务_发起评审_评审流程确认页_发起流程关联任务_提示_取消")
    def project_ReviewProcessConfirmationPage_InitiationProcess_cancel(self):
        '''
        评审流程确认页_发起流程
        '''

        self.click_IPM("评审流程确认页_发起流程_关联任务_提示_取消")
    @allure.step("项目管理_项目详情_项目tab应用_计划任务_发起评审_评审流程确认页_选取")
    def project_ReviewProcessConfirmationPage_selection(self):
        '''
        评审流程确认页_选取
        '''

        self.click_IPM("评审流程确认页_选取")

    def project_ReviewProcessConfirmationPage_selection_query_MarketName(self):
        '''
        评审流程确认页_选取
        '''

        self.click_IPM("评审流程确认页_选取_市场名")
    def project_ReviewProcessConfirmationPage_selection_query_ProjectName(self):
        '''
        评审流程确认页_选取
        '''

        self.click_IPM("评审流程确认页_选取_项目名")

    @allure.step("项目管理_项目详情_项目tab应用_计划任务_发起评审_评审流程确认页_选取_查询")
    def project_ReviewProcessConfirmationPage_InitiationProcess_query(self,projectname,Missionphase=None):
        '''
        评审流程确认页_选取_查询
        :param projectname: 项目名
        :param Missionphase: 任务阶段
        '''
        if Missionphase != None:
            self.click_IPM("评审流程确认页_选取_勾选（项目名+任务阶段）", projectname, Missionphase)
        else:
            self.click_IPM("评审流程确认页_选取_勾选（项目名）", projectname)





    def project_ReviewProcessConfirmationPage_selectiontask(self,MarketName=None,ProjectName=None,Drop_down_value=None,result=None,Query_Reset=None):
        '''
        评审流程确认页_选取
        :param MarketName: 项目名
        :param ProjectName: 任务阶段
        :param Drop_down_value: 项目名
        '''

        if Query_Reset =="查询":#查询功能查询按钮
            if MarketName != None:
                self.input_text_IPM("评审流程确认页_选取_市场名", MarketName)
            if ProjectName != None:
                self.input_text_IPM("评审流程确认页_选取_项目名", ProjectName)

            if Drop_down_value == "概念DCP" or \
                        Drop_down_value == "计划DCP" or \
                        Drop_down_value == "开发DCP" or \
                        Drop_down_value == "验证DCP" or \
                        Drop_down_value == "上市DCP" or \
                        Drop_down_value == "生命周期DCP":
                self.click_IPM("评审流程确认页_选取_任务阶段")
                self.DropDownBox("评审流程确认页_选取_任务阶段", "任务阶段", "字段名称", Drop_down_value)

            self.click_IPM("评审流程确认页_选取_查询")
            self.project_ReviewProcessConfirmationPage_InitiationProcess_query(ProjectName,Drop_down_value) #传入项目名和任务阶段获取唯一值
            if result == "确定" or result ==None:
                self.click_IPM("评审流程确认页_选取_确定")
            elif result == "取消":
                self.click_IPM("评审流程确认页_选取_取消")
            else:
                logging.info("当前传的{}不存在".format(result))
            sleep(1)
        elif Query_Reset == "重置": #查询功能重置按钮
            self.click_IPM("评审流程确认页_选取_重置")
        else: #跳过查询
            try:
                self.project_ReviewProcessConfirmationPage_InitiationProcess_query(ProjectName,Drop_down_value) #传入项目名和任务阶段获取唯一值
            except:
                self.click_IPM('评审流程确认页_选取_第一条')
            if result == "确定" or result ==None:
                self.click_IPM("评审流程确认页_选取_确定")
            elif result == "取消":
                self.click_IPM("评审流程确认页_选取_取消")
            else:
                logging.info("当前传的{}不存在".format(result))







    @allure.step("项目管理_项目详情_项目tab应用_计划任务_上会_上会预约_设置通知内容")
    def project_SetNotificationContent(self,Send_or_Cancel=None):

        '''
        计划任务_上会_上会预约_设置通知内容
        '''
        self.project_Reservable()
        if Send_or_Cancel == "发送" or Send_or_Cancel ==None:
            sleep(2)
            self.project_SetNotificationContent_SendNotification()

        else:
            self.project_SetNotificationContent_cancel()









    def project_Task_Edit_Name(self,taskname,*expansion_name1):
        '''
        点击任务名字编辑
        :param taskname: 编辑的任务名称
        :param expansion_name1: 展开的树结构名称
        '''

        if expansion_name1:
            for i in expansion_name1:
                self.project_Task_expansion(i)
        self.project_Task_selection(taskname)

    def project_Task_More_actions(self,taskname,function,*expansion_name1):
        '''
        打开任务的更多操作功能
        :param taskname: 编辑的任务名称
        :param function: 功能
        :param expansion_name1: 展开的任务树结构名称
        '''
        if expansion_name1:

            for i in expansion_name1:
                self.project_Task_expansion(i)
        self.project_more_actions(taskname, function)

    def elements_filelds(self):
        '''
        任务基本信息所有字段获取
        '''
        return self.find_elemens_ipm_yaml_get_attribute('任务基本信息')




    def Get_required_fields(self,proname,task_name,protime,Job_number_or_name=None,Confirm_or_Cancel=None,objectname=None):
        '''
        计划_任务字段获取
        :param proname: 项目名
        :param protime: 当前日期
        :param task_name: 任务名称
        :param Job_number_or_name: 员工姓名或工号
        :param Confirm_or_Cancel: 人员保存确定还是取消
        :param objectname: 对象名称
        Get_required_fields('项目名'，'任务名称'，'当前日期')
        '''


        field_att = self.Api.Api_project_task(proname,task_name,objectname)
        ele_res=self.elements_filelds()
        field = []
        for j in field_att:
            if j['字段名'] in ele_res:
                field.append(j)

        for i in field:
            if i.get("字段名") == "任务类型" or i.get("字段名")=="前置任务" or i.get("字段名")=="状态":
                logging.info("不需要传")
            else:
                if i.get("字段名") == "进度" or i.get("字段名")=="预估工时" or i.get("字段名")=="实际工时":
                    self.input_text_IPM('字段名称', text=random.randint(1, 100) , choice=i.get("字段名"))
                else:
                    logging.info(f"{i.get('字段名')} 是否展示：{i.get('是否展示')}")
                    if i.get("是否展示") == True:
                        logging.info(f"{i.get('字段名')} 是否可读：{i.get('是否可读')}")
                        if i.get("是否可读") == False:
                            logging.info(f"{i.get('字段名')} 是否必填：{i.get('是否必填')}")
                            if i.get("是否必填") == True:
                                logging.info(f"{i.get('字段名')} 类型：{i.get('类型')}")
                                if i.get("类型") == 'text':
                                    logging.info(f"{i} 文本类型：{i.get('文本类型')}")
                                    if i.get("文本类型") == '1':
                                        self.input_text_IPM('字段名称', text=random.randint(1, 100), choice=i.get("字段名"))
                                        sleep(1)
                                    else:
                                        self.input_text_IPM('字段名称', text=f'{i.get("字段名")}{protime}', choice=i.get("字段名"))
                                        sleep(1)

                                elif i.get("类型") == 'select':
                                    logging.info(f"{i} 字段名：{i.get('字段名')}")
                                    if i.get("字段名") == "任务类型":

                                        self.click_IPM('字段名称', choice=i.get("字段名"))
                                        self.click_IPM('下拉框')
                                        self.click_IPM('点击标题')
                                        sleep(1)
                                elif i.get("类型") == 'date':
                                    logging.info(f"{i.get('字段名')} 字段名：{i.get('字段名')}")
                                    self.input_text_IPM('字段名称', text=now_t, choice=i.get("字段名"))
                                    self.click_IPM('点击标题')
                                    sleep(1)
                                elif i.get("类型") == 'user':
                                    logging.info(f"{i.get('字段名')} 字段名：{i.get('字段名')}")
                                    sleep(1)
                                    self.click_IPM('字段名称', choice=i.get("字段名"))
                                    sleep(1)
                                    self.personnel_list(Job_number_or_name,Confirm_or_Cancel)


                            else:
                                if i.get("类型") == 'text':
                                    if i.get("文本类型") == '1':
                                        self.input_text_IPM('字段名称', text=1, choice=i.get("字段名"))
                                        sleep(1)
                                    else:
                                        self.input_text_IPM('字段名称', text=f'{i.get("字段名")}{protime}', choice=i.get("字段名"))
                                        sleep(1)
                                    sleep(1)
                                elif i.get("类型") == 'select':
                                    self.click_IPM('字段名称', choice=i.get("字段名"))
                                    self.click_IPM('下拉框')
                                    self.click_IPM('点击标题')
                                    sleep(1)

                                elif i.get("类型") == 'date':
                                    self.input_text_IPM('字段名称', text=now_t, choice=i.get("字段名"))
                                    self.click_IPM('点击标题')
                                    sleep(1)
                                elif i.get("类型") == 'user':
                                    sleep(2)
                                    self.click_IPM('字段名称', choice=i.get("字段名"))
                                    sleep(1)
                                    self.personnel_list(Job_number_or_name, Confirm_or_Cancel)

    def project_task_type(self,proname,task_name,protime,tasktype=None,Job_number_or_name=None,Confirm_or_Cancel=None,objectname=None):
        """
        计划_任务_选取任务类型
        :param proname: 项目名
        :param tasktype: 任务类型 ：TR任务/普通任务/普通里程碑任务/DCP任务/阶段任务
        :param protime: 当前日期
        :param task_name: 任务名称
        :param Job_number_or_name: 员工姓名或工号
        :param Confirm_or_Cancel: 人员保存确定还是取消
        """
        ele_not=self.element_exist_IPM('计划任务_点击展开')

        if ele_not == True:
            self.click_IPM('计划任务_点击展开')
        sleep(2)

        field_att = self.Api.Api_project_task(proname, task_name)
        for i in field_att:
            if i.get("字段名")=="任务类型":
                if tasktype == "普通任务" \
                        or tasktype == "TR任务" \
                        or tasktype == "DCP任务" \
                        or tasktype == "普通里程碑任务" \
                        or tasktype == "阶段任务":
                    self.click_IPM('字段名称', choice=i.get("字段名"))
                    self.click_IPM('下拉框_列表名', tasktype)
                else:
                    logging.info("当前任务类型不存在")
        self.Get_required_fields(proname,task_name,protime,Job_number_or_name,Confirm_or_Cancel,objectname)

    def project_Drop_down_box_multiple_selection(self,element_field,FieldName,*Drop_down_value):
        """
        下拉框_多选
        :param element_field: 字段元素
        :param FieldName: 字段名字
        :param Drop_down_value: 下拉框的值，支持传入多个

        """

        self.DropDownBox(element_field,FieldName,"字段名称",*Drop_down_value)

    def prpject_Team_Role(self,role,Number=None,role1=None):
        '''
        项目_团队_角色
        '''
        if Number == "0" or Number == None:
            self.click_IPM("团队_角色",role)
        if Number =="1":
            self.click_IPM("团队_角色_展开", role)
            self.click_IPM("团队_角色", role1)
        sleep(1)



    def project_team_AddRole(self):
        '''
        项目_团队_新增成员
        '''
        self.click_IPM("团队_角色_新增成员")


    def project_team(self,role="PMToffice",judge='删除',addrole=None,role_id=None):
        '''
        项目_团队
        :param judge: 传入删除，则将存在团队成员删除
        :param addrole: 添加成员
        :param role_id: 员工工号或姓名
        '''
        self.project_tab("团队")
        self.prpject_Team_Role(role)
        try:
            role_ele=self.find_elemens_ipm_yaml_get_attribute("团队_角色_表单成员")
            for i in role_ele:
                if i != None:
                    if judge == "删除":
                        self.click_IPM("团队_角色_成员删除",i)
                        self.click_IPM("团队_角色_成员删除_确定")
                        sleep(2)
                    else:
                        logging.info('当前不打算删除成员')
                if addrole == "添加成员" or addrole == "添加":
                    self.project_team_AddRole()
                    self.personnel_list(role_id)
                else:
                    logging.info('当前不打算添加成员')
        except:
            self.project_team_AddRole()
            self.personnel_list(role_id)
        sleep(1)










    def Create_project(self, Save_or_Cancel, templatename=None, nametext=None, Descriptiontext=None):
        """
        创建项目
        :param templatename: 选择对应的项目模板名字
        :param nametext: 项目名称
        :param Descriptiontext: 项目描述
        :param Save_or_Cancel: 保存还是取消
        """

        self.click_project()
        self.click_add()
        if templatename != None:
            try:
                self.Select_Template(templatename)
            except:
                logging.info(f"项目模板'{templatename}'不存在，请联系管理员添加模板或添加权限")
                raise
        if nametext != None:
            self.projecy_name(nametext)
        if Descriptiontext != None:
            self.projecy_Description(Descriptiontext)
        if Save_or_Cancel == '保存':
            self.projecy_preservation()
        else:
            self.projecy_cancel()

    def enter_the_project(self,projectname):
        '''点击卡片进入项目详情'''
        self.click_project_entrance(projectname)
        sleep(1)
        self.switch_window(-1)
        sleep(1)

    def Click_the_button_to_enter(self,projectname,edit_or_delete,delete_confirm_or_cancel= None):
        '''
        点击卡片展开编辑或删除按钮，并点击
        :param projectname: 传入项目名称
        :param edit_or_delete: 删除或编辑
        :param delete_confirm_or_cancel: 删除项目点击确认或取消
        '''

        self.click_project_entrance_ch(projectname)
        if edit_or_delete == "编辑":
            self.entrance_ch()
            sleep(1)
            self.switch_window(-1)
            sleep(3)
        elif edit_or_delete == "删除":
            self.delete_project()
            if delete_confirm_or_cancel == "确认":
                self.delete_project_determine()
            elif delete_confirm_or_cancel == "取消":
                self.delete_project_cancel()
            else:
                log.info(f"{delete_confirm_or_cancel}清输入正确的值，如：确认，取消")
        else:
            log.info(f"{edit_or_delete}清输入正确的值，如：编辑，删除")






    def project_entrance(self,projectname,protime):
        '''
        编辑项目-保存

        '''
        self.enter_the_project(projectname)
        sleep(5)
        self.click_edit()
        sleep(1)
        self.Get_required_fields(projectname,protime)
        self.perject_field_editing_save()






    def perject_field_editing(self,proname,protime):
        '''
        项目管理编辑页面字段维护
        '''

        self.Get_required_fields(proname,protime)



#断言
class Assert_result(AssertMode):
    def __init__(self,driver,element_yaml='ProjectManagement', expect='ProjectManagement.yaml'):
        super().__init__(driver, element_yaml,expect=expect)





