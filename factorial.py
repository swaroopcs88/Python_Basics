# a function to calculate factorial value
def fact(n):
    """to find factorial value"""
    prod = 1
    while n >= 1:
        prod = 1
        while n >= 1:
            prod *= n
            n -= 1

        return prod

# display factorials of first 10 numbers
# call fact() function and pass the numbers from 1 to 10

for i in range(1, 11):
    print('Factorial of {} is {}' .format(i, fact(i)))
