import sys
print('This is diamond with numbers ForArt')
columns = int(input('Enter the number of columns: '))
if columns >= 1:
    spaces = columns - 1
    print(spaces*' '+'1')
    spaces -= 1
    inspaces = 1
if columns < 1:
    sys.exit()
for i in range(2 , columns+1):
    print(spaces*' '+str(i)+inspaces*' '+str(i))
    spaces -= 1
    inspaces += 2
spaces += 2
inspaces -= 4
for i in range(columns-1 , 1 , -1):
    print(spaces*' '+str(i)+inspaces*' '+str(i))
    spaces += 1
    inspaces -= 2
print(spaces*' '+'1')

