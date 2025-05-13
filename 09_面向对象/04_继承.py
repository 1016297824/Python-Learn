# 继承
class Phone:
    IMET = None  # 序列号
    producer = None  # 厂商

    def __init__(self, IMET=19980116, producer="ZW"):
        self.IMET = IMET
        self.producer = producer

    def call_by_4g(self):
        print("4G通话")


class Phone_2025(Phone):
    face_id = None

    def __init__(self, IMET=19980116, producer="ZW", face_id="0615"):
        self.IMET = IMET
        self.producer = producer
        self.face_id = face_id

    def call_by_5g(self):
        print("5G通话")


phone = Phone_2025()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()


# 多继承
class NFC_Reader:
    def __init__(self, NFC_type="第五代", producer="WW"):
        self.NFC_type = NFC_type
        self.producer = producer

    def NFC_read(self):
        print("NFC读卡")

    def NFC_write(self):
        print("NFC写卡")


class RemoteController:
    def __init__(self, rc_type):
        self.rc_type = rc_type

    def controll(self):
        print("红外线开启了")

# 注意：同名属性从左至右，左边优先级高，先继承，先保留
class New_Phone(NFC_Reader, Phone, RemoteController):
    pass


myPhone = New_Phone()
myPhone.call_by_4g()
myPhone.NFC_read()
myPhone.NFC_write()
myPhone.controll()
print(myPhone.producer)
