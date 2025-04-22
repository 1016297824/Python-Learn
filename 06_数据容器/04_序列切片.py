# 视为序列的类型
"""
    列表（list）
    元组（tuple）
    字符串（string）
"""
# 对list进行切片
my_list = ["霸气", "可爱", "小蜜蜂", "霸气", "可爱", "小州官"]
new_list = my_list[1:4]  # 注意：步长默认为1，可以省略
print(my_list)
print(new_list)
print()

# 对tuple进行切片
my_tuple = ("霸气", "可爱", "小蜜蜂", "霸气", "可爱", "小州官")
new_tuple = my_tuple[:]  # 注意：从头到尾可以省略头尾
print(my_tuple)
print(new_tuple)
print()

# 对string进行切片
str = "霸气可爱小蜜蜂"
new_str = str[::2]
print(str)
print(new_str)
print()

# 对string进行逆向切片
str = "霸气可爱小蜜蜂"
new_str = str[::-1]  # 注意：逆向从头到尾可以省略头尾
print(str)
print(new_str)
print()

# 对list进行逆向切片
my_list = ["霸气", "可爱", "小蜜蜂", "霸气", "可爱", "小州官"]
new_list = my_list[5:1:-2]
print(my_list)
print(new_list)
print()

# 对tuple进行逆向切片
my_tuple = ("霸气", "可爱", "小蜜蜂", "霸气", "可爱", "小州官")
new_tuple = my_tuple[::-2]
print(my_tuple)
print(new_tuple)
print()
