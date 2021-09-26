# A python program to access all the instance variables of
# both the base classes in multiple inheritance
class A(object):
    def __init__(self):
        self.a = 'a'
        print(self.a)
        super().__init__()

class B(object):
    def __init__(self):
        self.b = 'b'
        print(self.b)
        super().__init__()

class C(A, B):
    def __init__(self):
        self.c = 'c'
        print(self.c)
        super().__init__()

# access the super class instance vars from C

o = C() # o is object of class C
