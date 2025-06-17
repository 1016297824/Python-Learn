# 函数传参
import time

# 不可变类型传参
"""
    不可变类型：
    字符串(str)
    整数(int)
    浮点数(float)
    元组(tuple)
    字节序列(bytes)
"""


# 注意：对于不可变参数，传递的是副本，不会改变原变量的值
def change(a: int):
    a += 1
    return a


a = 10
print(change(a))
print(a)

# 可变类型传参
"""
    可变类型：
    列表(list)
    字典(dict)
    集合(set)
    字节数组(bytearray)
"""


# 注：对于可变参数，传递的是地址，可以改变原变量的值
def change_l(l: list):
    l.append("14")
    return l


my_list = ["11", "12", "13"]
print(change_l(my_list))
print(my_list)
