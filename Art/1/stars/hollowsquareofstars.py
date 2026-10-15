print('This is hollow swuare of stars ForArt')
side = int(input('Enter the side of the star: '))
print(side*'*')
for i in range(side-2):
	print('*' + (side - 2)*' ' + '*')
print(side*'*')