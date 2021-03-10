# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 15:44 
# @File : goto_two.py
from pytest_logs import MyLogs

from wx_appium.page.basepage import BasePage
from wx_appium.page.goto_three import GotoThreePage


class GotoTwoPage(BasePage):
    # 进入添加成员界面
    def goto_twopage(self):
        self.swipe_click("添加成员")
        return GotoThreePage(self.driver)