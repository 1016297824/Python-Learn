# Union类型
from typing import Union

my_list: list[Union[int, str]] = [1, 2, 3, "123456"]
my_dict: dict[str, [Union[str, int]]] = {"name": "霸气可爱小蜜蜂", "age": 18}


def func(data: Union[int, str]) -> Union[int, str]:
    pass
