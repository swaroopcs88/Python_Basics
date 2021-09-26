# accepting string from keyboard
str1 = input("what is your name: ")
print("hi " + str1 + " nice to meet you!")


# accepting a single character or string from keyboard
ch = input("Enter a char: ")
print("you entered: ", ch)

# accepting a single character from keyboard
ch1 = input("Enter a char: ")
print("You entered: "+ch[0])

# accepting integer from keyboard
age = str(input("what's your age: "))
print("you are " + age +  " years old")

# accpeting float numbers from key board
x = float(input('Enter a number: '))
print('you entered: ', x)

# accepting two numbers from keyboard
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
print('You entered: ', a, b)

# display the numbers using a comma
print('You entered:  ', a, b, sep= ',')
print('You entered: %d, %d' %(a,b))


# find the sum of two numbers
i = int(input("Enter your first number: "))
j = int(input("Enter your second number: "))
print('The sum of ',i, ' and ', j, ' is ', i+j)
print('The sum of {} and {} is {}'.format(i,j, i+j))


# find sum and product of two numbers
q = int(input('Enter the first number: '))
w = int(input('Enter the second number: '))
# display sum
print('The sum of {0} and {1} is {2}'.format(q, w, q+w))
print('The product of {0} and {1} is {2}'.format(q, w, q*w))
# displat both sum and product
print('The sum of {0} and {1} is {2} and product of {0} and {1} is {3}'.format(q, w, q+w, q*w ))

# accepting input from other number systems
str3 = input('Enter hexadecimal number: ') # accept input as string
n = int(str3, 16) # inform the number is base 16
print('Hexadecimal to Decimal= ', n)

str4 = input('Enter octal number: ')
n = int(str4, 8) # inform the number is base 8
print('Octal to Decimal= ', n);


str5 = input('Enter binary number: ')
n = int(str5, 2) # inform the number is base 2
print('Binary to Decimal= ', n)

# accept more than one input in the same line - use loop along with input() function
r, t = [int(x) for x in input("Enter two numbers: ").split()]
print(r,t)

# accept 3 numbers separated by comma
var1, var2, var3 = [int(x) for x in input('Enter three numbers: ').split(',')]
print('Sum = ', var1+var2+var3)


# accepting group of strings from key board
lst = [x for x in input('Enter strings: ').split(',')]
print('You entered:\n', lst)


# using eval() along with input() function
x = eval(input("Enter an expression: "))
print("Result= %d" % x)



# accepting a list from keyboard
lst = eval(input("Enter a list: "))
print("List= ", lst)


# accepting a tuple from keyboard
tpl = eval(input("Enter a tuple: "))
print("Tuple= ", tpl)
