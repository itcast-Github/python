import random

#1. 定义一个列表，嵌套的列表
rooms = [[],[],[]]

#2. 有一个列表，保存了8名老师的名字
teachers = ["A","B","C","D","E","F","G","H"]

#3. 随机把8名老师的名字添加到 第1个列表中
for name in teachers:
    #生成一个0到2之间的随机数，用来进行随机分配办公室
    randomNum = random.randint(0,2)
    #向randomNum标记的room中添加一个新的老师名字
    rooms[randomNum].append(name)

#打印出当前所有办公室中的老师信息
#print(rooms)
i = 1
for room in rooms:
    #print(room)
    print("办公室%d里面的老师姓名是:"%i)
    for name in room:
        print(name,end=" ")
    print("")
    i+=1

# 打印类似 注意end=" "的使用 
# 办公室1里面的老师姓名是:
# C D F
# 办公室2里面的老师姓名是:
# B H
# 办公室3里面的老师姓名是:
# A E G