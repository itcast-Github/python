class Cat(object):
    #设计一个类
    #1. 类名
    #2. 属性
    #3. 方法

    #类属性
    num = 0

    def __init__(self):
        #实例属性
        self.age = 1
        #如果类属性的名字和实例属性的名字相同，那么
        #通过对象去获取num的时候，那么会获取实例属性的值
        self.num = 100

    #方法
    def run(self):
        print("-----猫 在跑----")

mao = Cat()
#用对象去访问类属性是可以的
print(mao.num)
#常用的方式是，使用类去访问类属性
print(Cat.num)
Cat.num+=1
print(Cat.num)





