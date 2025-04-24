# 字典练习
# 字典如下
my_dict = {
    "王力宏": {"部门": "科技部", "工资": 3000, "级别": 1},
    "周杰伦": {"部门": "市场部", "工资": 5000, "级别": 2},
    "林俊杰": {"部门": "市场部", "工资": 7000, "级别": 3},
    "张学友": {"部门": "科技部", "工资": 4000, "级别": 1},
    "刘德华": {"部门": "市场部", "工资": 6000, "级别": 2}
}
# 对所有级别为1的员工，工资加1000，并上升一级
print("姓名", "\t", "部门", "\t", "工资", "\t", "级别", end="\n")
for key in my_dict.keys():
    print(key, "\t", my_dict[key]["部门"], "\t", my_dict[key]["工资"], "\t", my_dict[key]["级别"], end="\n")
print()
for key in my_dict:
    if my_dict[key]["级别"] == 1:
        my_dict[key]["工资"] += 1000
        my_dict[key]["级别"] += 1
print("姓名", "\t", "部门", "\t", "工资", "\t", "级别", end="\n")
for key in my_dict:
    print(key, "\t", my_dict[key]["部门"], "\t", my_dict[key]["工资"], "\t", my_dict[key]["级别"], end="\n")
print()
