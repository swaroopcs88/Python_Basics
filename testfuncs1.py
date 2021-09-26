import traceback
def test():
	print('howdy')
	print('done')
	for line in traceback.format_stack():
        print(line.strip())
        

test()
print('here')
test()
print('there')
test()
print('where')
