class Test(object):

    #初始化的功能
    #往往是完成对象的属性设置
    def __init__(self):
        self.num = 100
        print("-----init----")
        print(self)

    #完成创建一个对象
    #当a=Test()执行的时候，是先调用__new__方法完成创建对象，然后会紧接着
    #调用__init__方法，完成初始化的功能
    def __new__(cls):
        print("----new-----")
        print(cls)
        return super().__new__(cls)

    #def __str__(self):
    #   return "xxxxxx"


a = Test()
print(a.num)
print(a)

# 打印：  a 等价于 self
# ----new-----
# <class '__main__.Test'>
# -----init----
# <__main__.Test object at 0x000001EAB4250FD0>
# 100
# <__main__.Test object at 0x000001EAB4250FD0>