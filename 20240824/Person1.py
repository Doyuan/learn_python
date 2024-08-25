# 用户类
class Person1(object):
    __slots__ = ('__name', '__age', '__gender')

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self): return self.__name

    @property
    def age(self): return self.__age

    @age.setter
    def age(self, age): self.__age = age

    def play(self):
        if self.__age <= 16:
            print("%s 正在玩飞行棋" % self.__name)
        else:
            print("%s 正在玩斗地主" % self.__name)


def main():
    person = Person1("王大锤", 22)
    person.play()


if __name__ == '__main__':
    main()
