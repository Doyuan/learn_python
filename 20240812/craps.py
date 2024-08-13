"""
Craps赌博游戏
两个骰子 如果第一次摇出7点或11点 玩家胜
如果摇出2 3 12点庄家胜 其他情况游戏继续

玩家再次摇骰子 摇出7点庄家胜 如果摇出第一次摇出的点数 玩家胜

否则游戏继续 玩家继续摇骰子
玩家进入游戏时有1000元 全部输光游戏结束
"""
import random

money = 1000
while money > 0:
    print("你的总资产为:", money)
    needs_go_on = False
    while True:
        debt = int(input("请下注: "))
        if 0 < debt <= money:
            break
        first = random.randint(1, 6) + random.randint(1, 6)
        print("玩家摇出了%d点" % first)
        if first == 7 or first == 11:
            print("玩家胜！")
            money += debt
        elif first == 2 or first == 3 or first == 12:
            print("庄家胜！")
            money -= debt
        else:
            needs_go_on = True

        while needs_go_on:
            current = random.randint(1, 6) + random.randint(1, 6)
            print("玩家摇出了%d点" % current)
            if current == 7:
                print("庄家胜！")
                money -= debt
                needs_go_on = False
            elif current == first:
                print("玩家胜！")
                money += debt
                needs_go_on = False

print("你破产了，游戏结束！")
