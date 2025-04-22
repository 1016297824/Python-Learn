# 字符串操作
from itertools import count

str = "霸气可爱小蜜蜂"

# 字符串查询
index = str.index("可爱")
print(index)
print()

# 字符串替换
new_str = str.replace("小蜜蜂", "小州官")
print(str)
print(new_str)
print()

# 字符串的分割
str = "霸气 可爱 小蜜蜂"
my_list = str.split(" ")
print(str)
print(my_list)
print()

# 字符串的规整
str = "  霸气 可爱 小蜜蜂"
new_str = str.strip()
print(str)
print(new_str)
print()

str = "12121 霸气121 可爱 121221小蜜蜂121"
new_str = str.strip("12霸蜂")
print(str)
print(new_str)
print()

# 统计字符串中某字符出现的次数
str = "  霸气 可爱 小蜜蜂"
count=str.count(" ")
print(count)
print()

# 统计字符串的长度
str = "霸气 可爱 小蜜蜂"
len = len(str)
print(len)
print()