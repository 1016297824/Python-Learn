# 列表
# 定义
["霸气", "可爱", "小蜜蜂"]
my_list = ["霸气", "可爱", "小蜜蜂"]
my_list = []
my_list = list()

# 二维列表
my_list = [["霸气", "可爱", "小蜜蜂"], ["1999.01.16", 27], [165, 127.5, "C"]]
print(my_list)
print(type(my_list))

for item in my_list:
    for item1 in item:
        print(item1, end=" ")
    print()

# 逆向输出列表内容
print()
print(my_list[-1][0], " ", type(my_list[-1][0]))
print(my_list[-1][1], " ", type(my_list[-1][1]))
print(my_list[-1][2], " ", type(my_list[-1][2]))
print()

# 列表的常用操作
# 查询元素位置
# 错误示范
# index1 = my_list.index("C")
# index2 = my_list.index(27)
# 正确查询
index1 = my_list[2].index("C")
index2 = my_list[1].index(27)
print(index1)
print(index2)
print()

# 修改列表元素
print(my_list[1][1], " ", type(my_list[1][1]))
my_list[1][1] = "26"
print(my_list[1][1], " ", type(my_list[1][1]))
print()

for item in my_list:
    for item1 in item:
        print(item1, end=" ")
    print()
print()

# 插入元素
my_list.insert(1, ["霸气", "可爱", "小州官"])
# 错误示范
# my_list.insert(1, 666666666666666666666666)
my_list.insert(1, [666666])
for item in my_list:
    for item1 in item:
        print(item1, end=" ")
    print()
print()

my_list[1].insert(0, 88888888)
for item in my_list:
    for item1 in item:
        print(item1, end=" ")
    print()
print()

# 在尾部追加元素
# 错误示范
# my_list.append(2222222)
my_list.append([2222222])
for item in my_list:
    for item1 in item:
        print(item1, end=" ")
    print()
print()

my_list[5].append(33333333)
for item in my_list:
    for item1 in item:
        print(item1, end=" ")
    print()
print()

# 删除元素
# 使用del关键字删除
del my_list[5]
for item in my_list:
    for item1 in item:
        print(item1, end=" ")
    print()
print()

# 使用pop方法删除
result = my_list.pop(1)
print(result)
print()
for item in my_list:
    for item1 in item:
        print(item1, end=" ")
    print()
print()

# 使用remove方法删除
my_list.remove(["霸气", "可爱", "小州官"])
for item in my_list:
    for item1 in item:
        print(item1, end=" ")
    print()
print()

# 清空列表
my_list.clear()
print(my_list)

my_list = [["霸气", "可爱", "小蜜蜂"], ["1999.01.16", 27], [165, 127.5, "C"]]
my_list = None
print(my_list)
print()

# 查询列表中某一元素的数量
my_list = [["霸气", "可爱", "小蜜蜂"], ["霸气", "可爱", "可爱", "小蜜蜂"], ["1999.01.16", 27], [165, 127.5, "C"]]
count = my_list[1].count("可爱")
print(count)
print()

# 查询列表全部元素个数
count = len(my_list)
print(count)
print()

# 列表的遍历
my_list = [["霸气", "可爱", "小蜜蜂"], ["1999.01.16", 27], [165, 127.5, "C"]]
# while循环遍历
index = 0
while index < len(my_list):
    index1 = 0
    while index1 < len(my_list[index]):
        print(my_list[index][index1], end=" ")
        index1 += 1
    print()
    index += 1
print()
# while循环逆向遍历
index = -1
while index >= -len(my_list):
    index1 = -1
    while index1 >= -len(my_list[index]):
        print(my_list[index][index1], end=" ")
        index1 -= 1
    print()
    index -= 1
print()
# for循环遍历
for item in my_list:
    for item1 in item:
        print(item1, end=" ")
    print()
print()
