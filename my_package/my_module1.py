# 自定义模块

# 控制 “*” 可以调用的变量（不影响其它调用方式）
# __all__ = ["sum"]

def sum(a, b):
    print(a + b)


def subtract(a, b):
    print(a - b)


# print(__name__) #调用时为 “my_module”
# 自定义模块测试
if __name__ == '__main__':
    sum(1, 2)
