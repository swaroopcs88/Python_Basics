# program to display Fibonacci series
n = int(input("How many Fibonacci's ? "))
f1 = 0 # this is the first Fibonacci number
f2 = 1 # this is the second Fibonacci number
c = 2 # count the number of Fibonaccis
if n == 1:
    print(f1)
elif n == 2:
    print(f1, '\n', f2, sep='')
else:
    print(f1, '\n', f2, sep='')
    while c<n:
        f = f1 + f2 # add two fibonacci number to get the new one
        print(f)
        f1, f2 = f2, f # this is same as f1=f2, f2=f
        c += 1 # increment counter