
palidrome =input("enter word or string: ");
word = str(palidrome);


length = len(word)
i=length
final = []
while i > 0:
	i -= 1
	if word[i] != ' ':
	 final.append(word[i]); 
	
null = ''


reverse = null.join(final);	

print (reverse)


final.sort(reverse=True)

sortString = null.join(final);


print (sortString)