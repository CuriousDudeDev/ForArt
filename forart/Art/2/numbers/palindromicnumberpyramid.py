print('This is palindromic number pyramid ForArt')
num = int(input('Enter the maximum number in the pyramid: '))
spaces = num - 1
for i in range(num):
	if i == 0:
		mid = 1
		print(spaces*' '+str(i+1))
		spaces -= 1
		mid += 1
	else:
		char = ''
		for j in range(1 , mid + 1):
			char += str(j)
		for k in range(mid-1 , 0, -1):
			char += str(k)
		print(spaces*' '+char)
		mid += 1
		spaces -= 1

			