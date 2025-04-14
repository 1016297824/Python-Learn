
# if语句练习
age = input("你今年多少岁了：")
age = int(age)
if age >= 18:
    print("你已经成年了")
    print("可以独立生活了")
else:
    print("你还没成年")
    print("需要父母的陪伴")
print("练习完成\n")

# elif语句练习
if age < 12:
    print("你是小学生")
elif age < 16:
    print("你是中学生")
else:
    print("你是大学生")
print("学业顺利\n")