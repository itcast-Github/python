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

# 打印
# -------跑-----
# Traceback (most recent call last):
#   File "03-单继承.py", line 25, in <module>
#     bosi.test()
#   File "03-单继承.py", line 14, in test
#     self.__test()
# AttributeError: 'Bosi' object has no attribute '_Bosi__test'