# a function to test whether a number is prime or not

def prime(n):
    """to check if n is prime or not"""

    x = 1 # this will be 0 if not prime

    for i in range(2, n):
        if n%i == 0:
            x = 0
            break
        else:
            x = 1
    return x

# generate prime, number series

num = int(input('How many primes do you want? '))

i = 2 # start with i value 2

c = 1 # this counts the number of primes

while True: # repeat forever
    if prime(i):
        print(i)
        c += 1 # increase counter
    i+=1 # generate next number to test
    if c>num: # if count exceeds num
        break # come out of while loop
