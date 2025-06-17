# 装饰器
import time
import random


# 装饰器的一般写法（闭包）
def outer(func):
    def inner():
        print("准备睡觉了")
        func()
        print("起床了")

    return inner


def sleep():
    time.sleep(random.randint(1, 3))
    print("睡眠中。。。")
    time.sleep(random.randint(2, 6))


lazyBoy = outer(sleep)
lazyBoy()
print()


# 装饰器的快捷写法（语法糖）
def logWrite(func):
    def inner():
        print("准备取钱")
        func()
        print("取完了")

    return inner


@logWrite
def getMoney():
    time.sleep(random.randint(1, 3))
    print("取钱中")
    time.sleep(random.randint(2, 6))


getMoney()
