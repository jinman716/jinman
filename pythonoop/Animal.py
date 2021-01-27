# -*- coding: utf-8 -*-
'''比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
重写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发 = 短毛，
添加一个新的方法， 会捉老鼠，
重写父类的【会叫】的方法，改成【喵喵叫】'''
from log_zsq import log_info


class Animal:
    def __init__(self,name,age,color,sex):
        self.name=name
        self.age = age
        self.color=color
        self.sex=sex
    @log_info
    def Scream(self):
        print(f'{self.name}现在{self.age},全身{self.color}性别{self.sex},喜欢尖叫')

    @log_info
    def Run(self):
        print(f'{self.name}现在{self.age},全身{self.color}性别{self.sex}，喜欢奔跑')

if __name__ == '__main__':
    animal_pig = Animal("亚索","20岁","红色","男")
    animal_dog = Animal("内瑟斯","39岁","棕色","男")
    animal_dog.Scream()
    animal_pig.Scream()
    animal_pig.Run()
    animal_dog.Run()
