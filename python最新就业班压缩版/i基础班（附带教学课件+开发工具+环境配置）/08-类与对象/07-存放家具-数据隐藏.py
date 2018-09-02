class Home:
    def __init__(self, area):
        self.area = area
        self.containsItem = []

    def __str__(self):
        msg = "家当前可用面积为:"+str(self.area)
        if len(self.containsItem)>0:
            msg += "\t"
            msg += "家里的物品有:"
            
            #msg += ",".join(self.containsItem)

            for temp in self.containsItem:
                #msg += temp.name + ","
                msg += temp.getName() + ","
            '''
            else:
                msg += "没有任何东西"
            '''
            msg = msg[:-1]
        return msg

    #添加一个新的物品到家里面
    def addItem(self, item):
        #if self.area > item.area:
        needArea = item.getArea()
        if self.area > needArea:
            self.containsItem.append(item)
            self.area -= needArea

class Bed:
    def __init__(self, name, area):
        self.name = name
        self.area = area
        
    def __str__(self):
        msg = self.name + "床的面积为:" + str(self.area)
        return msg

    def getName(self):
        return self.name

    def getArea(self):
        return self.area


#创建一个家对象
home = Home(128)
print(home)

bed = Bed("席梦思", 4)
print(bed)

home.addItem(bed)
print(home)

bed2 = Bed("硬板床", 3)
print(bed2)

home.addItem(bed2)
print(home)
