print('This is left triangle of stars ForArt')
base = int(input('Enter the base of the triangle: '))
spaces = base - 1
stars= 1
for i in range(base):
	print(spaces*' ' + stars*'*')
	stars += 1
	spaces -= 1