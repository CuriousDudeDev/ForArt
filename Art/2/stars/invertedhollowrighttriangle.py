print('This is inverted hollow triangle ForArt')
base = int(input('Enter the value of base: '))
rows = base
for i in range(rows):
	if i == 0:
		print(rows*'*')
	elif i==rows-1:
		print('*')
	else:
		print('*'+(rows-2-i)*' '+'*')