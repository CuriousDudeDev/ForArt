print('This is hollow right triangle ForArt')
base = int(input('Enter the value of Base: '))
if base == 0:
	print()
else:
	space = 0
	print('*')
	for i in range(2 , base):
		print('*' + space * ' ' + '*')
		space += 1
	print('*' * base)
