# LangYA.wang
# @Time : 2025/12/23 21:50
# @Author : 王一凡
# @Version : 
# @IDE : PyCharm
# @Project : PythonProject

# 打开一个文件,得到一个文件流
# 切记:要关闭
fs = open('test1.txt')

# 读数据
# content = fs.read(17)
# print(content)

# 读取所有的行,把所有的行,返回到一个列表中
# lst  = fs.readlines()
# print(lst)

line = fs.readline()
while line!='' and line is not None:
    print(line,end='')
    line = fs.readline()
fs.close()
