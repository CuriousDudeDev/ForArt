print('This is inverted alphabet pyramid ForArt')
columns = int(input('Enter the number of columns: '))
spaces = 0 
mid = 64+columns
for i in range(columns-1 , -1 , -1):
	if i == 0:
		print(spaces*' '+str(chr(65)))
		spaces += 1
	else:
		char = ''
		for j in range(65 , mid+1):
			char += chr(j)
		for k in range(mid-1 , 64 , -1):
			char += chr(k)
		print(spaces*' '+char)
		mid -= 1
		spaces += 1
