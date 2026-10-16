print('This is hollowrightriangle ForArt')
base = int(input('Enter the value of the base: '))
rows = base
for i in range(rows):
	if i == 0:
		print('*')
	elif i==rows-1:
		print(rows*'*')
	else:
		print('*'+(i-1)*' '+'*')

