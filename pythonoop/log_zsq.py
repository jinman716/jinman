# -*- coding: utf-8 -*-
import logging

logging.basicConfig(level=logging.INFO)
logs = logging.getLogger('log')

def log_info(func):
    def wapper(*args,**kwargs):
        logs.info(f'装饰器测试：{log_info.__name__},传入函数:{func.__name__}')
        return  func(*args,**kwargs)
    return wapper