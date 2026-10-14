print('This is Diamond of Stars ForArt')
base = int(input('Enter the base of the triangle: '))
if base%2 == 0:
	stars = 2
else:
	stars = 1
spaces = (base - stars)//2
times = (base+1)//2
for i in range(times-1):
	print(spaces * ' ' + stars * '*' + spaces * ' ')
	spaces -= 1
	stars += 2

stars = base
spaces = (base - stars)//2
rows = (base + 1)//2
for i in range(rows):
	print(spaces*' '+ stars*'*' + spaces*' ')
	stars -= 2
	spaces += 1