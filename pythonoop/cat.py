# -*- coding: utf-8 -*-
'''比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
重写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发 = 短毛，
添加一个新的方法， 会捉老鼠，
重写父类的【会叫】的方法，改成【喵喵叫】'''
import sys
from Animal import Animal
from log_zsq import log_info


class Cat(Animal):
    def __init__(self, hair, name, age, color, sex):
        super().__init__(name, age, color, sex)
        self.hair=hair

    @log_info
    def CatchMouse(self):
        print(f'{self.name}现在{self.age},全身{self.color},毛发是{self.hair}，性别{self.sex},喜欢捉老鼠')

    @log_info
    def Scream(self):
        print(f'{self.name}现在{self.age},全身{self.color},毛发是{self.hair}，性别{self.sex},喜欢喵喵叫')
if __name__ == '__main__':
     cat_1=Cat("短发","亚索","20岁","红色","男")
     cat_1.CatchMouse()
     cat_2=Cat("短发","亚索","20岁","红色","男")
     cat_2.Scream()