# Change the function to accept any number of numbers
# and sum it up and return the result(hint: use varargs).
def add(*num):
    
    sum = 0

    for n in num:
        sum = sum + n

    print("Sum: ", sum)

add(3,5)
add(4,5,6,7)
add(1,2,3,4,5)
