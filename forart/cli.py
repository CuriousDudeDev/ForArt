from importlib.resources import files

art_root = files("forart").joinpath("Art")
artfiles = sorted(art_root.rglob("*.py"))




def main():
    while True:
        print('---This is ForArt CLI---')
        print('Instructions')
        print('Select the appropriate button from below to get the patern. ')
        print('\n\n')
        print("0. Exit\n")
        num = 1
        prefix = str(art_root) + "/"
        for i in artfiles:
            print(f"{num}. {str(i)[len(prefix):]}")
            num += 1
        
        option = (input('Enter the number: '))
        if option.isdigit():
            option = int(option)
            if option == 0:
                print('Exitting........\n')
                break
            elif option > len(artfiles):
                print('Choose a proper option!!\n')
            else:
                file = artfiles[option - 1]
                print('Here is it -- ||\n')
                exec(open(file).read())
                print('\nDone!!\n')

        else:
            print('Invalid input!!!')
    
if __name__ == "__main__": 
    main()
