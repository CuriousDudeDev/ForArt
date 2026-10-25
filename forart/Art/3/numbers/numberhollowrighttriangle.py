print('This is number hollow right triangle ForArt')
columns = int(input('Enter the number of columns: '))
spaces = 1
if columns >= 1:
    print(1)
    spaces = 1
for i in range(columns - 2):
    print(str(1)+spaces*' '+str(i+2))
    spaces += 2
char = ''
for j in range(1, columns + 1):
    char += str(j)+' '
print(char)
    
