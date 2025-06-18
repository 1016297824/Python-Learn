# 统计文件中“爱小”出现的次数
# 方法一：
with open("file.txt", "r", encoding="utf-8") as f:
    i = 0
    for line in f:
        i += line.count("爱小")
print(i)

# 方法二：
f = open("file.txt", "r", encoding="utf-8")
my_file = f.read()
print(my_file.count("爱小"))
f.close()