# -*- coding: utf-8 -*- 
# @Time : 2021/3/1 13:23 
# @File : test_contact.py
import pytest
from web_wx.page.basepage import BasePage
from web_wx.page.main_page import MainPage
import sys
from pytest_logs import MyLogs
logger = MyLogs()

class TestContact:
    def setup(self):
        self.mainpage = MainPage()


    def test_addmember(self):
        logger.info("开始生成日志.....")
        logger.logsath()
        logger.info("开始新增成员")

        username = BasePage.getRandomSet(6)

        account = BasePage.getRandomSet(6)

        phonenum =BasePage.phone

        page = self.mainpage.goto_member()

        page.add_members(username, account, phonenum)

        names = page.get_members()

        print(names)

        assert username  in names

    def teardown(self):
        '''
        回到首页
        :return:
        '''
        self.mainpage.goto_index()


