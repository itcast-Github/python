import traceback

from types import MethodType

class MyClass(object):
    __slots__ = ['name', 'set_name']

def set_name(self, name):
    self.name = name

cls = MyClass()
cls.name = 'Tom'
cls.set_name = MethodType(set_name, cls)
cls.set_name('Jerry')
print(cls.name)
try:
    cls.age = 30
except AttributeError:
    traceback.print_exc()

class ExtMyClass(MyClass):
    pass

ext_cls = ExtMyClass()
ext_cls.age = 30
print(ext_cls.age)
