print('This is inverted number pyramid ForArt')
base = int(input('Enter the maximum numebr in base: '))
spaces = 0
for i in range(base-1 , -1 , -1):
	if i == 0:
		print(spaces*' '+str(i+1))
		spaces += 1
	else:
		char = ''
		for j in range(1 , i+2):
			char+= str(j)+' '
		print(spaces*' '+char)
		spaces += 1