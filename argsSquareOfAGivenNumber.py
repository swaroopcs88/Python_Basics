# WAP using argument parser to find the square of a given number
import argparse

# create ArgumentParser Class Object
parser = argparse.ArgumentParser(description='This program displays the square value of a given number')

# add one argument with the name num and type as integer
parser.add_argument("num", type=int, help="Please input integer type number.")

# retrieve the arguments passed to the program
args = parser.parse_args()

# find the square of the argument passed
result = args.num**2
print("Square value= ", result)