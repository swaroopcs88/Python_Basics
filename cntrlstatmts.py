"""
# to find area of the circle
import math # here math module is imported
r = float(input('Enter radius: '))
area = math.pi*r**2 # pi is a constant in math module
print('Area of circle= ', area)
print('Area of circle= {:0.2f}'.format(area))

# understanding the if statement
num = 1
if num == 1:
    print("One")

# understanding if statement
str = 'Yes'
if str == 'Yes':
    print("Yes")
    print("That's what you said")
    print("Your are awesome!")

# understanding indentation
x, y = 0, 2
if x == 1:
    print('a')
    print('b')
    if y == 2:
        print('c')
        print('d')
print('end')

# to know if a given number is even or odd
x = 8 # 3, 5, 7, 8, 4
if x % 2 == 0:
    print(x, " is even number")
else:
    print(x, " is odd number")


# using 'and' in if ... else statement
x = int(input('Enter a number: '))
if x >= 1 and x <= 10:
    print("You typed", x, "which is between 1 and 10")
else:
    print("You typed", x, "Which is below 1 or above 10")


# to know if a given number is zero or +ve or -ve
num = -87 # 4, 66, 31, -87
if num == 0:
    print(num, "is zero")
elif num > 0:
    print(num, "is positive")
else:
    print(num, "is negative")
    

# to display numbers from 1 to 10
x = 1
while x<= 10:
    print(x)
    x += 1
print('End')


# to display even numbers between 100 and 200

x = 100
while x >= 100 and x <= 200:
    print(x)
    x += 2
    


# python program to display even numbers between m and n

m, n = [int(i) for i in input("Enter minimum and maximum range: ").split(',')]

x = m # start from onwards

if x % 2 != 0: # if x is not even, start from next number
    x += 1

while x >= m and x <= n:
    print(x)
    x += 2
    


# to display each character from string

str7 = 'Hello'
for ch in str7:
    print(ch)


# to display each character from string - v2

str8 = 'How are you'
n = len(str8) # find number of characters in str
print('Length of string is ' +str(n))
for i in range(n):
    print(str8[i])


# to display odd numbers between 1 and 10

for i in range(1, 10, 2):
    print(i)



# display elements of a list using for loop
list = [10, 20.5, 'America', 'India', 'Chair', 'Door']
# display each element from the list
for item in list:
    print(item)




# to find the sum of list of numbers using for
# take a list of numbers

list1 = [10, 20, 30, 40, 50]
sum = 0 #initially sum is zero

for i in list1:
    print(i)
    sum += i
print('Sum = ', sum)


"""

# to find sum of list of numbers using while - v2
# take a list of numbers
list3 = [10, 20, 30, 40, 50]
sum = 0 #initially sum is zero
i = 0 #take a variable
while i < len(list3):
    print(list3[i]) # display elements from list
    sum += list3[i] # add each element to sum
    i += 1
print('Sum = ', sum)
