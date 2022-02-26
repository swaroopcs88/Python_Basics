# WAP to add two numbers using argument parser
# to find sum of two given numbers

import argparse

# create ArgumentParser class object
parser = argparse.ArgumentParser(description= "This program calculates sum of two given numbers")

# add two arguments with the names n1 and n2 and type as float
parser.add_argument("n1", type=float, help="Input first number")
parser.add_argument("n2", type=float, help="Input second number")

# retrieve the arguments passed to the program
args = parser.parse_args()

# convert the n1 and n2 values into float type then add them
result = float(args.n1) + float(args.n2)
print("Sum of two= ", result)