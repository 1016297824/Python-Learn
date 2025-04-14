
# 判断语句嵌套
print("欢迎来到动物园")
if int(input("您的身高是：")) > 120:
    print("您不是小朋友")
    if int(input("您的会员等级是：")) > 3:
        print("您是高级会员，可以免费游玩")
    else:
        print("您会员等级不足，请补票")
else:
    print("您是小朋友，可以免费游玩")