# 对象和方法
class Student:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"你好，我是{self.name}")


stu = Student("霸气可爱小蜜蜂", 18)
stu.say_hello()
