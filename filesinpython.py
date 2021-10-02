"""
# ex1: python program to create a text file store individual characters
# creating files to store characters
# open the file for writing data
# f = open(r'D:\swaroop\hg\test.txt', 'a')
f = open(r'D:\swaroop\hg\test.txt', 'r')
# enter characters from key board
str = input('Enter text: ')

# write the string into file
# f.write(str)
# read the data from test.txt
str = f.read()
print(str)
# closing the file
f.close()
"""

"""
# ex2: A python program to store group of strings into a text file
# creating a file with strings
f = open(r'D:\swaroop\hg\test.txt', 'w')

# enter strings from keyboard
print('Enter text (@ at end): ')
while str != '@':
    str = input() # accept string into str
    # write the string into the file
    if(str != '@'):
        f.write(str+"\n")
# closing the file
f.close()
"""

"""
# ex3: python program to read all strings from a text file and display them
# open the file for reading data
# f = open(r'D:\swaroop\hg\test.txt', 'r')
# append data to existing "test.txt" and then display the data
f = open(r'D:\swaroop\hg\test.txt', 'a+')
# read strings from the file
print('The file contents are: ')
str = f.read()
# str = f.read()
print(str)

# closing the file
f.close()

"""


"""
# ex4: A python program to append data to an existing file and then displaying the entire file
# appending and then reading strings
# open the file for reading data
f = open('D:/swaroop/hg/test.txt', 'a+')

print('Enter text to append(@ at end): ')
while str != '@':
    str = input() # accept string into str

    # write the string into file
    if(str != '@'):
        f.write(str+"\n")

# put the file pointer to the beginning of file

f.seek(0,0)

# read strings from the file
print('The file contents are: ')
str = f.read()
print(str)

# closing the file
f.close()
"""



"""
# ex5: A python program to know whether the file exists or not
# checking if the file exists and then reading data
import os, sys

# open the file for reading the data
fname = input('Enter filename: ')

if os.path.isfile(fname):
    f = open(fname, 'r')
else:
    print(fname+' does not exist')
    sys.exit()

# read strings from the file
print('The file contents are: ')

str = f.read()
print(str)

# closing the file
f.close()
"""



"""
# ex8: A python program to count the number of lines, words and characters in a text file
# counting number of lines, words and characters in a file
import os, sys

# open the file for reading data
fname = input('Enter filename: ')

if os.path.isfile(fname):
    f = open(fname, 'r')
else:
    print(fname+' does not exist')
    sys.exit()

# initialize the counters at 0
cl = cw = cc = 0

# read line by line from the file
for line in f:
    words = line.split()

    cl += 1
    cw += len(words)
    cc += len(line)

print('No. of lines: ', cl)
print('No. of words: ', cw)
print('No. of characters: ', cc)

# close the file
f.close()
"""



"""Binary files - handle data in the form of bytes. Hence, they can be used to read or write text, 
images or audio and video files. To open a binary file for reading purpose, we can use 'rb' mode. Here, 
'b' is attached to 'r' to represent that it is a binary file. write bytes into a binary file, we can use 
'wb' mode. To read bytes from a binary file, we can use the read() method and write bytes into binary file, 
we can use the write() methods"""
"""
# ex9: A python program to copy an image file into another file

# copying an image into a file
# open the files in binary mode
f1 = open('D:\swaroop\swaroop_office_data\Swaroop_D-Drive\swaps\Dashing Swaroop\Resized Web Versions\Resized 006.jpg', 'rb')
f2 = open('D:\swaroop\swaroop_office_data\Swaroop_D-Drive\swaps\Dashing Swaroop\Resized Web Versions\Resized 119.jpg', 'wb')

# read bytes from f1 and write into f2

bytes = f1.read()
f2.write(bytes) 

# close the files
f1.close()
f2.close()
"""




"""with statement
can be used while opening a file. advantage of with statement is that it 
will take care of closing a file which is opened by it. hence, we need not close
the file explicitly. In case of an exception also, 'with' statement will close
the file before the exception is handled.
with open('filename','openmode') as fileobject:
"""



# ex10: A python program to use 'with' to open a file and write some strings into the file.
# with statement to open a file
with open('D:\swaroop\hg\sample.txt', 'r') as f:
    for line in f:
        print(line)

# ex