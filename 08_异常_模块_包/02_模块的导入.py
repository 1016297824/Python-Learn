# 模块的导入
# [from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]
# []中可以省略；*表示导入所有

import time
# from time import sleep
# from time import sleep as sl
# from time import *
# 注意：导入不同模块的同名函数时，会使用后导入的模块中的函数

print("你好")
time.sleep(5)
print("我好")
