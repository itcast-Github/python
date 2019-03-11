#coding=utf-8
class Person(object):

    def __init__(self,name,age):
        #只要属性名前面有2个下划线，那么就表示 私有的属性
        #所谓的私有，不能在外部使用 对象名.属性名获取
        #
        #原来没有添加__的属性，默认是 公有
        self.__name = name
        self.__age = age


    def setNewAge(self,newAge):
        if newAge>0 and newAge<=100:
            self.__age = newAge

    def getAge(self):
        return self.__age


    def __test(self):
        print("----test____")

    def test2(self):
        self.__test()
        print("------test2-----")

laowang = Person("老王",30)
laowang.setNewAge(31)
age = laowang.getAge()
print(age)


laowang.test2()

# 打印
# 31
# ----test____
# ------test2-----