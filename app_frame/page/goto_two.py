# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 15:44 
# @File : goto_two.py
from pytest_logs import MyLogs

from app_frame.page.basepage import BasePage
from app_frame.page.goto_three import GotoThreePage
from pytest_logs import MyLogs
logs=MyLogs()
class GotoTwoPage(BasePage):
    # 进入添加成员界面
    def goto_twopage(self,name):
        logs.info("")
        self.swipe_click(name)

        self.parse_action("../datas/goto_two.yaml")
        return GotoThreePage(self.driver)