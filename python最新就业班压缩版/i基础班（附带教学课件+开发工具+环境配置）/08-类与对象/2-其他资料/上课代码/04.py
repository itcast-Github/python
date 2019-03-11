class Dog:
    def __init__(self, newColor):
        self.color = newColor
    
    def bark(self):
        print("---旺旺叫----")

    def printColor(self):
        print("颜色为：%s"%self.color)

    def __str__(self):
        return "当前对象的颜色为:"+self.color

def test(AAA):
    AAA.printColor()

wangcai = Dog("白")
#wangcai.printColor()


xiaoqiang = Dog("黑")
#xiaoqiang.printColor()

#test(wangcai)


print(wangcai)
print(xiaoqiang)
print(id(wangcai))
print(id(xiaoqiang))

# 打印
# 当前对象的颜色为:白
# 当前对象的颜色为:黑
# 2534086476016
# 2534086476072