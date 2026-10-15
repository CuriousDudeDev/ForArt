print("This is Floyd's Triangle ForArt")
columns = int(input('Enter the number of columns: '))
number = 1
for i in range(1 , columns+1):
	for j in range(i):
		print(number , end=' ')
		number += 1
	print()
