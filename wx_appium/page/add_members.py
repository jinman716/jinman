# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 13:02 
# @File : add_members.py
from wx_appium.page.basepage import BasePage


class AddMembersPage(BasePage):
    def addmember(self):
        self.parse_action("../datas/add_members.yaml")
        return self.parse_action('../datas/toast.yaml')


