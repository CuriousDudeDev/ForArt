print('This is inverted hollow right triangle ForArt')
base = int(input('Enter tangehe value of Base: '))
print(base*'*')
spaces = base - 3
for i in range(base-2):
	print('*' + spaces * ' ' + '*')
	spaces -= 1
print('*')