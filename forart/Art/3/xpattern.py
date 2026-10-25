print('This is X pattern ForArt')
columns = int(input('Enter the total number of columns: '))
inspaces = columns - 2
spaces = 0
for i in range((columns - 1)//2):
    print(spaces*' '+'*'+inspaces*' '+'*')
    spaces += 1
    inspaces -= 2
if columns%2 == 0 and columns > 0:
    print(spaces*' '+'**')
    print(spaces*' '+'**')
elif columns == 0:
    print()
else:
    print(spaces*' '+'*')
inspaces += 2
spaces -= 1
for i in range((columns - 1)//2):
    print(spaces*' '+'*'+inspaces*' '+'*')
    spaces -= 1
    inspaces += 2
