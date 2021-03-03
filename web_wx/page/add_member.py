# -*- coding: utf-8 -*- 
# @Time : 2021/3/1 11:31 
# @File : add_member.py
import logging
from selenium.webdriver.common.by import By
from web_wx.page.basepage import BasePage

from pytest_logs import  MyLogs
logger = MyLogs()
class Add_MemberPage(BasePage):
    def add_members(self, username, acctId, phoneNum):

        # 成员姓名
        self.find(By.ID, "username").send_keys(username)

        # 成员账号
        self.find(By.ID, "memberAdd_acctid").send_keys(acctId)

        # 手机号
        self.find(By.ID, "memberAdd_phone").send_keys(phoneNum)

        # 保存
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        logger.info("新增成功")

        return True

    def get_members(self):
        # 定义一个集合
        names = []

        # find_elements 查找第一页页面上的相同属性的所有元素，[element1,element2......]
        members_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        for i in members_list:
            names.append(i.get_attribute("title"))
        logger.info(f"此时第一页集合元素为{names}")

        # 若有多页，先判断翻页元素是否存在
        while True:
            # 点击下一页按钮
            self.find(By.CSS_SELECTOR, ".js_next_page").click()

            # 循环获取当前页面属性为title的值加入集合names中
            members_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
            for i in members_list:
                names.append(i.get_attribute("title"))

            # 定位下一页按钮元素,判断下一页按钮是否可点击
            next_page_button = self.find(By.CSS_SELECTOR, ".js_next_page").get_attribute("disabled")
            logger.warning(f"next_page_button={next_page_button}")

            # 当下一页按钮不可点击，即disabled=true时，跳出循环
            if next_page_button == "true":
                break

        logger.info(f"此时集合元素为{names}")
        return names
