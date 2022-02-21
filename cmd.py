# to display command line args. save this as cmd.py

import sys

n = len(sys.argv) # n is the number of arguments

args = sys.argv # args list contains arguments


print('No. of command line args= ', n)
print('The args are: ', args)
print('The args one by one: ')
for a in args:
    print(a)
