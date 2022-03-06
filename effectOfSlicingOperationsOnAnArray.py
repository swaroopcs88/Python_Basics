# accessing elements of an array using index
from array import *
x= array('i', [10, 20, 30, 40, 50])

# create array y with elements from 1st to 3rd from x
y = x[1:4]
print(y)

# create array y with elements from 0th till the last element in x
y = x[0:]
print(y)

# create array y with elements from 0th to 3rd from x
y = x[:4]
print(y)

# create array y with last 4 elements from x
y = x[-4:]
print(y)

# create y with last 4th element and with 3 [-4-(-1) = -3] elements
y = x[-4: -1]
print(y)

# create y with 0th to 7th elements from x
# stride 2 means, after 0th element, retrieve every second element from x
y = x[0:7:2]
print(y)