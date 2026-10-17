print('This is hollow pyramid ForArt')
side = int(input('Enter the value of side: '))
spaces = side -1
inspaces = side - 2
print(spaces*' '+side*'*')
spaces -= 1
for i in range(side-2):
    print(spaces*' '+'*'+inspaces*' '+'*')
    spaces -= 1
print(side*'*')
