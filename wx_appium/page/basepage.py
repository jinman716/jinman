# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 10:18 
# @File : basepage.py
import random
from typing import List, Dict
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver



class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, by, locator):
        """
        查找元素
        :param by: 定位方法
        :param locator: 定位值
        :return: element
        """
        return self.driver.find_element(by, locator)

    def find_click(self, by, locator):
        """
        查找元素并点击
        :param by: 定位方法
        :param locator: 定位值
        """
        self.find(by, locator).click()

    def find_sendkeys(self, by, locator, key):
        """
        查找元素并传值
        :param by: 定位方法
        :param locator: 定位值
        """
        self.find(by, locator).send_keys(key)

    def get_toast(self, by, locator):
        """
        获取toast
        :param by: 定位方法
        :param locator: 定位值
        :return: toast的文本信息
        """
        return self.find(by, locator).text

    def swipe_click(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));').click()

    # 封装生成随机字母+数字函数
    def getRandomSet(bits):
        num_set = [chr(i) for i in range(48, 58)]
        char_set = [chr(i) for i in range(97, 123)]
        total_set = num_set + char_set
        value_set = "".join(random.sample(total_set, bits))
        return value_set

    # 封装生成随机手机号函数
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

    def parse_action(self, path):
        """
        步骤数据加载
        :param path:yaml文件路径
        """
        with open(path, encoding="utf-8") as f:
            steps = yaml.safe_load(f)
        for step in steps:
            if step["action"] == "find_click":
                self.find_click(step["by"], step["locator"])
            elif step["action"] == "find_sendkeys":
                if step["value"] == "name":
                    self.find_sendkeys(step["by"], step["locator"],BasePage.getRandomSet(5))
                elif step["value"] == "phone":
                    self.find_sendkeys(step["by"], step["locator"],BasePage.phone)
            elif step["action"] == "get_toast":
                # 返回获取的toast文本信息
                return self.get_toast(step["by"], step["locator"])

