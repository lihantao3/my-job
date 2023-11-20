"""
说明：CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；
    其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负

Craps赌博游戏
我们设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所有的赌注
"""

from random import randint

class Craps(object):
    def __init__(self):
        self.money = 1000
        print('游戏开始，你的初始金额是1000￥。')

    def play(self, times):
        for i in range(times):
            if self.money >= 100:
                first = randint(1, 6)
                second = randint(1, 6)
                sum = first + second
                print('第一个骰子是%d点, 第二个骰子是%d点，本次点数为%d' % (first, second, sum))
                if sum == 7 or sum == 11:
                    self.money += 100
                    print('玩家胜利，余额+100')
                elif sum == 2 or sum == 3 or sum == 12:
                    self.money -= 100
                    print('庄家胜，余额-100')
                else:
                    new = 0
                    while new != 7 and new != sum:
                        first = randint(1, 6)
                        second = randint(1, 6)
                        new = first + second
                        print('本次点数为%d，继续投掷...' % new)
                    if new == 7:
                        self.money -= 100
                        print('庄家胜,余额-100')
                    else:
                        self.money += 100
                        print('玩家胜利，余额+100')
                print('您的余额为%d' % self.money)
            else:
                print('您的余额不足100元，已无法进行游戏。')

    def check_money(self):
        print('您当前的余额为%d' % self.money)



