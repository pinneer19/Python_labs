# class MyObj(object):
#   def __init__(self):
#     self.name = 'Chuck Norris'
#     self.phone = '+6661'
#
# obj = MyObj()
# print(obj.__dict__)
# print(dir(obj))
import inspect

a = dict()

# print(dict(type=int,data=d))
from types import CellType

print(CellType)

a = bytes(range(10))
print(a)
print(a.hex())


class B:
    def hello(self):

        self.a = 5

A = 9
class A(B):
    def hello(self):
        A()
        a = 5


# print(dir(hello))

def get_class(method):
    cls = getattr(
        inspect.getmodule(method),
        method.__qualname__.split('.<locals>', 1)[0].rsplit('.', 1)[0],
        None
    )
    if isinstance(cls, type):
        return cls


def hello(num2):
    num1 = 9
    def printer():
        print(num1 + num2)
    return printer

# print(A().hello.__globals__)
# print(A().hello.__code__.co_names)
# print(get_class(A().hello) is not type(A()))
print(hello(6).__closure__[0].cell_contents)