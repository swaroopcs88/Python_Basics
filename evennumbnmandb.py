# to display even numbers between m and n
m, n = [int(i) for i in input("Enter minimum and maximum range:").split(',')]
x = m # start from m onwards
if x % 2 != 0 : # if x is not even, start from next number
    x = x + 1
    print('alli')
while x >= m and x <= n:
    print(x)
    print('illi')
    x += 2
