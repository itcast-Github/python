import random

while True:#死循环
    #1. 让电脑产生一个数字
    computer = random.randint(0,2)
    #print("computer--->%d"%computer)

    #2. 提示用户并获取一个数字
    player = int(input("请选择 0剪刀 1石头 2布（提示:按9退出）:"))

    if player==9:
        break

    #3. 判断输赢，并显示相应的结果
    if (player==0 and computer==2) or (player==1 and computer==0) or (player==2 and computer==1):
        print("赢了，走。。。出去喝一杯")
    elif player == computer:
        print("平局，不要走，决战到天亮")
    else:
        print("输了，洗洗手再来")
