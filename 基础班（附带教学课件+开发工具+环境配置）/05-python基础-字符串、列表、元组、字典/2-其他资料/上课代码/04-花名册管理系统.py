#coding=utf-8

#定义一个列表，用来存储所有的名字
names = []

while True:

    #1. 打印提示
    print("="*30)
    print("        欢迎使用xxxx系统 V6.8")
    print(" 1：添加新名字")
    print(" 2：删除一个名字")
    print(" 3：修改一个名字")
    print(" 4：查询一个名字")
    print(" 5：遍历所有的名字")
    print(" 0:退出系统")
    print("="*30)

    #2. 获取要操作的数字
    key = input("请输入您要数字:")

    #3. 根据选择，来做相应的事情
    if key=="1":
        #3.1 提示用户输入一个新名字
        insertName = input("请输入要添加的名字:")
        #3.2 把用户输入的名字添加到列表中
        names.append(insertName)
    elif key=="2":
        xxxxx
    elif key=="3":
        xxxxx
    elif key=="4":
        xxxxx
    elif key=="5":
        print("-"*40)
        for name in names:
            print(name)
    elif key=="0":
        xxxxx

