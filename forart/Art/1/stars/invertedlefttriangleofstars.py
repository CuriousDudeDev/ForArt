print('This is inverted left triangle of stars ForArt')
base = int(input('Enter the base of the triangle: '))
stars = base
spaces = 0
for i in range(base):
	print(spaces*' ' + stars*'*')
	spaces += 1
	stars -= 1

