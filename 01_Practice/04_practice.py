
# while循环打印 9*9 乘法表1
i = 0
j = 0
while i <= 9:
    i += 1
    j = i
    while j <= 9:
        print(f"{i}*{j}={i*j}", end="\t")
        j += 1
    print("\n")


# 循环打印 9*9 乘法表1
i = 0
while i < 9:
    i += 1
    j = 0
    while j < i:
        j += 1
        print(f"{j}*{i}={j*i}", end="\t")
    print("\n")