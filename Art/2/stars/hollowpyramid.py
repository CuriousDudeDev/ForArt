print('This is hollow pyramid ForArt')
base = int(input('Enter the value of Base: '))
spaces = base//2
rows = spaces + 1
inspaces = 1
print(spaces*' '+'*'+spaces*' ')
spaces -= 1
for i in range(rows - 2):
	print(spaces*' '+'*'+inspaces*' '+'*')
	spaces -= 1
	inspaces += 2
if base% 2 == 0:
	base+= 1
	print(base*'*')
else:
	print(base*'*')