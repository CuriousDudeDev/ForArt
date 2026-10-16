print('This is inverted palindromic pyramid ForArt')
num = int(input('Enter the maximum number in the pyramid: '))
spaces = 0
mid = num
for i in range(num-1 , -1 , -1):
	if i == 0:
		print(spaces*' '+str(i+1))
		spaces += 1
	else:
		char = ''
		for j in range(1 , mid+1):
			char += str(j)
		for k in range(mid-1 , 0 , -1):
			char += str(k)
		print(spaces*' '+char)
		mid -= 1
		spaces += 1


