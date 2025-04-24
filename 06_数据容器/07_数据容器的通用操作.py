# 数据容器的通用操作
my_list = ["霸气", "可爱", "小蜜蜂"]
my_tuple = ("霸气", "可爱", "小蜜蜂")
my_str = "霸气可爱小蜜蜂"
my_set = {"霸气", "可爱", "小蜜蜂"}
my_dict = {"霸气": 99, "可爱": 100, "小蜜蜂": 98}

# 获取最大元素
print(max(my_list))
print(max(my_tuple))
print(max(my_str))
print(max(my_set))
print(max(my_dict))
print()

# 获取最小元素
print(min(my_list))
print(min(my_tuple))
print(min(my_str))
print(min(my_set))
print(min(my_dict))
print()

# 容器转列表
print(list(my_list))
print(list(my_tuple))
print(list(my_str))
print(list(my_set))
print(list(my_dict))
print()

# 容器转元组
print(tuple(my_list))
print(tuple(my_tuple))
print(tuple(my_str))
print(tuple(my_set))
print(tuple(my_dict))
print()

# 容器转字符串
print(str(my_list))
print(str(my_tuple))
print(str(my_str))
print(str(my_set))
print(str(my_dict))
print()

# 容器转集合
print(set(my_list))
print(set(my_tuple))
print(set(my_str))
print(set(my_set))
print(set(my_dict))
print()

# 容器排序
print(sorted(my_list))
print(sorted(my_tuple))
print(sorted(my_str))
print(sorted(my_set))
print(sorted(my_dict))
print(sorted(my_list, reverse=True))
print(sorted(my_tuple, reverse=True))
print(sorted(my_str, reverse=True))
print(sorted(my_set, reverse=True))
print(sorted(my_dict, reverse=True))
print()