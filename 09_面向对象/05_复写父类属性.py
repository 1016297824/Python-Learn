# 复写父类属性
class Phone:
    IMET = 19980116
    producer = "ZW"

    def __init__(self, IMET=19980116, producer="ZW"):
        self.IMET = IMET
        self.producer = producer

    def call(self):
        print("4G通话")


class NewPhone(Phone):
    IMET = 19990116
    producer = "WW"

    def __init__(self, IMET=19990116, producer="WW"):
        self.IMET = IMET
        self.producer = producer

    def call(self):
        print("5G通话")
        print("通话完毕，切换省电模式")
        # print("4G通话")
        # 调用父类方法
        Phone.call(self)
        super().call()

    def oldProducer(self):
        print(self.producer)
        print(Phone.producer)
        print(super().producer)


myPhone = NewPhone()
myPhone.call()
myPhone.oldProducer()
