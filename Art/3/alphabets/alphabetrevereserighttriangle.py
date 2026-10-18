print('This is alphabets reverse right triangle ForArt')
columns = int(input('Enter the number of columns: '))
list = []
value = 64
for i in range(1 , columns+1):
    list.insert(0 , chr(value+i))
    for char in list:
        print(char , end= ' ')
    print()
