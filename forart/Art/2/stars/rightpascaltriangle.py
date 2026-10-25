print('This is the right pascal triangle pascal art')
rows = int(input('Enter the number of rows till the middle row: '))
for i in range(1, rows+1):
	print(i * '*')
for i in range(rows-1 , 0 , -1):
	print(i *'*')
