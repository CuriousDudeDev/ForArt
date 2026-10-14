print('This is pyramid of stars ForArt')
base = int(input('Enter the base of the pyramid: '))

if base % 2 == 0:
    stars = 2
else:
    stars = 1
times = (base + 1) // 2
spaces = (base - stars) // 2
for i in range(times):
    print(spaces * ' ' + stars * '*' + spaces * ' ')
    spaces -= 1
    stars += 2