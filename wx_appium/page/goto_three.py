# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 15:49 
# @File : goto_three.py
from pytest_logs import MyLogs

from wx_appium.page.add_members import AddMembersPage
from wx_appium.page.basepage import BasePage

class GotoThreePage(BasePage):
    def goto_threepage(self):
        self.parse_action("../datas/goto_three.yaml")
        return AddMembersPage(self.driver)