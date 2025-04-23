# 字典的定义
# 注意：key必须是不可变类型
"""
    不可变类型：
    字符串(str)
    整数(int)
    浮点数(float)
    元组(tuple)
"""
{
    "霸气": 99,
    "可爱": 100,
    "小蜜蜂": 98
}
my_dict = {}
my_dict = dict()
my_dict = {"霸气": 99, "可爱": 100, "小蜜蜂": 98}
print(my_dict)
print()

# 字典的key不能重复
# 保留最后一个
my_dict = {
    "霸气": 99,
    "可爱": 100,
    "小蜜蜂": 98,
    "可爱": 666
}
print(my_dict)
print()

# 字典基于key获取value
my_dict = {"霸气": 99, "可爱": 100, "小蜜蜂": 98}
print(my_dict["霸气"])
print(my_dict["可爱"])
print(my_dict["小蜜蜂"])
print()

# 字典的嵌套
my_dict = {
    "小可爱": {
        "身高": 163,
        "体重": 100,
        "肉肉": 3
    },
    "小蜜蜂": {
        "身高": 164,
        "体重": 99,
        "肉肉": 2
    },
    "小州官": {
        "身高": 165,
        "体重": 98,
        "肉肉": 1
    }
}
print(my_dict)
print(my_dict["小可爱"]["身高"])
print(my_dict["小蜜蜂"]["体重"])
print(my_dict["小州官"]["肉肉"])
print()

# 字典中新增元素
my_dict = {"小霸气": 99, "小可爱": 100, "小蜜蜂": 98}
my_dict["小州官"] = 101
print(my_dict)
print()

# 字典更新元素
my_dict = {"小霸气": 99, "小可爱": 100, "小蜜蜂": 98}
my_dict["小霸气"] = 101
print(my_dict)
print()

# 删除元素
item = my_dict.pop("小霸气")
print(item)
print(my_dict)
print()

# 清空字典
my_dict.clear()
print(my_dict, " ", type(my_dict))
print()

# 取得字典中全部的key
my_dict = {"小霸气": 99, "小可爱": 100, "小蜜蜂": 98}
keys = my_dict.keys()
print(keys, " ", type(keys))
print()

# 遍历字典
my_dict = {"小霸气": 99, "小可爱": 100, "小蜜蜂": 98}
# 方法1：通过取得所有的key对象遍历
keys = my_dict.keys()
for key in keys:
    print(type(key), " ", key, " ", my_dict[key], end="\n")
print()
# 方法2：直接遍历字典
for key in my_dict:
    print(type(key), " ", key, " ", my_dict[key], end="\n")
print()

#统计字典的元素数量
count=len(my_dict)
print(count)
print()