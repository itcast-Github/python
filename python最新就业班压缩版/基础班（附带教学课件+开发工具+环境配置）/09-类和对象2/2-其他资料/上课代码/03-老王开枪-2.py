class Ren:
    def __init__(self,name):
        self.name = name
        self.xue = 100

    def anzidan(self,danjia,zidan):
        danjia.baocunzidan(zidan)

    def andanjia(self,qiang,danjia):
        qiang.lianjiedanjia(danjia)


class Danjia:

    def __init__(self, rongliang):
        self.rongliang = rongliang
        self.rongnaList = []

    def __str__(self):
        return "弹夹当前的子弹数量为:" + str(len(self.rongnaList)) + "/" + str(self.rongliang)

    def baocunzidan(self,zidan):
        if len(self.rongnaList) < self.rongliang:
            self.rongnaList.append(zidan)
        

class Zidan:
    pass

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



laowang = Ren("老王")

danjia = Danjia(20)
print(danjia)

i=0
while i<5:
    zidan = Zidan()
    laowang.anzidan(danjia,zidan)
    i+=1

print(danjia)


qiang = Qiang()
print(qiang)
laowang.andanjia(qiang,danjia)
print(qiang)









