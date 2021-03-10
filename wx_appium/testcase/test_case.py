# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 16:37 
# @File : test_case.py
import yaml

from wx_appium.page.app import APP


class TestAddmembers:
    def setup(self):
        self.app = APP()

    def test_addmembers(self):
        # 获取addmember返回的toast并进行断言
        toast = self.app.goto_main_page().goto_onepage().goto_twopage().goto_threepage().addmember()
        print(toast)
        assert "添加成功" == toast


