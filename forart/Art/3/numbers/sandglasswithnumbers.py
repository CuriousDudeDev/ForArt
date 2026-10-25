print('This is sandglass with numbers ForArt')
num = int(input('Enter the maximum number in the art: '))
list = []
for i in range(1 , num+1):
    list.append(i)
spaces = 0
for j in range(num):
    print(spaces*' ' , end = '')
    for k in list:
        print(k , end = ' ')
    print()
    list.pop(0)
    spaces += 1
spaces -= 2
list.append(num)
for k in range(num-1 , 0 , -1):
    list.insert(0 , k)
    print(spaces*' ' , end = '')
    for k in list:
        print(k , end = ' ')
    print()
    spaces -= 1
    
    
