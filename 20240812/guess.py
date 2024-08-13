# 猜数字游戏
import random

answer = random.randint(1, 100)

# 猜的次数
count = 0

while True:
    count += 1
    number = int(input('请输入一个数字: '))
    if number < answer:
        print("大一点")
    elif number > answer:
        print("小一点")
    else:
        print("恭喜你答对了")
        break

print('你总共猜测了%d次' % count)

if count > 7:
    print("你的智商余额明显不足")
