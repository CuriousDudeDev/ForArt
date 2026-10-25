import string
print('This is inverted right triangle ForArt')
columns = int(input('Enter the number of columns: '))
for i in range(columns , 0 , -1):
	print(string.ascii_uppercase[:i])