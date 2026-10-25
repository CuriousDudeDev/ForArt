print('This is inverted pyramid of stars ForArt')
base = int(input('Enter the base of the triangle: '))
stars = base
spaces = (base - stars)//2
rows = (base + 1)//2
for i in range(rows):
	print(spaces*' '+ stars*'*' + spaces*' ')
	stars -= 2
	spaces += 1
