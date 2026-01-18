# LangYA.wang
# @Time : 2026/1/12 14:25
# @Author : 王一凡
# @Version : 
# @IDE : PyCharm
# @Project : PythonProject


class Person:
    shengwu_category = '人类' # 类属性

    def __init__(self,name): #实例属性(对象属性)
        self.name = name

p1 = Person('张三')
p2 = Person('李四')
# print(p1.name)
# print(p2.name)
# print(p1.shengwu_category)

print(Person.shengwu_category)
Person.shengwu_category  = '人科'
print(p1.shengwu_category)