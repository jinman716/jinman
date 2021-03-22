# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 15:49 
# @File : goto_three.py
from pytest_logs import MyLogs
from app_frame.page.serch import Back
from app_frame.page.basepage import BasePage
logs=MyLogs
class GotoThreePage(BasePage):
    def goto_threepage(self):
        self.parse_action("../datas/go_to_three.yaml")
        return Back(self.driver)