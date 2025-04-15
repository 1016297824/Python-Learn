import random

# 猜数游戏，使用while循环猜 1~100 之间的数
num = random.randint(1, 100);
i = 0;
print("这是一个 1~100 的整数，猜猜这个数是多少：")
while 1:
    i += 1;
    temp = int(input(f"第{i}次猜测："))
    if temp == num:
        print(f"恭喜你第{i}次猜对了，这个数就是{num}")
        break;
    elif temp < num:
        print("猜小了")
    else:
        print("猜大了")