"""
print('starting....')

def test(x):
    '''this is a test function which intelligently does nothing'''
    if isinstance(x, str)
    print('in test() x = ' +str(x))

test('hello sept')
test(10)

"""

# functions examples1
"""
print('start')


def test():
    """this is my test function which prints to monitor"""
    print('howdy')
    print('done')


test()
print('here')
test()
print('over')

"""
"""
# 1 Required arguments with single argument example

def test(x):
    """this is a function example to verify required argument types"""
    print(x)
    print('done')
# if no argument is passed. TypeError: test() missing 1 required positional argument: 'x' will be displayed
test()
# single argument passed
test('wassup')
test('hello')

# if you pass x it self as an argument.
print(x)
# NameError: name 'x' is not defined will be displayed
"""

"""
# 1. Required arguments with multiple arguments example
def test(x,y):
    """this is a function example to verify required argument types"""
    # suppose if I use only one argument inside the print for example
    # print(x) or print(y). only the first argument or the second argument
    # is printed on the screen
    print(x)
    print(y)
    # two arguments printed
    print(x, y)
    

test('howdy', 10)
test('Jack', 'Sparrow')
test(10, [10,20,30])
"""

# How are parameters passed in python?
# all parameters are passed by value i.e. passed by copy

# given a string check whether it contains vowels in it?
# to count the number of vowels
"""
def countVowels(x):
    """this is a function that counts the vowels present in it"""
    count = 0

    vowels = 'aeiou'
# has vowel ae
    x = 'abed'
# has a vowel e
    x = 'bed'
    for ch in x:
        if ch in vowels:
            count += 1
    return count
"""
# function - is a re-usable code block which can be re-used repetitively whenever needed.


# isinstance
# you can find out for any given variable what is its type, by using isinstance of()

# annotations in python examples
# what type I am expecting and what type is returned
# https://www.python.org/dev/peps/pep-3107/#:~:text=Function%20annotations%20are%20nothing%20more,meaning%20or%20significance%20to%20annotations.
# https://www.python.org/dev/peps/pep-3107/
# https://www.geeksforgeeks.org/python-docstrings/#

"""
Function annotations are nothing more than a way of associating arbitrary Python expressions 
with various parts of a function at compile-time.

By itself, Python does not attach any particular meaning or significance to annotations.
"""


# Example 1: Using triple single quotes
"""
def my_function():
	'''Demonstrates triple double quotes
	docstrings and does nothing really.'''

	return None

print("Using __doc__:")
print(my_function.__doc__)

print("Using help:")
help(my_function)

"""


# One-line Docstrings
"""
def power(a, b):
	'''Returns arg1 raised to power arg2.'''

	return a**b

print(power.__doc__)
"""



# 2. Default arguments
# here x is required argument
def count(x, y='aeiou'):
    count = 0
    for ch in x:
        if ch in y:
            count += 1
    return count
# only one argument is passed here and it is passed for x
count('wow this is nuts')
# two arguments are passed here.
count('this is crazy', 'abc')



# https://www.geeksforgeeks.org/default-arguments-in-python/


# Default Arguments:

# if no arguments are passed while calling the function. the default value i.e. assigned to
# arguments while declaring the argument will be passed to the function - keywordname = value
# student function contains 3 arguments out of which two arguments are assigned with default values
"""
def student(firstname, lastname ='Mark', standard ='Fifth'):

	print(firstname, lastname, 'studies in', standard, 'Standard')
# suppose no argument is passed. TypeError: student() missing 1 required positional argument: 'firstname'
student()
# required arguments - firstname
student('Swaroop')
# default arguments - lastname and standard. suppose if the user does not pass
# the value for these two arguments default values will be picked
student('Bharath')
student('Rakesh', 'Jeevan', 'first')
"""

# 3. keyword arguments

# Example #1: Calling functions without keyword arguments

"""
def student(firstname, lastname ='Mark', standard ='Fifth'):
	print(firstname, lastname, 'studies in', standard, 'Standard')

# In the first call, there is only one required argument and the rest arguments use the default values. 
# 1 positional argument
student('John')

#  In the second call, lastname and standard arguments value is replaced from default value to new passing value. 
# 3 positional arguments						
student('John', 'Gates', 'Seventh')	

# 2 positional arguments
student('John', 'Gates')				
student('John', 'Seventh')
"""


"""
# Example  # 2: Calling functions with keyword arguments

def student(firstname, lastname ='Mark', standard ='Fifth'):
	print(firstname, lastname, 'studies in', standard, 'Standard')

# 1 keyword argument
student(firstname ='John')

# 2 keyword arguments
student(firstname ='John', standard ='Seventh')

# 2 keyword arguments
student(lastname ='Gates', firstname ='John')


"""

# 4. Variable length arguments - variadic

# how many var args can be their in a function declaration?

# in which position the var args will be declared in a function

# def x(a, *y):
"""
# global variable - declared outside the function body
p = 100
# what is a local variable - a variable declared within the boundary of the function either at the header or the body

def f1(x):
    if isinstance(x, str):
        print('arg is a string')
    elif isinstance(x, int):
        print('arg is an int')
    else:
        print('type(x)')
f1('hello')
f1(33)
f1(True)
"""
# global variable
# global variable should not be created with one letter or two letter.
# it should be verbose, so that it is easy to understand.

p = 100

def f1(x):

    print(x)
    # local variable with a name same as global variable i.e. p
    p = 2
    # suppose if you want to modify the global variable value inside the function x
    global p
    p = 30
    y = 12
    print(p)
    print(y)
# function is called  by passing an argument 5
f1(5)
# here p is referring to the global variable which was declared outside of the function x
print(p)
