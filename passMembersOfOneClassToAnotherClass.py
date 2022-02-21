# WAP to create Emp class and make all the members of the
# Emp class available to another class i.e. Myclass


# this class contains employee details
class Emp:
    # this is a constructor
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    # this is an instance method
    def display(self):
        print('Id= ', self.id)
        print('Name= ', self.name)
        print('Salary = ', self.salary)

# this class displays employee details
class MyClass:
    # method to receive Emp class instance
    # and displays employee details
    @staticmethod
    def mymethod(e):
        # increment salary of e by 1000
        e.salary += 1000
        e.display()

# create Emp class instance e

e = Emp(12, 'Puneeth Raj Kumar', 1500000)
e = Emp(14, 'shivu', 232132)
e = Emp(16, 'ramu', 321321432)
# call static method of MyClass and pass e
MyClass.mymethod(e)

