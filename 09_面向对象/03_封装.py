# 封装

class Phone:
    def __init__(self, money=16000, current_voltage=66):
        self.money = money
        # 私有变量
        self.__current_voltage = current_voltage

    # 私有方法
    def __keep_single_core(self):
        print("让CPU单核运行")

    def get_current_voltage(self):
        return self.__current_voltage


phone = Phone()
print(phone.money)
# print(phone.__keep_single_core)   # 报错，无法调用私有方法
print(phone.get_current_voltage())
# 不改变私有属性
phone.__current_voltage = 60
print(phone.__current_voltage)
print(phone.get_current_voltage())
