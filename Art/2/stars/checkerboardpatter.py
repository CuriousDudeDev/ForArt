print('This is checkerboard pattern ForArt')
columns = int(input('Enter the number of columns: '))
start = 0
for i in range(1 , columns+1):
    if start%2 == 1:
        print(' ' , end = ' ')
    for j in range(columns):
        print('*' , end=' ')
    print()
    start += 1
        
    
