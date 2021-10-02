# errors in python program
# compile-time errors
# runtime errors
# logical errors

# A python program to understand the compile-time error
# ex1: compile-time error
"""
x = 1

if x == 1
    print('where is colon?')
# SyntaxError: invalid syntax
"""

# a python program to demonstrate compile-time error
# another compile-time error
"""
x = 10
if x % 2 ==0:
    print(x, ' is divisible by 2')
        print(x, ' is even number')
# IndentationError: unexpected indent
"""
"""
# runtime errors
# A python program to understand runtime errors
# example for runtime error
def concat(a, b):
    print(a+b)

# callconcat() and pass arguments
concat('Hai', 25)
# TypeError: can only concatenate str (not "int") to str
"""

"""
# ex4: another runtime error
animal = ['Dog','Cat','Horse','Donkey']
print(animal[4])
#IndexError: list index out of range

"""


"""
# Logical Errors
# A python program to increment the salary of an employee by 15%
def increment(sal):
    sal = sal * 15/100
    return sal

# call increment() and pass salary
sal = increment(5000.00)
print('Incremented salary= %.2f' %sal)

"""

"""
compile time errors and logical errors can be eliminated by the programmer by modifying the program
source code. in case of runtime errors, when the programmer knows which type of error occurs, he has 
to handle by programmer are called exceptions.
"""

"""
# A python program to understand the effect of an exception
# an exception example
# open a file
f = open(r"D:\swaroop\hg\test.txt", "w")

# do some processing on the file
# accept a, b values, store the result of a/b into the file
a, b = [int(x) for x in input("Enter two numbers: ").split()]
c = a/b
f.write("writing %d into D:\swaroop\hg\test.txt" %c)

# close the file
f.close()
print('File closed')
"""


"""Exceptions, runtime error which can be handled by the programmer. That means if programmer can guess an error
in the program and he can do something to eliminate the harm caused by that error, then it is called an 'exception'.
if the programmer cannot do anything in case of an error, then it is called an 'error' and not an exception"""
"""
# A python program to handle the ZeroDivisionError exception
# an exception handling example
try:
    f = open(r"D:/swaroop/hg/test.txt", "w")
    a, b = [int(x) for x in input("Enter two numbers: ").split()]
    c = a/b
    f.write("writing %d into D:/swaroop/hg/test.txt" %c)

except ZeroDivisionError:
    print('Division by zero happened')
    print('Please do not enter 0 in input')

finally:
    f.close()
    print('File closed')

"""


"""
#ex8: A python program to handle syntax error given by eval() function
# example for syntax error
try:
    date = eval(input("Enter date: "))
except:
    print('Invalid date entered')
else:
    print('You entered: ', date)

"""

"""
#ex9: A python program to handle IOError produced by open function
# example for IOError
# accept a filename
try:
    name = input('Enter filename: ')
    f = open(name, 'r')

except IOError:
    print('File not found: ', name)

else:
    n = len(f.readlines())
    print(name, 'has', n, 'lines')
    f.close()
"""

"""
# ex10: A python program to handle multiple exceptions
# example for two exceptions
# a function to find total and average of list elements

def avg(list):
    tot=0
    for x in list:
        tot+=x
    avg = tot/len(list)
    return tot, avg

# call the avg and pass a list
try:
    t,a = avg([1,2,3,4,5,'a']) # here, give empty list and try
    print('Total = {}, average= {}'.format(t,a))
except TypeError:
    print('Type Error, please provide numbers. ')
except ZeroDivisionError:
    print('ZeroDivisonError, please do not give empty list. ')
"""


"""
#ex11: A python program to understand the usage of try and finally blocks
# try without except block
try:
    x = int(input('Enter a number: '))
    y = 1 / x
finally:

    print("we are not catching the exception.")
print("The inverse is: ", y)
"""

"""
#ex12: A python program using the assert statement and catching assertion error
# handling AssertionError
try:
    x = int(input('Enter a number between 5 and 10: '))
    assert x>= 5 and x <= 10
    print('The number entered: ', x)
except AssertionError:
    print('The condition is not fulfilled')

"""

"""
#ex13: A python program to use the assert statement with a message
# handling AssertionError - v 2.0
try:
    x = int(input('Enter a number between 5 and 10: '))
    assert x>= 5 and x<= 10, "Your input is not correct"
    print('The number entered: ', x)
except AssertionError as obj:
    print(obj)
"""
