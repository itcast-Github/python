class Cat(object):
    def __init__(self):
        self.__name = "abc"

    def __test(self):
        print("-----Cat test----")

    def run(self):
        print("-------跑-----")

class Bosi(Cat):
    
    def test(self):
        self.__test() 
        print(self.__name)

class Jiafei(Cat):
    pass


bosi = Bosi()

bosi.run()

bosi.test()
