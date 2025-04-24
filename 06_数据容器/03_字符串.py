# 字符串操作
from itertools import count
my_str = "霸气可爱小蜜蜂"

# 字符串查询
index = my_str.index("可爱")
print(index)
print()

# 字符串替换
new_str = my_str.replace("小蜜蜂", "小州官")
print(my_str)
print(new_str)
print()

# 字符串的分割
my_str = "霸气 可爱 小蜜蜂"
my_list = my_str.split(" ")
print(my_str)
print(my_list)
print()

# 字符串的规整
my_str = "  霸气 可爱 小蜜蜂"
new_str = my_str.strip()
print(my_str)
print(new_str)
print()

my_str = "12121 霸气121 可爱 121221小蜜蜂121"
new_str = my_str.strip("12霸蜂")
print(my_str)
print(new_str)
print()

# 统计字符串中某字符出现的次数
my_str = "  霸气 可爱 小蜜蜂"
count=my_str.count(" ")
print(count)
print()

# 统计字符串的长度
my_str = "霸气 可爱 小蜜蜂"
len = len(my_str)
print(len)
print()