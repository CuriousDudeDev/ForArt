print('This is hollow pyramid ForArt')
rows = int(input('Enter the value of rows: '))
for i in range(rows):
	if i == 0:
		print((rows-1)*' '+'*')
	elif i == rows -1:
		print(((rows*2)-1)*'*')
	else:
		spaces = rows-i-1
		inspaces = ((rows*2)-1) - 2*spaces - 2
		print(spaces*' '+'*'+inspaces*' '+'*')

