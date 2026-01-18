# LangYA.wang
# @Time : 2026/1/11 20:14
# @Author : 王一凡
# @Version : 
# @IDE : PyCharm
# @Project : PythonProject
import random #标准库
import radar


class car:
    def __init__(self,name,color,speed):
        self.name = name
        self.color = color
        self.speed = speed

    def run(self):
        # 在类里面访问对象的属性:属性名
        print(f'{self.name} 跑起来了!')
    # 魔法函数
    # print(对象)时输入的内容
    def __str__(self):
        return f'汽车的品牌是:{self.name},汽车的颜色是:{self.color},汽车的最高时速是:{self.speed}'
    #
    def __del__(self):
        print(f'有人删除我的汽车了,删除的型号是{self.name}+{self.color}')
mycar1 = car('劳斯莱斯','黑色','300')
mycar2 = car('梅德赛德奔驰','白色','288')
mycar3 = car('法拉利','蓝色','260')

print(id(mycar1), id(mycar2))

# 访问类的方法
mycar1.run()

# 访问类的属性
print(mycar1.name)

# 修改类的属性
mycar1.name = '太阳神阿波罗'
print(mycar1.name)
mycar1.run()

print(mycar3)
del mycar3