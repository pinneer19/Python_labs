# class MyObj(object):
#   def __init__(self):
#     self.name = 'Chuck Norris'
#     self.phone = '+6661'
#
# obj = MyObj()
# print(obj.__dict__)
# print(dir(obj))
a = dict()

# print(dict(type=int,data=d))
from types import CellType
print(CellType)

a = bytes(range(10))
print(a)
print(a.hex())