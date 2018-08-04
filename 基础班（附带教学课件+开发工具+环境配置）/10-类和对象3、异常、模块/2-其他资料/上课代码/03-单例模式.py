

class Singleton(object):
    
    __instance = None

    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
        return cls.__instance






a = Singleton()
print(a)
b = Singleton()
print(b)
