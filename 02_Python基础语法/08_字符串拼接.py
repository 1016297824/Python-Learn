
# 字符串的拼接方式
kawayi = "霸气可爱"
baobao = "小州官"
heti = kawayi + baobao
test = "霸气可爱"   "小州官"
print(kawayi)
print(baobao)
print(heti)
print(test)
print("\n")

# 字符串站位拼接，%s将变量转换成字符串拼接
shengao = 165
quanjin = 900
message = "霸气可爱小州官 身高 %s cm，一拳 %s 斤" % (shengao, quanjin)
print("霸气可爱小州官 身高 %s cm，一拳 %s 斤" % (shengao, quanjin))
print(message)
print("\n")

# 字符串站位拼接，%d、%f原装拼接
shengao = 165.5
quanjin = 900
message = "霸气可爱小州官 身高 %.2f cm，一拳 %d 斤" % (shengao, quanjin)
print("霸气可爱小州官 身高 %7.2f cm，一拳 %5d 斤" % (shengao, quanjin))
print(message)
# 破坏性测试
print("\n破坏性测试")
message = "霸气可爱小州官 身高 %d cm，一拳 %.2f 斤" % (shengao, quanjin)
print("霸气可爱小州官 身高 %d cm，一拳 %.2f 斤" % (shengao, quanjin))
print(message)
print("\n")

# 使用f"内容{变量}"快速格式化
# f为format缩写
# 注：此方法不对数据做精度控制
shengao = 165.5
quanjin = 900
message = f"霸气可爱小州官 身高{shengao}cm，一拳{quanjin}斤"
print(message)
print("\n")

# 表达式的格式化
shouru = 15798.5
zhichu = 5748
print("1-利润为：%d" % (shouru - zhichu ))
print(f"2-利润为：{shouru - zhichu}")
print("利润类型为：%s" % type(shouru - zhichu))
print("\n")

shouru = 15798.5
zhichu = 5748
print("1-利润为：%.2f" % (shouru - zhichu ))
print(f"2-利润为：{shouru - zhichu}")
print("利润类型为：%s" % type(shouru - zhichu))
print("3-正利润为：%.2f，负利润为：%.2f" % (shouru - zhichu, zhichu -shouru))