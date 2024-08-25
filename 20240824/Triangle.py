from math import sqrt


class Triangle(object):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self.__a + self.__b + self.__c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self.__a) * (half - self.__b) * (half - self.__c))


def main():
    a, b, c = 3, 4, 5

    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())

        print(t.area())
    else:
        print("无法构成三角形")


if __name__ == '__main__':
    main()
