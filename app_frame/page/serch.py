# -*- coding: utf-8 -*- 
# @Time : 2021/3/15 14:03 
# @File : serch.py
from app_frame.page.basepage import BasePage
import  time
class Back(BasePage):
    def back(self,name):
        self._params['name'] = name
        self.parse_action("../datas/serch.yaml")
        time.sleep(3)
        return self.parse_action("../datas/serch.yaml")

