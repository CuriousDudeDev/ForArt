print('This is number pyramid ForArt')
base = int(input('Enter the maximum number in base: '))
spaces = base -1
for i in range(base):
	if i == 0:
		print(spaces*' '+str(i+1))
		spaces -= 1
	else:
		char = ''
		for j in range(1 , i+2):
			char+= str(j)+' '
		print(spaces*' '+char)
		spaces -= 1

