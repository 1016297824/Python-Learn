# 闭包
from functools import total_ordering


# 简单闭包
# 作用：将logo作为全局变量并防止logo被外部操作修改
def outer(logo):
    def inner(msg):
        print(f"<{logo}>{msg}<{logo}>")

    return inner


test = outer("霸气可爱")
test("小蜜蜂")

test1 = outer("霸气可爱")
test("小鲤鱼")


# 使用nonlocal关键字修改外部函数中全局变量的值

def init(num: int):
    def total(add: int):
        nonlocal num
        num = num + add
        print(num)

    return total


total = init(10)
total(10)
total(10)
total(10)
total(10)
total(10)


# 简单实现ATM取钱案例
def bank(money: int = 50000):
    def atm(change, get: bool = True):
        nonlocal money
        if get:
            money = money - change
            print(f"取款{change}，", end="")
        else:
            money = money + change
            print(f"存款{change}，", end="")
        print("当前剩余存款：" + str(money))

    return atm


money = bank()
money(10000)
money(20000, False)
