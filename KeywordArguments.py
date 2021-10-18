# Functions can also be called using keyword arguments of the form kwarg=value
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("--This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("--Lovely plumage, the", type)
    print("--It's", state, "!")

# accepts one required argument (voltage) and three optional arguments (state, action, and type).
# parrot(1000)   # 1 positional argument
# parrot(voltage=1000) # 1 keyword argument
# parrot(voltage=1000, action='VOOOOOOM') # 2 keyword argument
# parrot(action='VOOOOOOM', voltage=100000000000) # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump') # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies') # 1 positional, 1 keyword

# but all the following calls would be invalid:

# parrot() # required argument missing
# parrot(voltage=5.0, 'dead') # non-keyword argument after a keyword argument
# parrot(110, voltage=220) # duplicate value for the same argument
# parrot(actor='John Clesse') # unknown keyword argument
