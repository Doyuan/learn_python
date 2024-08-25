class Person(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # 访问器
    @property
    def name(self):
        return self.__name

    # 访问器 getter方法
    @property
    def age(self):
        return self.__age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self.__age = age

    def play(self):
        if self.__age <= 16:
            print("%s 正在玩飞行棋." % self.__name)
        else:
            print("%s 正在玩斗地主." % self.__name)


def main():
    person = Person("王大锤", 12)
    person.play()
    person.age = 22
    person.play()


if __name__ == '__main__':
    main()
