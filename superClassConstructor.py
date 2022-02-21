# example to confirm that the superclass contructor is called to initialize
# the instance of the subclass

class BaseData:
    def __init__(self, i):
        print(f'Constructor with argument {i}')

        self.id = i

class Data(BaseData):
    pass


d = Data(10)
print(type(d))
