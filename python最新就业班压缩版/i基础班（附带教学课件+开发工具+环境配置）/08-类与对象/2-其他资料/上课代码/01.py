'''

#定义一个猫类
class Cat:
    #属性

    #方法
    def eat(self):
        print("----吃-----")

    def drink(self):
        print("----喝-----")

    def sleep(self):
        print("-----睡觉----")


    def printInfo(self):
        print(self.weiba)
        print(self.high)


#创建一个 猫 对象
xiaohuamao = Cat()
xiaohuamao.eat()
xiaohuamao.drink()
xiaohuamao.sleep()


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


xiaohuamao.printInfo()

'''


# 1
class Person:
    def eat(self):
        print('吃吃吃')

# xiaobai = new Person() 创建对象错误
xiaobai = Person()

xiaobai.eat()

xiaobai.color = '白色' # 引出02__init__的使用
print(xiaobai.color)



