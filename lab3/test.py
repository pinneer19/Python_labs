class MyObj(object):
  def __init__(self):
    self.name = 'Chuck Norris'
    self.phone = '+6661'

obj = MyObj()
print(obj.__dict__)
print(dir(obj))