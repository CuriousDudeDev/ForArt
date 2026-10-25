print('This is row-start number triangle ForArt')
columns = int(input('Enter the number of columns: '))
for i in range(1 , columns + 1):
    char = ''
    for j in range(i , i*2):
        char += str(j)+' '
    print(char)
