# -*- coding: utf-8 -*- 
# @Time : 2021/2/2 17:52 
# @File : Test_runner.py
# coding=GBK
import os
import sys
import subprocess
import time
sys.path.append(r'D:\pychram\pythonProject\calctest')
if __name__ == "__main__":
    print('开始生成测试报告'.center(20, '*'))
    p = subprocess.Popen("pytest ./calc_case/calccase.py --alluredir=./report")
    q = subprocess.Popen("allure serve ./report")
    time.sleep(5)
    print('正在打开测试报告'.center(20, '*'))
    p.kill()
    q.kill()

