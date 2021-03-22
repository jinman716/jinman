# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 16:37 
# @File : test_case.py
import allure
from pytest_logs import     MyLogs
from app_frame.page.app import APP
logs=MyLogs()
@allure.feature('删除成员功能')
class TestDelmembers:
    def setup(self):
        self.app = APP()

    logs.info("测试删除成员")
    @allure.story("测试删除成员")
    def test_delmembers(self):
        name="泰达米尔"
        toast = self.app.goto_main_page().goto_onepage().goto_twopage(name).goto_threepage().back(name)
        print(toast)
        logs.info("结果断言")
        assert "无搜索结果" == toast


