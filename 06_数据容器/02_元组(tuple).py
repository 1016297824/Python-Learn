# 元组
# 定义
("霸气", "可爱", "小蜜蜂")
my_tuple = ("霸气", "可爱", "小蜜蜂")
my_tuple = ()
my_tuple = tuple()

# 单个元组定义
# 注：必须加“逗号”
tuple_One = ("One",)

# 元组嵌套
my_tuple = (("霸气", "可爱", "小蜜蜂"), ("1999.01.16", 27), (165, 127.5, "C"))
print(my_tuple)
print(type(my_tuple))
print()

# 查找某一元素位置
name = my_tuple[0].index("小蜜蜂")
print(name)
print()

# 查找某一元素出现次数
my_tuple = ("霸气", "可爱", "可爱", "小蜜蜂", "可爱")
count = my_tuple.count("可爱")
print(count)
print()

# 统计元组内所有元素个数
my_tuple = (("霸气", "可爱", "小蜜蜂"), ("1999.01.16", 27), (165, 127.5, "C"), 5, 8)
print(len(my_tuple))
print()

# while循环遍历元组
my_tuple = (("霸气", "可爱", "小蜜蜂"), ("1999.01.16", 27), (165, 127.5, "C"))
index = 0
while index < len(my_tuple):
    index1 = 0
    while index1 < len(my_tuple[index]):
        print(my_tuple[index][index1], end=" ")
        index1 += 1
    print()
    index += 1
print()

# while循环逆向遍历元组
my_tuple = (("霸气", "可爱", "小蜜蜂"), ("1999.01.16", 27), (165, 127.5, "C"))
index = -1
while index >= -len(my_tuple):
    index1 = -1
    while index1 >= -len(my_tuple[index]):
        print(my_tuple[index][index1], end=" ")
        index1 -= 1
    print()
    index -= 1
print()

# for循环遍历元组
my_tuple = (("霸气", "可爱", "小蜜蜂"), ("1999.01.16", 27), (165, 127.5, "C"))
for index in my_tuple:
    for item in index:
        print(item, end=" ")
    print()
print()

# 元组嵌套列表
my_tuple = (("霸气", "可爱", "小蜜蜂"), ["1999.01.16", 27], (165, 127.5, "C"))
print(my_tuple)
my_tuple[1].insert(1, "宝宝")
print(my_tuple)
my_tuple[1].clear()
print(my_tuple)
# 错误示范，嵌套的列表可修改，但不可清空
my_tuple[1] = None
print(my_tuple)
