# WAP to create an integer type array
import array
print(type(array))
print(array)
a = array.array('i', [4, 6, 2, 9, -3, -5, -1])
print(type(a))
print(a)
print('The array elements are: ')
for element in a:
    print(element)