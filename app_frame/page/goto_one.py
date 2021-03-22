# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 13:02 
# @File : goto_one.py
from app_frame.page.basepage import BasePage
from app_frame.page.goto_two import GotoTwoPage
import time

class GotoOnePage(BasePage):
    def goto_onepage(self):
        # time.sleep(10)
        self.parse_action("../datas/goto_one.yaml")
        return GotoTwoPage(self.driver)