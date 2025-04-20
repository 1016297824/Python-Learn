
# 函数使用，体温判断
def panduan(x):
    if x<=37.5:
        print(f"体温{x}，没有发烧")
    else:
        print(f"体温{x}，发烧了")

num = float(input("请输入你的体温："))
panduan(num)