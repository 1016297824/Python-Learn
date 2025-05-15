# JSON数据格式
import json

# 准备工作
data = [
    {"name": "霸气可爱小蜜蜂", "age": 18},
    {"name": "霸气可爱小州官", "age": 19},
    {"name": "霸气可爱小懒虫", "age": 20}
]

# 将列表转化为JSON
json_data1 = json.dumps(data)
json_data2 = json.dumps(data, ensure_ascii=False)
print(type(json_data1))
print(json_data1)
print()
print(type(json_data2))
print(json_data2)
print()

# 将字典转化为JSON
my_dict = {"name": "霸气可爱小懒虫", "age": 18}
json_dict1 = json.dumps(my_dict)
print(type(json_dict1))
print(json_dict1)
print()
json_dict2 = json.dumps(my_dict, ensure_ascii=False)
print(type(json_dict2))
print(json_dict2)
print()

# 将JSON数据转化
json_str1 = '{"name": "霸气可爱小懒虫", "age": 18}'
data1 = json.loads(json_str1)
print(type(data1))
print(data1)
print()

json_str2='[{"name": "\u9738\u6c14\u53ef\u7231\u5c0f\u871c\u8702", "age": 18}, {"name": "\u9738\u6c14\u53ef\u7231\u5c0f\u5dde\u5b98", "age": 19}, {"name": "\u9738\u6c14\u53ef\u7231\u5c0f\u61d2\u866b", "age": 20}]'
data2 = json.loads(json_str2)
print(type(data2))
print(data2)
print()
