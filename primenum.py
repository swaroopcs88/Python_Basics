# a func to test whether a number is prime or not

def prime(n):
    """to check if n is prime or not"""
    x = 1 # this will be 0 if not prime

    for i in range(2, n): # divide n from 2 to n-1
        if n % i == 0: # if divisible by any number
            x = 0 # take x as 0
            break
        else:
            x = 1 # else take x as 1
        return x
# test if a number is prime or not
num = int(input('Enter a number: '))

# check if number is prime or not

result = prime(num)

if result == 1:
    print(num, ' is a prime')
else:
    print(num, ' is not a prime')
