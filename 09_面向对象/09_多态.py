# 多态
class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


def make_noise(animal: Animal):
    animal.speak()


dog = Dog()
cat = Cat()
make_noise(dog)
make_noise(cat)
print()


class AC():
    def cool_wind(self):
        pass


class Midea(AC):
    def cool_wind(self):
        print("美的空调制冷")


class Gree(AC):
    def cool_wind(self):
        print("格力空调制冷")


midea = Midea()
gree = Gree()


def make_cool(ac: AC):
    ac.cool_wind()


make_cool(midea)
make_cool(gree)
