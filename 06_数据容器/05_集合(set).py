# 集合的定义
# 注意：集合会自动去重，且无序
from itertools import count

{"霸气", "可爱", "小蜜蜂"}
my_set = set()
my_set = {"霸气", "可爱", "小蜜蜂", "霸气", "可爱", "小州官"}
print(my_set)
print(type(my_set))
print()

# 添加元素
my_set.add("宇宙")
my_set.add("无敌")
my_set.add("大帅哥")
my_set.add("小州官")
print(my_set)
print()

# 删除元素
my_set.remove("大帅哥")
print(my_set)
print()

# 随机取出一个元素
element = my_set.pop()
print(element)
print(my_set)
print()

# 清空集合
my_set = {"霸气", "可爱", "小蜜蜂", "霸气", "可爱", "小州官"}
my_set.clear()
print(my_set)

my_set = {"霸气", "可爱", "小蜜蜂", "霸气", "可爱", "小州官"}
my_set = None
print(my_set)
print()

# 取2个集合的差
my_set1 = {"霸气", "可爱", "小蜜蜂"}
my_set2 = {"霸气", "可爱", "小州官"}
my_set3 = my_set1.difference(my_set2)
my_set4 = my_set2.difference(my_set1)
print(my_set1)
print(my_set2)
print(my_set3)
print(my_set4)
print()

# 消除集合中的差集
my_set1 = {"霸气", "可爱", "小蜜蜂"}
my_set2 = {"霸气", "可爱", "小州官"}
my_set3 = my_set1.difference_update(my_set2)
print(my_set1)
print(my_set2)
print(my_set3)
print()

# 将两个集合合并
my_set1 = {"霸气", "可爱", "小蜜蜂"}
my_set2 = {"霸气", "可爱", "小州官"}
my_set3 = my_set1.union(my_set2)
print(my_set1)
print(my_set2)
print(my_set3)
print()

# 统计集合的元素数量
my_set = {"霸气", "可爱", "小蜜蜂", "霸气", "可爱", "小州官"}
count = len(my_set)
print(my_set)
print(count)
print()

# 集合遍历
# 注意：集合不支持脚标，只能用for循环遍历
my_set = {"霸气", "可爱", "小蜜蜂", "霸气", "可爱", "小州官"}
print(my_set)
for item in my_set:
    print(item, end=" ")
print()