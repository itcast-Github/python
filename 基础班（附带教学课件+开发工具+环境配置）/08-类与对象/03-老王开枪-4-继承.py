class Ren:
    def __init__(self,name):
        self.name = name
        self.xue = 100
        self.qiang = None

    def __str__(self):
        return self.name + "剩余血量为:" + str(self.xue)

    def anzidan(self,danjia,zidan):
        danjia.baocunzidan(zidan)

    def andanjia(self,qiang,danjia):
        qiang.lianjiedanjia(danjia)

    def naqiang(self,qiang):
        self.qiang = qiang


    def kaiqiang(self,diren):
        self.qiang.she(diren)

    def diaoxue(self,shashangli):
        self.xue -= shashangli


class Danjia:

    def __init__(self, rongliang):
        self.rongliang = rongliang
        self.rongnaList = []

    def __str__(self):
        return "弹夹当前的子弹数量为:" + str(len(self.rongnaList)) + "/" + str(self.rongliang)

    def baocunzidan(self,zidan):
        if len(self.rongnaList) < self.rongliang:
            self.rongnaList.append(zidan)

    def chuzidan(self):
        #判断当前弹夹中是否还有子弹
        if len(self.rongnaList) > 0:
            zidan = self.rongnaList[-1]
            self.rongnaList.pop()

            return zidan
        else:
            return None
        

class Zidan:

    def __init__(self,shashangli):
        self.shashangli = shashangli

    def shanghai(self,diren):
        diren.diaoxue(self.shashangli)

class Qiang:

    def __init__(self):
        self.danjia = None

    def __str__(self):
        if self.danjia:
            return "枪当前有弹夹"
        else:
            return "枪没有弹夹"

    def lianjiedanjia(self,danjia):
        if not self.danjia:
            self.danjia = danjia

    def she(self,diren):
        zidan = self.danjia.chuzidan()
        if zidan:
            zidan.shanghai(diren)
        else:
            print("没有子弹了，放了空枪....")

class Sandan(Qiang):
    #反现了一个问题：继承来的she功能，不是我想要的，那么此时该怎么办呢？
    #答案：重写父类的这个方法
    def she(self, diren):
        i=0
        while i<3:
            super().she(diren)
            i+=1



# class Sandan(Qiang):
#     #反现了一个问题：继承来的she功能，不是我想要的，那么此时该怎么办呢？
#     #答案：重写父类的这个方法
#     def she(self, diren):
#         i=0
#         while i<3:
#             zidan = self.danjia.chuzidan()
#             if zidan:
#                 zidan.shanghai(diren)
#             else:
#                 print("没有子弹了，放了空枪....")

#             i+=1

class AK47(Qiang):
    pass

class M4A1(Qiang):
    pass

laowang = Ren("老王")

danjia = Danjia(20)
print(danjia)

i=0
while i<5:
    zidan = Zidan(5)
    laowang.anzidan(danjia,zidan)
    i+=1

print(danjia)


qiang = Sandan()
print(qiang)
laowang.andanjia(qiang,danjia)
print(qiang)


#创建一个敌人
diren = Ren("敌人")
print(diren)
laowang.naqiang(qiang)

laowang.kaiqiang(diren)
print(diren)
print(danjia)
laowang.kaiqiang(diren)
print(diren)
print(danjia)








