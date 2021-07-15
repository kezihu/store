# -*- coding: utf-8 -*-
# @Time    : 2021/7/15 15:25
# @Author  : Kevin_liu
# @File    : demo.py
import random

data = random.randint(0,10) #产生随机数
money = 2000 #金币
count = 0 #次数
while True:
    if money <= 0 or count > 10:
        print('对不起，您的金币不足！游戏结束！')
        break
    else:
        count = count + 1
        money = money - 200
        guessNum = input('请输入您猜的数字：\n')
        if guessNum.isdigit():
            guessNum = int(guessNum)
            if data > guessNum:
                print('小了')
            elif data < guessNum:
                print('大了')
            else:
                money = money + 5000
                print('恭喜您，猜对了！您一共猜测了',count,'次，您当前剩余',money,'金币')
                a = int(input('请问您是否要继续游戏？1.继续 2.退出\n'))
                if a == 2:
                    print("Bye!期待您下次的来玩！")
                    break
                else:
                    print('新的一轮游戏开始了！')
                    data = random.randint(0,10) #产生随机数
                    count = 0 #次数
        else:
            print('请输入数字！')




