chepiao = 0 # 1 表示有车票  0表示没有车票
changdu = 8 # 单位为cm，表示的是刀子的长度 ，超过10cm禁止携带

'''
if chepiao == 1:
    print("可以进入候车厅，等待列车到来")
    print("这里尽然还有wifi，还有妹子...")
    if changdu<=10:
        print("通过安检，好紧张")
        print("刚刚那个安检员好漂亮....")
        print("可以上车...")
        #还可以继续嵌套if
        #if xxx:
        #    print()
    else:
        print("没有通过安检")
        print("等待公安的处理")
else:
    print("请先购买车票，然后在过来检票")
'''



#方式2
chepiaoFlag = 0 #0表示没有通过第一道安检  1表示通过了

if chepiao == 1:
    print("可以进入候车厅，等待列车到来")
    print("这里尽然还有wifi，还有妹子...")
    chepiaoFlag = 1
else:
    print("请先购买车票，然后在过来检票")

if chepiaoFlag == 1:
    if changdu<=10:
        print("通过安检，好紧张")
        print("刚刚那个安检员好漂亮....")
        print("可以上车...")
        #还可以继续嵌套if
        #if xxx:
        #    print()
    else:
        print("没有通过安检")
        print("等待公安的处理")


#方式3（较难理解，但是也可以完成）

if chepiao == 1:
    print("可以进入候车厅，等待列车到来")
    print("这里尽然还有wifi，还有妹子...")
    chepiaoFlag = 1
else:
    print("请先购买车票，然后在过来检票")

if chepiaoFlag == 1 and changdu<=10:
    print("通过安检，好紧张")
    print("刚刚那个安检员好漂亮....")
    print("可以上车...")
    #还可以继续嵌套if
    #if xxx:
    #    print()
elif chepiaoFlag == 1 and changdu>10:
    print("没有通过安检")
    print("等待公安的处理")












