# 定义类

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print("%s正在学习%s" % (self.name, course_name))

    def watch_movie(self):
        if self.age <= 18:
            print("%s只能观看《熊出没》." % self.name)
        else:
            print("%s正在观看岛国爱情大电影." % self.name)


def main():
    stu = Student("东源", 23)
    stu.study("Python程序设计")
    stu.watch_movie()

    stu1 = Student("狗爬爬", 12)
    stu1.study("小学五年级语文")
    stu1.watch_movie()


if __name__ == '__main__':
    main()
