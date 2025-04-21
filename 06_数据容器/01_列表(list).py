# 列表
# 定义
["霸气", "可爱", "小蜜蜂"]
list_name = ["霸气", "可爱", "小蜜蜂"]
list_name = []
list_name = list()

# 二维列表
list_name = [["霸气", "可爱", "小蜜蜂"], ["1999.01.16", 27], [165, 127.5, "C"]]
print(list_name)
print(type(list_name))

for item in list_name:
    for item1 in item:
        print(item1, end=" ")
    print()

# 逆向输出列表内容
print()
print(list_name[-1][0], " ", type(list_name[-1][0]))
print(list_name[-1][1], " ", type(list_name[-1][1]))
print(list_name[-1][2], " ", type(list_name[-1][2]))
print()

# 列表的常用操作
# 查询元素位置
# 错误示范
# index1 = list_name.index("C")
# index2 = list_name.index(27)
# 正确查询
index1 = list_name[2].index("C")
index2 = list_name[1].index(27)
print(index1)
print(index2)
print()

# 修改列表元素
print(list_name[1][1], " ", type(list_name[1][1]))
list_name[1][1] = "26"
print(list_name[1][1], " ", type(list_name[1][1]))
print()

for item in list_name:
    for item1 in item:
        print(item1, end=" ")
    print()
print()

# 插入元素
list_name.insert(1, ["霸气", "可爱", "小州官"])
# 错误示范
# list_name.insert(1, 666666666666666666666666)
list_name.insert(1, [666666])
for item in list_name:
    for item1 in item:
        print(item1, end=" ")
    print()
print()

list_name[1].insert(0, 88888888)
for item in list_name:
    for item1 in item:
        print(item1, end=" ")
    print()
print()

# 在尾部追加元素
# 错误示范
# list_name.append(2222222)
list_name.append([2222222])
for item in list_name:
    for item1 in item:
        print(item1, end=" ")
    print()
print()

list_name[5].append(33333333)
for item in list_name:
    for item1 in item:
        print(item1, end=" ")
    print()
print()

# 删除元素
# 使用del关键字删除
del list_name[5]
for item in list_name:
    for item1 in item:
        print(item1, end=" ")
    print()
print()

# 使用pop方法删除
result = list_name.pop(1)
print(result)
print()
for item in list_name:
    for item1 in item:
        print(item1, end=" ")
    print()
print()

# 使用remove方法删除
list_name.remove(["霸气", "可爱", "小州官"])
for item in list_name:
    for item1 in item:
        print(item1, end=" ")
    print()
print()

# 清空列表
list_name.clear()
print(list_name)

list_name = [["霸气", "可爱", "小蜜蜂"], ["1999.01.16", 27], [165, 127.5, "C"]]
list_name = None
print(list_name)
print()

# 查询列表中某一元素的数量
list_name = [["霸气", "可爱", "小蜜蜂"], ["霸气", "可爱", "可爱", "小蜜蜂"], ["1999.01.16", 27], [165, 127.5, "C"]]
count = list_name[1].count("可爱")
print(count)
print()

# 查询列表全部元素个数
count = len(list_name)
print(count)
print()

# 列表的遍历
list_name = [["霸气", "可爱", "小蜜蜂"], ["1999.01.16", 27], [165, 127.5, "C"]]
# while循环遍历
index = 0
while index < len(list_name):
    index1 = 0
    while index1 < len(list_name[index]):
        print(list_name[index][index1], end=" ")
        index1 += 1
    print()
    index += 1
print()
# while循环逆向遍历
index = -1
while index >= -len(list_name):
    index1 = -1
    while index1 >= -len(list_name[index]):
        print(list_name[index][index1], end=" ")
        index1 -= 1
    print()
    index -= 1
print()
# for循环遍历
for item in list_name:
    for item1 in item:
        print(item1, end=" ")
    print()
print()
