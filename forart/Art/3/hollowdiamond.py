print('This is hollow Diamond ForArt')
columns = int(input('Enter the number of columns above the middle line: '))
if columns == 1:
    print('*')
elif columns > 1:

    spaces = columns -1
    inspaces = 1
    print(spaces*' '+ '*')
    spaces -= 1
    for i in range(columns-1):
        print(spaces*' '+'*'+inspaces*' '+'*')
        spaces -= 1
        inspaces += 2

    inspaces = (columns*2)-5
    spaces = 1
    for i in range(columns-2):
        print(spaces*' '+'*'+inspaces*' '+'*')
        spaces += 1
        inspaces -= 2
    print(spaces*' '+ '*')
