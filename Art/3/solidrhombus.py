print('This is solid rhombus ForArt')
side = int(input('Enter the value of side: '))
spaces = side - 1
for i in range(side):
    print(spaces*' '+side*'*')
    spaces -= 1
