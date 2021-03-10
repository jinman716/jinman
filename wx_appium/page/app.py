# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 9:47 
# @File : app.py
from appium import webdriver

from wx_appium.page.goto_one import  GotoOnePage


class APP:
    def __init__(self):
        self.driver = None
        self.start()

    def start(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "wework"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps['automationName'] = 'uiautomator2'
        # 不清空缓存启动app
        caps["noReset"] = "true"
        # 设置等待页面空闲状态的时间为0s
        caps['settings[waitForIdleTimeout]'] = 0
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 显式等待10s
        self.driver.implicitly_wait(10)

    def goto_main_page(self):
        # 返回主页
        return GotoOnePage(self.driver)