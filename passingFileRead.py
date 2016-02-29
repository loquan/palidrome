import sys

filename= str(sys.argv)

	
if len(sys.argv) > 1 :
	print(sys.argv[1])
else :
	print('pass in a file please')
	exit()
	
	
with open(sys.argv[1], 'r') as infile:

    data = infile.read()  # Read the contents of the file into memory.


my_list = data.splitlines()

print(my_list)
	

