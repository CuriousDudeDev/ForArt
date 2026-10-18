print('This is butterfly pattern ForArt')
columns = int(input('Enter the number of rows above the middle lines: '))
spaces = (columns*2) - 2
for i in range(1 ,columns+1 ):
    print('*'*i + spaces*' '+'*'*i)
    spaces -= 2
if columns%2 == 0:
    print(columns*2*'*')
spaces = 2
for i in range(columns-1 , 0 , -1):
    print('*'*i + spaces*' '+'*'*i)
    spaces += 2
