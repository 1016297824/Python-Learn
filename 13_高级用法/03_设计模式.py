# 两种设计模式：单例模式和工厂模式
from typing import Union
from strTools import str_tools

# 单例模式：节省内存和创建对象的开销
s1 = str_tools
s2 = str_tools

print(id(s1))
print(id(s2))
print()


# 工厂模式：易于维护，当某个子类名称改变时，仅需修改工厂类中的名称即可
class Person:
    def __init__(self):
        print("Person init called")


class Student(Person):
    def __init__(self):
        print("Student init called")


class Teacher(Person):
    def __init__(self):
        print("Teacher init called")


class Worker(Person):
    def __init__(self):
        print("Worker init called")


class PersonFactory:
    def __init__(self):
        print("Factory init called")

    def get_person(self, p_type: str) -> Union[Student, Teacher, Worker, None]:
        if p_type == 's':
            return Student()
        elif p_type == 't':
            return Teacher()
        elif p_type == 'w':
            return Worker()
        else:
            print("get error")
            return None


personFactory = PersonFactory()
student = personFactory.get_person("s")
teacher = personFactory.get_person("t")
worker = personFactory.get_person("w")
