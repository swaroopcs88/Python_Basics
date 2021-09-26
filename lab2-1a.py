# First code and test this. Invoke this function, pass 10 and 20 and
# verify if you get 30 as the result. Now pass “hello” and “world”
# as arguments and check the result.


# a function that exhibits polymorphism

def add(a, b):
    print(a+b)

# call add() and pass two integers

add(5,2,3) # displays 15

# call add() and pass two strings

add("hello", "world") # displays helloworld
