# 捕获异常

#基本语法
try:
    f = open("err.txt","r",encoding="utf-8")
except:
    print("没有\"err.txt\"文件")
    f = open("err.txt","w",encoding="utf-8")