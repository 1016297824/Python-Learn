# 函数的基础使用（定义，参数，返回值）
# 注意
"""
    函数参数的可变类型
    列表（list）
    字典（dict）
    集合（set）

    函数参数的不可参数
    整数（int）
    浮点数（float）
    字符串（str）
    元组（tuple）
"""


def add(x, y):
    return x + y


def add1(x, y, z):
    z = x + y
    return z


def add2(x, y, *z):
    z = x + y
    return z


print(add(2, 2))
z = 0
print(add1(1, 2, z), " ", z)
z = 0
print(add2(1, 2, z), " ", z)

def add3(x,y):
    result = x + y
    return result

result = add3(5, 2)
print(result)