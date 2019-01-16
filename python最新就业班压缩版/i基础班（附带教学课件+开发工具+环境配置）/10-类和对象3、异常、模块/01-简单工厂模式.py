class AppleCake(object):
    def __init__(self, weidao="苹果味道"):
        self.taste = weidao


class OrangeCake(object):
    def __init__(self, weidao="橘子味道"):
        self.taste = weidao


class CakeFactory(object):
    def createCake(self, weidao):
        if weidao == "橘子":
            cake = OrangeCake()
        elif weidao == "苹果":
            cake = AppleCake()
        return cake


class CakeStore(object):

    def __init__(self):
        self.factory = CakeFactory()

    def taste(self, weidao):

        cake = self.factory.createCake(weidao)

        print("------品尝味道:%s----"%cake.taste)


a = CakeStore()
a.taste("橘子")
