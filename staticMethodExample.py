# another example for static method
class MyClass:
    # method to calculate x to the power of n
    @staticmethod
    def my_method(x, n):
        result = x ** n
        print('{} to the power of {} is {}'.format(x, n, result))

# call the static method
MyClass.my_method(5, 3)
MyClass.my_method(5, 4)
