import sys
from pathlib import Path


def _get_art_dir():
    if getattr(sys, 'frozen', False):
        return Path(sys._MEIPASS) / 'forart' / 'Art'
    from importlib.resources import files
    return Path(str(files('forart').joinpath('Art')))


artfiles = sorted(_get_art_dir().rglob("*.py"))



def main():
    while True:
        print('---This is ForArt CLI---')
        print('Instructions')
        print('Select the appropriate button from below to get the patern. ')
        print('\n\n')
        print("0. Exit\n")
        num = 1
        art_root = _get_art_dir()
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
                exec(file.read_text())
                print('\nDone!!\n')

        else:
            print('Invalid input!!!')
    
if __name__ == "__main__": 
    main()
