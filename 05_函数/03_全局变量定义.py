# 函数内部使用全局变量
num = 200


def test1():
    print(num)
    return None


def test2():
    global num
    num = 300
    return num


print(test1())
print(num)
print(test2())
print(num)
