# -*- coding: utf-8 -*- 
# @Time : 2021/3/1 10:58 
# @File : basepage.py
import logging
import math
from random import random
import random
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver == None:
            # 复用浏览器，需要设置 option.debugger_address
            option = Options()
            option.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=option)
            # 创建完driver ， 立刻设置隐式等待
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

        if self.base_url != "":
            self.driver.get(self.base_url)

    #封装常用定位方法
    # 查找单个元素
    def find(self, locator, value):
        return self.driver.find_element(locator, value)

    # 查找多个元素
    def finds(self, locator, value):
        return self.driver.find_elements(locator, value)

    # 输入框输入内容
    def sen_keys(self, by, locator, content):
        return self.find(by, locator).send_keys(content)

    #封装隐式等待
    def wait_for_click(self, timeout, locator):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    # 退出浏览器
    def quit(self):
        return self.driver.quit()


    #封装生成随机字母+数字函数
    def getRandomSet(bits):
        num_set = [chr(i) for i in range(48, 58)]
        char_set = [chr(i) for i in range(97, 123)]
        total_set = num_set + char_set
        value_set = "".join(random.sample(total_set, bits))
        return value_set

    #封装生成随机手机号函数
    def create_phone():
        # 第二位数字
        second = [3, 4, 5, 7, 8][random.randint(0, 4)]

        # 第三位数字
        third = {
            3: random.randint(0, 9),
            4: [5, 7, 9][random.randint(0, 2)],
            5: [i for i in range(10) if i != 4][random.randint(0, 8)],
            7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
            8: random.randint(0, 9),
        }[second]

        # 最后八位数字
        suffix = random.randint(9999999, 100000000)

        # 拼接手机号
        return "1{}{}{}".format(second, third, suffix)

    phone = create_phone()
