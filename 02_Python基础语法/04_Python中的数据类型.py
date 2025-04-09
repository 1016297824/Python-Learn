

#使用print直接输出类型信息
print("直接输出类型信息")
print(type(123))
print(type(13.14))
print(type("霸气可爱小蜜蜂"))

#使用变量存储type()结果
print("\n使用变量存储type()结果")
type_int = type(123)
type_float = type(13.14)
type_string = type("霸气可爱小蜜蜂")
type_result = type(type(123))

print(type_int)
print(type_float)
print(type_string)
print(type_result)

#使用type()查看变量的数据类型
print("\n使用type()查看变量的数据类型")
zhenshu = 123456789
xiaoshu = 123.456
zifuchuan = "霸气可爱小蜜蜂"
print(type(zhenshu))
print(type(xiaoshu))
print(type(zifuchuan))
