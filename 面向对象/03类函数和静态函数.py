# LangYA.wang
# @Time : 2026/1/12 14:37
# @Author : 王一凡
# @Version : 
# @IDE : PyCharm
# @Project : PythonProject


class Person:
    # 类函数:1.装饰器@classmethod,2.在类层面的
    @classmethod
    def run(cls):
        print('所有人都可以直立行走')

    # 静态函数:.1.装饰器@staticmethod,2.只和关系有关(除此之外没有任何关系,不常用)
    @staticmethod
    def work():
        print('大家在工作')

    def sleep(self): # 实例函数,对象函数,成员函数
        print('我开始睡觉')

