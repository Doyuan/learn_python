
x = 50
def func(x):
    print('x is ', x)
    x = 2
    print('change local x to', x)


func(x)

print("x still is", x)

# 全局变量
y = 50

def func():
    global y
    print('y is', y)
    y = 2
    print('change global y to', y)

func()
print("Values of y is", y)