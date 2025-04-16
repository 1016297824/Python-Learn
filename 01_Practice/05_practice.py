
# for循环打印 9*9 乘法表
for x in range(1,10):
    for y in range(1,10):
        if y <= x:
            print(f"{y}*{x}={x*y}", end="\t")
    else:
        print()
print()

for x in range(1,10):
    for y in range(1,x+1):
            print(f"{y}*{x}={x*y}", end="\t")
    else:
        print()