def init(self, name):
    self.name = name

def say_hello(self):
    print('Hello, %s!' % self.name)

# Hello = type('Hello', (object, ), dict(__init__ = init, hello = say_hello))
Hello = type('Hello', (object, ), {'__init__':init, 'hello':say_hello})
'''
class Hello:
    def __init__(...)
    def hello(...)
'''
h = Hello('Tom')
h.hello()
