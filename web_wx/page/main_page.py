# -*- coding: utf-8 -*- 
# @Time : 2021/3/1 10:15 
# @File : main_page.py
from selenium.webdriver.common.by import By
from selenium import webdriver
from web_wx.page.add_member import Add_MemberPage
from web_wx.page.basepage import BasePage


class MainPage(BasePage):
    #测试页面地址
    base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'
    #定义添加成员的方法
    def goto_member(self):
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        #self.find(By.CSS_SELECTOR, ".ww_operationBar:nth-child(1) > .js_add_member").click()
        return Add_MemberPage(self.driver)


    def goto_index(self):
        self.find(By.ID,"menu_contacts").click()
        return True