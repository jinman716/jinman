# -*- coding: utf-8 -*-
import os
import pytest
import yaml
import sys
sys.path.append(r'D:\pychram\pythonProject\calctest')
import allure
from calc_class.calcclass import Calculator
with open(r"D:\pychram\pythonProject\calctest\calc_datas\calc.yaml") as f:
    data = yaml.safe_load(f)
    # 获取add数据
    add_datas = data['add']['datas']
    # 获取div数据
    div_datas = data['div']['datas']
    # 获取sub数据
    sub_datas = data['sub']['datas']
    # 获取mul数据
    mul_datas = data['mul']['datas']


@pytest.fixture(scope="module")
def get_calc():
    # 实例化计算器类
    print("开始计算")
    calc = Calculator()
    yield calc
    print("结束计算")

@pytest.fixture(params=add_datas, ids=data['add']['myid'])  # 获取加法数据，并返回
def get_add_datas(request):
    data = request.param
    return data


@pytest.fixture(params=sub_datas, ids=data['sub']['myid'])  # 获取减法法数据，并返回
def get_sub_datas(request):
    data = request.param
    return data


@pytest.fixture(params=mul_datas, ids=data['mul']['myid'])  # 获取乘法法法数据，并返回
def get_mul_datas(request):
    data = request.param
    return data


@pytest.fixture(params=div_datas, ids=data['div']['myid'])  # 获取除法法数据，并返回
def get_div_datas(request):
    data = request.param
    return data
