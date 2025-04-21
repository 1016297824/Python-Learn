# 元组
# 定义
("霸气", "可爱", "小蜜蜂")
tuple_name = ("霸气", "可爱", "小蜜蜂")
tuple_name = ()
tuple_name = tuple()

# 单个元组定义
# 注：必须加“逗号”
tuple_One = ("One",)

# 元组嵌套
tuple_name = (("霸气", "可爱", "小蜜蜂"), ("1999.01.16", 27), (165, 127.5, "C"))
print(tuple_name)
print(type(tuple_name))
print()

# 查找某一元素位置
name = tuple_name[0].index("小蜜蜂")
print(name)
print()

# 查找某一元素出现次数
tuple_name = ("霸气", "可爱", "可爱", "小蜜蜂", "可爱")
count = tuple_name.count("可爱")
print(count)
print()

# 统计元组内所有元素个数
tuple_name = (("霸气", "可爱", "小蜜蜂"), ("1999.01.16", 27), (165, 127.5, "C"), 5, 8)
print(len(tuple_name))
print()

# while循环遍历元组
tuple_name = (("霸气", "可爱", "小蜜蜂"), ("1999.01.16", 27), (165, 127.5, "C"))
index = 0
while index < len(tuple_name):
    index1 = 0
    while index1 < len(tuple_name[index]):
        print(tuple_name[index][index1], end=" ")
        index1 += 1
    print()
    index += 1
print()

# while循环逆向遍历元组
tuple_name = (("霸气", "可爱", "小蜜蜂"), ("1999.01.16", 27), (165, 127.5, "C"))
index = -1
while index >= -len(tuple_name):
    index1 = -1
    while index1 >= -len(tuple_name[index]):
        print(tuple_name[index][index1], end=" ")
        index1 -= 1
    print()
    index -= 1
print()

# for循环遍历元组
tuple_name = (("霸气", "可爱", "小蜜蜂"), ("1999.01.16", 27), (165, 127.5, "C"))
for index in tuple_name:
    for item in index:
        print(item, end=" ")
    print()
print()

# 元组嵌套列表
tuple_name = (("霸气", "可爱", "小蜜蜂"), ["1999.01.16", 27], (165, 127.5, "C"))
print(tuple_name)
tuple_name[1].insert(1, "宝宝")
print(tuple_name)
tuple_name[1].clear()
print(tuple_name)
# 错误示范，嵌套的列表可修改，但不可清空
tuple_name[1] = None
print(tuple_name)
