# 捕获异常
# 注意：异常有传递性，会层层上传

# 基本语法
try:
    f = open("err.txt", "r", encoding="utf-8")
except:
    print("没有\"err.txt\"文件")
    f = open("err.txt", "w", encoding="utf-8")

# 捕获指定异常
try:
    # 1/0
    print(name)
except NameError as e:
    print("变量未定义异常")
    print(e)
print()

# 捕获多个异常
try:
    1 / 0
    print(name)
except (NameError, ZeroDivisionError) as e:
    if e != None:
        print("出现指定异常：", e)
    else:
        print("出现未知异常")
print()

# 捕获所有异常
try:
    print(name)
    1 / 0
except Exception as e:
    print(e)
print()

# 没有异常时执行文件
try:
    f = open("err.txt", "r", encoding="utf-8")
except Exception as e:
    print("捕获到异常：", e)
else:
    print("没有异常")
finally:
    f.close()