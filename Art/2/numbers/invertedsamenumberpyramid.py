print('This is inverted number pyramid ForArt')
columns = int(input('Enter the number of columns: '))
spaces = 0
for i in range(columns-1 , -1 , -1):
	if i == 0:
		print(spaces*' '+str(i+1))
		spaces += 1
	else:
		char = ''
		for j in range(1 , i+2):
			char+= str(i+1)+' '
		print(spaces*' '+char)
		spaces += 1