# 类的封装
class Phone:
    def __init__(self,enable = True):
        self.__is_5g_enable = enable

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5G开启")
        else:
            print("5G关闭，使用4G网络")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

phone = Phone()
phone.call_by_5g()

phone1 = Phone(False)
phone1.call_by_5g()