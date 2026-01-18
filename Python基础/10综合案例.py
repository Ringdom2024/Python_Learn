# LangYA.wang
# @Time : 2025/12/28 16:35
# @Author : 王一凡
# @Version : 
# @IDE : PyCharm
# @Project : PythonProject

# 原始目录:D:\all_code\PythonProject\Python基础
import os

def copy_task(source_dir,destination_dir):
    """
    拷贝source_dir中的所有的py文件,到指定的destination_dir文件夹中
    :param source_dir: 原始目录
    :param destination_dir: 目标目录
    :return:
    """
    for f in os.listdir(source_dir):
        f_path = os.path.join(source_dir,f)
        if os.path.isfile(f_path) and f.endswith('.py'):
            # 拷贝单个文件
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            sink_path = os.path.join(destination_dir,f)
            # 拷贝单个py文件
            copy_py_file(f_path,sink_path)
        elif os.path.isdir(f_path):
            destination_path = os.path.join(destination_dir,f)
            copy_task(f_path,destination_path)


def copy_py_file(source_file,destination_file):
    """
    拷贝单个py文件到指定位置(读取原始文件中的数据,并写入同一个文件夹中)
    :param source_file:
    :param destination_file:
    :return:
    """
    source_file = open(source_file,'r',encoding='utf-8')
    destination_file = open(destination_file,'w',encoding='utf-8')

    # content = source_file.read() 有风险,文件比较大,不能用此方法
    # destination_file.write(content)

    while True:
        content = source_file.read(1024*10)
        if content == "" or content is None:
            break
        destination_file.write(content)

    source_file.close()
    destination_file.close()


copy_task(r'D:\all_code\roco_Project\携程AI智能助手项目\ctrip_assistant',r'D:\all_iminf\temp')
print('代码已运行完成')