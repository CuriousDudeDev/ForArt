print('This is inverted hollow pyramid ForArt')
rows = int(input('Enter the value of base: '))
for i in range(rows):
	if i == rows -1:
		print((rows-1)*' '+'*')
	elif i == 0:
		print(((rows*2)-1)*'*')
	else:
		spaces = i
		inspaces = ((rows*2)-1) - 2*spaces - 2
		print(spaces*' '+'*'+inspaces*' '+'*')