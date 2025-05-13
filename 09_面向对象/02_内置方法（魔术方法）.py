# 内置方法使用

class Student:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__ 内置方法（类信息输出）
    def __str__(self):
        return f"Student类对象，name: {self.name}, age: {self.age}"

    # __lt__ 内置方法（小于比较）
    def __lt__(self, other):
        return self.age < other.age

    # __le__ 内置方法（小于等于比较）
    def __le__(self, other):
        return self.age <= other.age

    # __gt__ 内置方法（大于比较）
    def __gt__(self, other):
        return self.age > other.age

    # __ge__ 内置方法（大于等于比较）
    def __ge__(self, other):
        return self.age >= other.age

    # __eq__ 内置方法（相等比较）
    def __eq__(self, other):
        return self.age == other.age

stu = Student("霸气可爱小蜜蜂", 18)
stu_other = Student("霸气可爱小州官", 20)
stu_other1 = Student("霸气可爱小州官", 20)

# __str__ 的使用
print(stu)
print(str(stu))
print()

# __lt__ 的使用
print(stu < stu_other)
print(stu_other < stu)
print()

# __le__ 的使用
print(stu <= stu_other)
print(stu_other <= stu)
print(stu_other <= stu_other1)
# print(stu_other == stu_other1)    # 不可用
print()

# __gt__ 的使用
print(stu > stu_other)
print(stu_other > stu)
print()

# __ge__ 的使用
print(stu >= stu_other)
print(stu_other >= stu)
print(stu_other >= stu_other1)
# print(stu_other == stu_other1)    # 不可用
print()

# __eq__ 的使用
print(stu == stu_other)
print(stu_other == stu_other1)
print()