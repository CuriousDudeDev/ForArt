print('This is same number pyramid ForArt')
columns = int(input('Enter the number of columns: '))
spaces = columns - 1
for i in range(columns):
	if i == 0:
		print(spaces*' '+str(i+1))
		spaces -= 1
	else:
		char = ''
		for j in range(0 , i+1):
			char+= str(i+1)+' '
		print(spaces*' '+char)
		spaces -= 1
