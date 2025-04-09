

# 整数转字符串
print("整数转字符串")
zhengshu = 11
print(type(zhengshu))

str_zhengshu = str(zhengshu)
print("原版：", type(zhengshu), "字符串", type(str_zhengshu))

# 小数转字符串
print("\n小数转字符串")
xiaoshu = 123.456
print(type(xiaoshu))

str_xiaoshu = str(xiaoshu)
print("原版：", type(xiaoshu), "字符串", type(str_xiaoshu))

# int 转 float
print("\nint 转 float")
zhengshu = 11
print(type(zhengshu))

float_zhengshu = float(zhengshu)
print("整数值：", zhengshu, "小数值：", float_zhengshu)
print("整数：", type(zhengshu), "小数：", type(float_zhengshu))

# 4舍float 转 int
print("\n4舍float 转 int")
xiaoshu1 = 123.456
print(type(xiaoshu1))

zhengshu1 = int(xiaoshu1)
print("小数值：", xiaoshu1, "整数值：", zhengshu1)
print("小数：", type(xiaoshu1), "整数：", type(zhengshu1))

# 5入float 转 int
print("\n5入float 转 int")
xiaoshu2 = 123.654
print(type(xiaoshu2))

zhengshu2 = int(xiaoshu2)
print("小数值：", xiaoshu2, "整数值：", zhengshu2)
print("小数：", type(xiaoshu2), "整数：", type(zhengshu2))

# 小数字符串转整数
"""
    经测试小数字符串无法转变为整数
    测试代码如下
"""
# print("\n小数字符串转整数")
# str_xiaoshuzifu = "123.456"
# print(type(str_xiaoshuzifu))
#
# zhengshu = int(str_xiaoshuzifu)
# print("字符串值：", str_xiaoshuzifu, "整数值：", zhengshu)
# print("字符串：", type(str_xiaoshuzifu), "整数：", type(zhengshu))


# 整数字符串转小数
"""
    经测试小数字符串无法转变为整数
    测试代码如下
"""
print("\n整数字符串转小数")
str_zhengshu = "123"
print(type(str_zhengshu))

xiaoshu = float(str_zhengshu)
print("字符串值：", str_zhengshu, "小数值：", xiaoshu)
print("字符串：", type(str_zhengshu), "小数：", type(xiaoshu))

