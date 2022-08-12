# -*- coding: utf-8 -*-
# @Time    : 2022-08-02 17:15
# @Author  : wuqi
# @Email   : qi.wu@transsion.com
# @File    : BasicInfo_BoardParametersSetting.py
# @Software: PyCharm

import allure
from ..test_case.conftest import *
from libs.common.read_element import Element
from public.base.basics import Base

object_name = os.path.basename(__file__).split('.')[0]
basic = Element(pro_name, object_name)


class BoardUserSetting(Base):
    """看板参数配置"""

    @allure.step("查询条件工号输入")
    def input_job_number(self, content):
        self.input_text(basic['工号输入框'], content)

    @allure.step("查询条件姓名输入")
    def input_name(self, content):
        self.input_text(basic['姓名输入框'], content)

    @allure.step("选择岗位")
    def choice_post(self, content):
        self.is_click(basic["岗位下拉选择框"])
        self.is_click(basic["岗位下拉选项"], content)

    @allure.step("点击新增按钮")
    def click_insert(self):
        self.is_click(basic["新增按钮"])

    @allure.step("点击查询按钮")
    def click_search(self):
        self.is_click(basic["查询按钮"])

    @allure.step("点击重置按钮")
    def click_reset(self):
        self.is_click(basic["重置按钮"])

    @allure.step("点击导出按钮")
    def click_export(self, content):
        # self.is_click(basic["导出按钮"])
        self.check_download(basic["导出按钮"], content)

    @allure.step("点击编辑按钮")
    def click_edit(self):
        self.is_click(basic["编辑按钮"])

    @allure.step("点击删除按钮")
    def click_del(self, row):
        self.is_click(basic["删除按钮"], row)

    @allure.step("填写表单")
    def fill_form(self, kwargs):
        """
        :param kwargs:dict (key为表单行数， value为录入内容)
        """
        for k, v in kwargs.items():
            if int(k) < 4:
                self.input_text(basic["新增/编辑弹窗第n行表单"], v, k)
            elif 3 < int(k) < 6:
                self.is_click(basic["新增/编辑弹窗第n行表单"], k)
                self.is_click(basic["新增/编辑弹窗下拉选项"], v)
            elif int(k) == 6:
                self.upload_file(basic['新增/编辑弹窗第n行表单'], v, k)
            else:
                assert False, "填入内容行数错误"

    @allure.step("确认保存")
    def click_form_accept(self):
        self.is_click(basic["新增/编辑弹窗确认"])

    @allure.step("取消保存")
    def click_form_cancel(self):
        self.is_click(basic["新增/编辑弹窗取消"])

    @allure.step("删除弹窗确认")
    def click_del_accept(self):
        self.is_click(basic["删除弹窗确认"])

    @allure.step("删除弹窗确认")
    def click_del_cancel(self):
        self.is_click(basic["删除弹窗取消"])
