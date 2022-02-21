# first we associate the name 'y' with the number 3
y = 3
#z = 4
print(z)
def print_stuff(): # then we associate the name print_stuff with this function
    print("calling print_stuff") # (***)
    print(y)
    #z = 12
    print(z)
    print("exiting print_stuff")

print_stuff() # we call print_stuff and the program execution goes to (***)
print(y) # works fine
print(z) # Name Error!!!
