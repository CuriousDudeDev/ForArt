print('This is alphabets floyd triangle ForArt')
columns = int(input('Enter the number of columns: '))
value = 64
for i in range(1 , columns+1):
    char = ''
    for j in range(i , 2*i):
        char += chr(value+j)+' '
    print(char)
    
