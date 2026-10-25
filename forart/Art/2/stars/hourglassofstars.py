print('This is hourglass of stars FoRaRT')
n = int(input('Enter the value of n(rows above or rows below): '))
line = (2*n) -1
for i in range(n):
	print(' '*i+line*'*'+i*' ')
	line -= 2
line = 3

for  i in range(n-2 , -1 , -1):
	print(' '*i+line*'*'+i*' ')
	line += 2
