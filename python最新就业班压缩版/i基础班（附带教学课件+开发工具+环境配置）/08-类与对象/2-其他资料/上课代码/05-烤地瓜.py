class SweetPotato:

    #用来完成一些初始化的工作
    def __init__(self):
        self.cookedLevel = 0
        self.cookedString = "生的"
        self.condiments = []

    def __str__(self):
        msg = "地瓜的生熟程度为:" + self.cookedString
        msg += " 等级为:" + str(self.cookedLevel)

        if len(self.condiments)>0:
            msg += " 作料为:"#作料为:芥末酱,番茄酱,酱油,自然
            for temp in self.condiments:
                msg +=  temp + ","
            msg = msg[:-1]
            #第2种方法
            #msg = msg.strip(",")
        else:
            msg += "当前没有添加任何作料"

        return msg

    #烤地瓜方法
    def cook(self, times):
        self.cookedLevel += times
        if self.cookedLevel>8:
            self.cookedString = "焦了"
        elif self.cookedLevel>5:
            self.cookedString = "熟了"
        elif self.cookedLevel>3:
            self.cookedString = "半生不熟"
        else:
            self.cookedString = "生的"

    #添加作料
    def addCondiments(self, temp):
        self.condiments.append(temp)



diGua = SweetPotato()
print(diGua)

diGua.cook(2)
print(diGua)

diGua.addCondiments("芥末酱")
print(diGua)
diGua.addCondiments("番茄酱")
print(diGua)
diGua.addCondiments("咖喱")
print(diGua)
diGua.addCondiments("孜然")
print(diGua)


diGua.cook(2)
print(diGua)
diGua.cook(3)
print(diGua)
diGua.cook(5)
print(diGua)

# 打印
# 地瓜的生熟程度为:生的 等级为:0当前没有添加任何作料
# 地瓜的生熟程度为:生的 等级为:2当前没有添加任何作料
# 地瓜的生熟程度为:生的 等级为:2 作料为:芥末酱
# 地瓜的生熟程度为:生的 等级为:2 作料为:芥末酱,番茄酱
# 地瓜的生熟程度为:生的 等级为:2 作料为:芥末酱,番茄酱,咖喱
# 地瓜的生熟程度为:生的 等级为:2 作料为:芥末酱,番茄酱,咖喱,孜然
# 地瓜的生熟程度为:半生不熟 等级为:4 作料为:芥末酱,番茄酱,咖喱,孜然
# 地瓜的生熟程度为:熟了 等级为:7 作料为:芥末酱,番茄酱,咖喱,孜然
# 地瓜的生熟程度为:焦了 等级为:12 作料为:芥末酱,番茄酱,咖喱,孜然