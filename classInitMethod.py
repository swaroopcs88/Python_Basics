# A sample class with init method
class Person:

    # init method or constructor
    def __init__(self, name):
        self.name = name

    # sample method
    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Nikhil')
p.say_hi()