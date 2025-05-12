# 内置方法使用

class Student:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__ 的使用
    def __str__(self):
        return f"Student类对象，name: {self.name}, age: {self.age}"


stu = Student("霸气可爱小蜜蜂", 18)
print(stu)
print(str(stu))
print()
