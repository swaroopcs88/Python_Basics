"""
# python global variables
# create a variable outside a function and use it inside the function
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()
"""
# create a variable inside a function, with the same name as global variable
"""
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)
"""
# create a global variable inside a function

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)