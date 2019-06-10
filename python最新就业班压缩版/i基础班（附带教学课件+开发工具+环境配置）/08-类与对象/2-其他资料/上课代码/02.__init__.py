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


# 1
class Tree:
    def __init__(self, shuzhi, yezi):
        self.shuzhi = shuzhi
        self.yezi = yezi
huyang = Tree('有树枝','有叶子 啊哈哈')
print(huyang.shuzhi)