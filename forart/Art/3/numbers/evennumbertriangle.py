print('This is even number triangle ForArt')
columns = int(input('Enter the number of columns: '))
value = 0 
for i in range(1 , columns + 1):
    char = ''
    for j in range(i , 2*i):
        char += str(value)+' '
        value += 2
    print(char)
