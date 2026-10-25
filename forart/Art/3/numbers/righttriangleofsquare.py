print('This is right triangle of square ForArt')
columns = int(input('Enter the number of columns: '))
list = []
for i in range(1 , columns+1):
    list.append(i)
    for j in list:
        print(str(j*j) , end=' ')
    print()
        
        
