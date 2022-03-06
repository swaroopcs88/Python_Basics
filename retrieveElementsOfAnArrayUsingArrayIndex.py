# accessing elements of an array using index
from array import *
x = array('i', [10, 20, 30, 40, 50])

# find number of elements in the array
n = len(x)

# display array elements using indexing
for element in range(n):
    print(x[element], end=',')
    #print(x[element], end=':')
    #print(x[element], end=' ')
