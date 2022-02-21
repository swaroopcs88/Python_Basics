# scope of a variable
# no more y here...

def print_stuff():
    print("calling print_stuff")
    print(4)
    z = 4
    print(z)
    print("exiting print_stuff")
    y = 1
print_stuff() # Name Error. this shouldn't surprise you since we haven't yet set y
y = 3 # only now do we associate the name 'y' with number 3
print_stuff() # the rest works fine
print(y)
