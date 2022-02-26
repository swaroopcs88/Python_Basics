"""
# WAP to accept string from keyboard and display it
str = input("Enter your name: ")
print('your name is: ', str)
# WAP to accept character as a string
ch = input("Enter a char: ")
print("U entered: " +ch)
# WAP to accept a single character from keyboard
ch = input("Enter a char: ")
print("U entered: " + ch[0])
# WAP to accept integer numbers from keyboard
# accepting integer from keyboard
str = input("Enter a number: ")
x = int(str) # convert str into int
print("u entered: ", x)
# WAP to accept integer number from keyboard
# accepting integer number from keyboard version 2
x = int(input("Enter a number: "))
print("U entered: ", x)
# WAP to accept float number from keyboard
x = float(input("Enter a number: "))
print("You entered: ", x)

# WAP to accept two integers from keyboard
# accepting two integers from keyboard
x = int(input("Enter a first number: "))
y = int(input("Enter a second number: "))
print('You entered: ', x , y)
print('You entered: ', x , y, sep=',')
print('You entered: ', x , y, sep=':')
"""
# WAP to accept two numbers and find their sum

# find sum of two numbers
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
print("The sum of two numbers {} and {} is {}".format(x, y, x+y)) # display sum
print("The sum of ', x, 'and ', y,' is", x+y) # display sum

# WAP to find sum and product of two numbers
# find sum and product of two numbers
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

# display sum
print('')