print('This is plus pattern ForArt')
num = int(input('Enter the number of stars in the middle line or the vertical line: '))
spaces = num // 2
for i in range((num - 1)//2):
    print(spaces*' '+'*')
print(num*'*')
for i in range((num - 1)//2):
    print(spaces*' '+'*')
