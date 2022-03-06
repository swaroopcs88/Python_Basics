# accessing elements of an array using index
from array import *
x = array('i',[10, 20, 30, 40, 50])

# find the number of elements in the array
n = len(x)

# display array elements using indexing
i = 0
while i<n:
    print(x[i], end=' ')
    i += 1
    