#打印功能提示
def printMenu():
    print("="*30)
    print("      学生管理系统V1.0")
    print("1. 添加学生信息")
    print("2. 删除学生信息")
    print("3. 修改学生信息")
    print("4. 查询学生信息")
    print("5. 显示所有学生信息")
    print("0. 退出系统")
    print("="*30)


#添加一个新学生的信息
def addStuInfo():
    
    #3.1 提示并获取学生的姓名
    newName = input("请输入新学生的名字：")

    #3.2 提示并获取学生的性别
    newSex = input("请输入新学生的性别：(男/女)")

    #3.3 提示并获取学生的手机号码
    newPhone = input("请输入新学生的手机号码：")

    newInfo = {}
    newInfo['name'] = newName
    newInfo['sex'] = newSex
    newInfo['phone'] = newPhone

    stuInfos.append(newInfo)
    

#用来保存学生的所有信息
stuInfos = []

while True:
    #1. 打印功能提示
    printMenu()

    #2. 获取功能的选择
    key = input("请输入功能对应的数字：")

    #3. 根据用户的选择，进行相应的操作
    if key=="1":
        #添加学生信息
        addStuInfo()

    elif key == '3':
        #修改学生的信息
        #3.1 提示并获取需要修改的学生序号
        stuId = int(input("请输入要修改的学生的序号："))

        #3.2 重新输入学生的信息(姓名，性别，手机号码)
        #3.2.1 提示并获取学生的姓名
        newName = input("请输入新学生的名字：")

        #3.2.2 提示并获取学生的性别
        newSex = input("请输入新学生的性别：(男/女)")

        #3.2.3 提示并获取学生的手机号码
        newPhone = input("请输入新学生的手机号码：")

        stuInfos[stuId-1]['name'] = newName
        stuInfos[stuId-1]['sex'] = newSex
        stuInfos[stuId-1]['phone'] = newPhone


    elif key == '5':
        #print(stuInfos)
        print("="*30)
        print("学生的信息如下:")
        print("="*30)

        print("序号    姓名    性别   手机号码")
        i = 1
        for tempInfo in stuInfos:
            print("%d      %s      %s     %s"%(i, tempInfo['name'], tempInfo['sex'], tempInfo['phone'] ))
            i+=1


