#coding=utf-8

#1. 定义一个列表，里面有一些名字
names = ["xiaohong","xiaoming","laowang"]

#2. 获取一个要查找的名字
insertName = input("请输入您的名字:")

#3. 判断是否存在，并显示相应的提示
findFlag = 0
for name in names:
    if name==insertName:
        findFlag = 1
        break#如果在前面已经找到了需要的名字，那么就结束循环，因为剩下的不会再进行判断，所以提升了程序的运行效率
    #else:
    #   findFalg = 0


if findFlag == 1:
    print("找到了")
else:
    print("没有找到")
    names.append(insertName)



print("-"*20)
print(names)
