#定义一个猫类
class Cat:
    #属性

    #当创建完一个对象后，立马会自动调用
    def __init__(self,newColor,newWeight,newWeiba):
        self.color = newColor
        self.weight = newWeight
        self.weiba = newWeiba
        print("hahahahahah")

    #方法
    def eat(self):
        print("----吃-----")

    def drink(self):
        print("----喝-----")

    def sleep(self, a, b):
        print("-----睡觉----")
        print("---a=%d,b=%d----"%(a,b))

    def printInfo(self):
        print(self.weiba)
        #print(self.high)


#创建一个 猫 对象
xiaohuamao = Cat("花色",5,"有")
#xiaohuamao.eat()
#xiaohuamao.drink()
#xiaohuamao.sleep(11,22)

xiaohuamao.printInfo()
'''
#给xiaohuamao对象添加属性
xiaohuamao.color = "花色"
xiaohuamao.weight = 5 #kg
xiaohuamao.weiba = "有"

#获取xiaohuamao对象的数据
a = xiaohuamao.color
print(a)
print(xiaohuamao.weight)
print(xiaohuamao.weiba)

#注意：如果没有属性，那么还偏偏要访问这个属性，那么会产生一个异常
#print(xiaohuamao.high)








'''
