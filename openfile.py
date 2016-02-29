





with open('file.txt', 'r') as infile:

    data = infile.read()  # Read the contents of the file into memory.


my_list = data.splitlines()

print(my_list)