# WAP to accept 1 or more arguments and display them as list elements
# to find power value of a number
import argparse

# call the Arguemnt Parser()
parser = argparse.ArgumentParser()

# add the arguments to the parser
parser.add_argument('nums', nargs='+')

# retrieve the arguments into args object
args = parser.parse_args()

# display the arguments from the list: args.nums
for x in args.nums:
    print(x)