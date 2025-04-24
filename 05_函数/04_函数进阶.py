# 函数返回多返回值
def duoduo():
    return "小可爱", 2023


x, y = duoduo()
print(x, " ", y)
print()


# 位置参数
def weizhi(x, y):
    print(x + y)


weizhi(5254, 123)
print()


# 关键字参数
def guanjianzi(name, age, high):
    print(name, " ", age, " ", high)


guanjianzi(name="小可爱", high=165, age=18)
guanjianzi("小可爱", high=166, age=19)  # 位置参数可以和关键字参数混用
print()


# 缺省参数
def quesheng(name, age, high=165):  # 默认参数后不能加非默认参数
    print(name, " ", age, " ", high)


quesheng("小可爱", 18)
print()


# 不定长参数
# 位置传递的不定长参数
def budingWZ(*ages):
    print(type(ages))
    for item in ages:
        print(item, end=" ")


budingWZ(1, 2, 3)
print()
print()


# 关键字传递的不定长参数
def budingGJZ(**ages):
    print(type(ages))
    for key in ages:
        print(f"{type(key)}: {key}: {ages[key]}", end="\n")


budingGJZ(name="小可爱", age=18, high=165)
print()


# 使用匿名函数
def addFun(add1):
    result = add1(1, 2)
    print(result)


addFun(lambda x, y: x + y)
