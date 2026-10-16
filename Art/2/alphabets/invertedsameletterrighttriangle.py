print('This is inverted same letter right triangle ')
columns = int(input('Enter the number of columns: '))
value = 64+columns
for i in range(columns , 0 , -1):
    print(chr(value)*i)
    value -= 1
