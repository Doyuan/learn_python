# 关键词参数

def func(a, b=3, c=10):
    print("a is ", a, "b is ", b, "c is ", c)


func(1, 2)
func(2, c=24)
func(c=100, a=12)


# 可变参数
def func(a=5, *number, **phone_back):
    print("a is", a)

    # 遍历所有元组中的选项
    for single_item in number:
        print('single_item is', single_item)

    # 遍历所有字典中选项
    for first_part, second_part in phone_back.items():
        print('first_part is', first_part, "second_part is", second_part)


func(3,1,2,3, Jack=1123, John=2231, Jam=3321)