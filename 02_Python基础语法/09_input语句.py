
# input语句使用
print("请告诉我你是谁")
name = input()
print(f"你的名字是{name}")

# 等同语句
name = input("请告诉我你是谁？\n")
print("我是%s" % name)

# 输入数字类型
num = input("数字：")
print("原类型：", type(num), "结果：", num)
num = float(num)
print("转换后的类型：", type(num), "结果：%.2f" % num)
#四舍五入
print("四舍五入：", round(num, 2))

