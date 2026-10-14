print('This is inverted right triangle of stars ForArt')
base = int(input('Enter the base of the triangle: '))
line = base
for i in range(base):
	print(line* '*')
	line -= 1