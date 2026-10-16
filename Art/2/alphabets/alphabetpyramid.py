print('This is alphabet pyramid ForArt')
columns = int(input('Enter the number of columns: '))
spaces = columns - 1
for i in range(columns):
	if i == 0:
		mid = 65
		midchar = chr(mid)
		print(spaces*' '+midchar)
		spaces -= 1
		mid += 1
	else:
		char = ''
		for i in range(65 , mid+1):
			char += chr(i)
		for j in range(mid-1 , 64 , -1):
			char += chr(j)
		print(spaces*' '+char)
		mid += 1
		spaces -= 1