#用来保存学生的所有信息
stuInfos = []

#全局变量
#newName = ""
#newSex = ""
#newPhone = ""

#打印功能提示
def printMenu():
    print("="*30)
    print("      学生管理系统V1.0")
    print("1. 添加学生信息")
    print("2. 删除学生信息")
    print("3. 修改学生信息")
    print("4. 查询学生信息")
    print("5. 显示所有学生信息")
    print("6. 保存数据")
    print("0. 退出系统")
    print("="*30)

#获取一个学生的信息

def getInfo():

#    global newName
#    global newSex
#    global newPhone

    #3.1 提示并获取学生的姓名
    newName = input("请输入新学生的名字：")

    #3.2 提示并获取学生的性别
    newSex = input("请输入新学生的性别：(男/女)")

    #3.3 提示并获取学生的手机号码
    newPhone = input("请输入新学生的手机号码：")

    #通过列表的方式把数据整合成一个整体，然后返回
    #return [newName, newSex, newPhone]
    #通过元组的方式把数据整合成一个整体，然后返回
    #return (newName, newSex, newPhone)
    return {"name":newName, "sex":newSex, "phone":newPhone}
    


#添加一个新学生的信息
def addStuInfo():
    
    result = getInfo() #["aaaa","男","10086"]

    newInfo = {}
   # newInfo['name'] = result[0]
   # newInfo['sex'] = result[1]
   # newInfo['phone'] = result[2]
    newInfo['name'] = result["name"]
    newInfo['sex'] = result["sex"]
    newInfo['phone'] = result["phone"]

    stuInfos.append(newInfo)
    
#用来修改一个学生的信息
def modifyStuInfo():
    #3.1 提示并获取需要修改的学生序号
    stuId = int(input("请输入要修改的学生的序号："))

    result = getInfo()

    stuInfos[stuId-1]['name'] = result['name']
    stuInfos[stuId-1]['sex'] = result['sex']
    stuInfos[stuId-1]['phone'] = result['phone']


#保存当前所有的学生信息到文件中
def save2file():

    f = open("backup.data","w")

    #[{},{},{}]
    f.write(str(stuInfos))


    f.close()


#恢复数据
def recoverData():
    f = open("backup.data")
    content = f.read()
    stuInfos = eval(content)
    f.close()


def main():

    #恢复之前的数据
    recoverData()


    print(stuInfos)



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
            modifyStuInfo()

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
        elif key=='6':
            #保存数据到文件中
            save2file()



#调用主函数
main()
