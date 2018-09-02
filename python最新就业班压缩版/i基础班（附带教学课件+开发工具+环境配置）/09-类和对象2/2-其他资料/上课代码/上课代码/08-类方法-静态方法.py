class Test(object):
    #类属性
    num = 0


    #实例方法
    def __init__(self):
        #实例属性
        self.age = 1


    def test(self):
        print(self.age)

    @classmethod
    def setNum(cls,newNum):
        cls.num = newNum

    @staticmethod
    def printTest():
        print("当前这个程序，是验证Test类的")



a = Test()
print(Test.num)

#a.setNum(200)
Test.setNum(300)

print(Test.num)

Test.printTest()


#不允许使用类名访问实例属性
#print(Test.age)
Test.test()
