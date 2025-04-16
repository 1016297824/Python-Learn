
# for循环基础语法
str = "霸气可爱小蜜蜂"
for c in str:
    print(c, end=" ")
print()

# 统计可爱的个数
str1 = "霸可爱气可爱可爱小可爱蜜可爱蜂"
temp = ""
i = 0
for c in str1:
    if((temp + c) == "可爱"):
        i += 1
    temp = c
print("可爱的个数为%d" % i)