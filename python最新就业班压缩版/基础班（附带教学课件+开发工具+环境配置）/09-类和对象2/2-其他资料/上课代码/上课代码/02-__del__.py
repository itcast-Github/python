#coding=utf-8
class Person(object):

    def __init__(self,name,age):
        #只要属性名前面有2个下划线，那么就表示 私有的属性
        #所谓的私有，不能在外部使用 对象名.属性名获取
        #
        #原来没有添加__的属性，默认是 公有
        self.__name = name
        self.__age = age

    def __del__(self):
        print("-----del------")


laowang = Person("老王",30)
laozhang = laowang
print(laowang)
print(laozhang)
print("--------1-------")
del laowang
#因为老王这个变量已经被删除了，所以不能够再次使用
#print(laowang)
print("-------0-------")
del laozhang
print("--------2--------")
print(laozhang)

