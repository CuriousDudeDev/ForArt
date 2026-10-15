import string
print('This is CAPITAL Alphabet Right Triangle ForArt')
columns = int(input('Enter the number of columns: '))
for i in range(1 , columns+1):
	print(string.ascii_uppercase[:i])