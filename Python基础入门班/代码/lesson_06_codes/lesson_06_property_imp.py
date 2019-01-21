class MyProperty:
    def __init__(self, fget = None, fset = None, fdel = None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, cls):
        if self.fget:
            print('__get__')
            return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset:
            print('__set__')
            return self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel:
            return self.fdel(instance)

    def getter(self, fn):
        self.fget = fn
        
    def setter(self, fn):
        self.fset = fn

    def deler(self, fn):
        self.fdel = fn
        
class Student:
    @MyProperty
    def score(self):
        return self._score

    @score.setter
    def set_score(self, value):
        self._score = value

s = Student()
s.score = 95
print(s.score)
