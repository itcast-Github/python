def add(self, value):
    self.append(value)

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # print(cls)
        # print(name)
        # print(bases)
        # print(type(attrs))
        # attrs['add'] = lambda self, value: self.append(value)
        attrs['add'] = add
        attrs['name'] = 'Tom'
        return type.__new__(cls, name, bases, attrs)
        
class MyList(list, metaclass = ListMetaclass):  # 额外增加add方法，实际等价于append。
    pass

mli = MyList()
mli.add(1)
mli.add(2)
mli.add(3)
print(mli.name)
print(mli)
