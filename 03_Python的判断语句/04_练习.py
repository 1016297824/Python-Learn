import random

# 猜随机数字
print("这是一个1~10的整数，请猜猜它是多少")
num = random.randint(1, 10)
temp = int(input("第一次猜测："))
if temp != num:
    if temp > num:
        print("猜大了")
    else:
        print("猜小了")
    temp = int(input("第二次猜测："))
    if temp != num:
        if temp > num:
            print("猜大了")
        else:
            print("猜小了")
        temp = int(input("第三次猜测："))
        if temp != num:
            print("机会用完了，这个数是：", num)
        else:
            print("第三次猜对了，这个数就是：", num)
    else:
        print("第二次猜对了，这个数就是：", num)
else:
    print("第一次猜对了，这个数就是：", num)