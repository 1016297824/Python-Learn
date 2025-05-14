# 函数中的类型注解

# 对形参进行类型注解
def add(a: int, b: int):
    return a + b


add(2, 3)


# 对返回值进行类型注解
def func(data: list) -> list:
    pass


print(func(123))
