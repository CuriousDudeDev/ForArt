print('This is inverted right triangle of numbers ForArt')
columns = int(input('Enter the number of columns: '))
line = ''
for i in range(1 , columns+1):
	line += str(i)
for i in range(columns):
	print(line[:(columns-i)])

