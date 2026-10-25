print('This is binary pyramid ForArt')
columns = int(input('Enter the number of columns: '))
value = 1
spaces = columns - 1
for i in range(1 , columns+1):
    char = ''
    for j in range(i):
        if value % 2 == 0:
            char += str(0) + ' ' 
            value += 1
        else:
            char += str(1)+' '
            value += 1
    print(spaces*' ' + char)
    spaces -= 1
   
