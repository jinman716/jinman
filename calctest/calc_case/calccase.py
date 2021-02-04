# -*- coding: utf-8 -*- 
# @Time : 2021/2/1 13:26 
# @File : calccase.py
import sys
sys.path.append(r'D:\pychram\pythonProject\calctest')
import allure
import pytest
@allure.feature("计算器测试")
class TestCalcutor:
    @allure.story("测试加法")
    @pytest.mark.run(order=1)#order控制方法执行顺序
    def test_add(self,get_calc, get_add_datas):#定义测试加法案例方法，实例化加法
        # 步骤说明
        with allure.step("加法计算"):
            result = get_calc.add(get_add_datas[0],get_add_datas[1])#获取测试数据
        if isinstance(result, float):#判断数据类型，如果是浮点数，强制保留小数点后两位
            result = round(result, 2)
        assert result == get_add_datas[2]#断言:判断是否相等，相等则pass，不相等则fail


    @allure.story("测试减法")
    @pytest.mark.run(order=2)#order控制方法执行顺序
    def test_sub(self, get_calc, get_sub_datas):
        # 步骤说明
        with allure.step("减法计算"):
            result = get_calc.sub(get_sub_datas[0], get_sub_datas[1])#获取测试数据
        if isinstance(result, float):#判断数据类型，如果是浮点数，强制保留小数点后两位
            result = round(result, 2)
        assert result == get_sub_datas[2]#断言:判断是否相等，相等则pass，不相等则fail

    @allure.story("测试乘法")
    @pytest.mark.run(order=3)#order控制方法执行顺序
    def test_mul(self, get_calc, get_mul_datas):
        # 步骤说明
        with allure.step("乘法计算"):
            result = get_calc.mul(get_mul_datas[0], get_mul_datas[1])#获取测试数据
        if isinstance(result, float):#判断数据类型，如果是浮点数，强制保留小数点后两位
            result = round(result, 2)
        assert result == get_mul_datas[2]#断言:判断是否相等，相等则pass，不相等则fail

    @allure.story("测试除法")
    @pytest.mark.run(order=5)  # order控制方法执行顺序
    def test_div(self, get_calc, get_div_datas):
        # 步骤说明
        with allure.step("除法计算"):
            result = get_calc.div(get_div_datas[0], get_div_datas[1])#获取测试数据
        if isinstance(result, float):#判断数据类型，如果是浮点数，强制保留小数点后两位
            result = round(result, 2)
        assert result == get_div_datas[2]#断言:判断是否相等，相等则pass，不相等则fail

