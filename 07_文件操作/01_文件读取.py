# 文件操作
# 打开文件
import time

f = open("test.txt", "r", encoding="utf-8")
print(type(f))
print()

# 文件读取
# read()
my_str = f.read(6)
print(type(my_str), "\n", my_str,end="")
print(f.read())
print()

# readLines() -> 返回列表对象
f = open("test.txt", "r", encoding="utf-8")
line = f.readlines()
print(type(line), "\n", line)
print(line[3])

# readLine() -> 返回字符串
f = open("test.txt", "r", encoding="utf-8")
line = f.readline()
print(type(line), "\n", line)
print()

# for循环读取文件行
f = open("test.txt", "r", encoding="utf-8")
for line in f:
    print(line,end="")
print()
print()

#关闭文件
# time.sleep(66666666)
f.close()

# with open() 操作文件
# 注意：执行完with open() 后，会自动关闭文件操作
with open("test.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line,end="")
print()