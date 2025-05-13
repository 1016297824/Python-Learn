# 类型注解
import random
import json

# 基础数据类型注解
var_1: int = None
var_2: str = None
var_3: bool = None


# 类对象的类型注解
class Student():
    pass


stu: Student = Student()

# 基础容器类型注解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, "霸气可爱小蜜蜂", True)
my_dict: dict = {"霸气可爱小蜜蜂": 666}
# 详细容器类型注解
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int, str, bool] = (1, "霸气可爱小蜜蜂", True)
my_dict: dict[str, int] = {"霸气可爱小蜜蜂": 666}

# 在注释中引入类型注解
var_4 = random.randint(1, 10)  # type:int
vat_5 = json.loads('{"name":"zhang"}')  # type:dict[str,str]


def func():
    return 10


var_6 = func()  # type:int
