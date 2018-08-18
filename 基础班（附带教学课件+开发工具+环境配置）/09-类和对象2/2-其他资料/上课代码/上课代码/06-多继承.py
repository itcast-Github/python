class Ma(object):
    def pao(self):
        print("-----100km/h--跑---")

    def jiao(self):
        print("-----马在叫-----")


class Lv(object):
    def tuowupin(self):
        print("-----托物品-----")

    def jiao(self):
        print("-----驴在叫-----")



class Luozi(Lv,Ma):
    pass


luozi = Luozi()
luozi.pao()
luozi.tuowupin()
luozi.jiao()


print(Luozi.__mro__)

