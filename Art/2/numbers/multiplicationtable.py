print('This is multiplication table ForArt')
rows = int(input('Enter the number of rows: '))
list =[]
for i in range(1 , rows+1):
    list.append(i)
for j in list:
    print(j , end = ' ')
print()
for k in range(2 , rows+1):
    char = ''
    for m in list:
        char += str(m*k)+' '
    print(char)
        
