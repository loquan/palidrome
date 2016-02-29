import sys


def readEachLine( testString ):
	word = str(testString);
	length = len(word)
	i=length
	final = []
	while i > 0:
		i -= 1
		if word[i] != ' ':
			final.append(word[i]); 
	null = ''
	reverse = null.join(final);	


	final.sort(reverse=True)
	sortString = null.join(final);	


	if reverse.lower() == word.lower() :
	  print("AY |",sortString)
	else :  
	  print("NAY |",sortString)
	

	
	

#reading a files
filename= str(sys.argv)


if len(sys.argv) > 1 :
	print(sys.argv[1])
else :
	print('pass in a file please')
	exit()
	
#opening the files	
with open(sys.argv[1], 'r') as infile:

    data = infile.read()  # Read the contents of the file into memory.


my_list = data.splitlines()

#prints each line in a array
#print(my_list)
for eachLine in my_list:     # First Example
   readEachLine(eachLine)





