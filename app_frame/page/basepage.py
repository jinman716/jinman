# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 10:18 
# @File : basepage.py
import random
from typing import List, Dict

import allure
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pytest_logs import MyLogs

from app_frame.testcase.run import SCREEN_SHOT
logs = MyLogs()
class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
    _params = {}
    _error_count = 0
    _error_max = 10
    _black_list = [(By.XPATH, "//*[@text='关闭']"), (By.XPATH, "//*[@resource-id='com.tencent.wework:id/bpc']")]
    def find(self, by, locator=None):
        try:
            element = self.driver.find_element(*by) if isinstance(by, tuple) else self.driver.find_element(by, locator)
            # 找到元素后重置错误次数
            self._error_count = 0
            self.driver.implicitly_wait(10)
            return element
        except Exception as e:
            logs.warning(f"元素：by={by} locator={locator} 未找到，开始黑名单处理...")
            self._error_count += 1
            self.driver.implicitly_wait(10)
            # 保存出现错误页面的截图
            self.driver.get_screenshot_as_file(f"{SCREEN_SHOT}/tmp.png")
            self.driver.get_screenshot_as_file("tmp.png")
            allure.attach.file("tmp.png", attachment_type=allure.attachment_type.PNG)
            # 设置最大查找次数
            if self._error_count > self._error_max:
                logs.error(f"需要的元素：by={by} locator={locator}，未找到，请处理...")
                raise e
            for black in self._black_list:
                # 查找当前弹窗是否存在于黑名单中，存在则点击关闭，返回函数本身
                elements = self.driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    logs.info(f"黑名单元素：{elements[0]}已处理!")
                    return self.find(by, locator)
            raise e

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
            elif step['action'] == 'find_sendkeys':
                value: str = step['value']
                for param in self._params:
                    value = value.replace("${" + param + "}", self._params[param])
                self.find_sendkeys(step['by'], step['locator'], value)
            elif step["action"] == "get_toast":
                # 返回获取的toast文本信息
                return self.get_toast(step["by"], step["locator"])




