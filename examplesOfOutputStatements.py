# examples of print statements
# strings using double quotes
print("hello")
# strings using single quotes
print('Hello world!')
# escape sequence examples
print("""This is the \nfirst line""") 
print('''This is the \tfirst line''')
print('This is the \\n first line')
print("This is the \\tfirst line")
print('hai'*3)
print(3*'hello')
# concatenate(joining) operator
print("City name = " + "Hyderabad")
print("First name = " + "Supritha")
a = 2
print(a)
a , b = 2, 3
print(a,b)
# separator examples 
print(a, b, sep=',')
print(a, b, sep=':')
print(a, b, sep="------------------>")
# print output in same lines
print("Hello", end='')
print("Dear", end='')
print("How are you?", end='')
# print output in separate lines
print("Hello")
print("Dear")
print("How are you?")
# print output with tab space
print("Hello", end="\t")
print("Dear", end="\t")
print("How are you?", end="\t")
# print object statement
print('hello')
lst = [23, 'name', 'orange', 'apple', 32]
print(lst)
d = {'idly': 30, 'roti': 21, 'puri': 3, 'vada':2}
print(d)
a = 2
print(a, "is even number")
print('the number',a, 'is even')
# print formatted string statement
x = 10
print('value=%i' %x)
x, y = 10, 15
print('x=%i y=%d' %(x, y))
"""to display a string, we can use %s in the formatted string. When we use %20s, 
it will allot 20 spaces and the string is displayed right alignes in those spaces.
To align the string towards left side in the spaces, we can use %-20s."""

name = 'Linda'
age = '12'
print('Hai %s' % name)
print('my age is %s' % age)

print('Hai(%20s)' % name)
print('Hai (%-20s)' % name)

# to display single character
name = 'Linda'
print('Hai %c, %c' %(name[0], name[1]))
# display floating point values
num = 123.456789
print('The value is: %f' % num)
print("The value is: %8.2f" %num)
# replacement string denoted by a pair of curly braces
n1 , n2, n3 = 1, 2, 3
# observe{0} which was replaced by the value of n1, n2, n3
print('number1={0}'.format(n1))
print('number2={0}'.format(n2))
print('number3={0}'.format(n3))
print('number1={0}, number2={1}, number3={2}'.format(n1, n2, n3)) # display all three numbers, 0, 1 and 2 represent values of n1, n2 and n3 
print('number1={1}, number2={0}, number3={2}'.format(n1, n2, n3)) # if we change the order of the values, to be changed in the output as

# using names in replacement fields
print('number1={two}, number2={one}, number3={three}'.format(one=n1, two=n3, three=n2))
# using curly braces without mentioning indexes or names
name, salary = 'Ravi', 15000
print("Hello {0}, Your Salary is {1} ".format(name, salary))
print("Hello {n}, your salary is {s} ".format(n=name, s=salary))
print("Hello {:s}, your salary is {:2f}".format(name, salary))
print('Hello %s, your salary is %.2f'%(name, salary))
