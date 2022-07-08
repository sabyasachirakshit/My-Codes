"""
? A program to prettify the folders on a specified path!
"""
import os
ip = 'Invalid Path'


def prettify_filename(path_file):
    if os.path.exists(path_file) is True:
        os.chdir(Path)
        for i in os.listdir():
            os.rename(i, i.title())
        print('Folder Prettified:', os.listdir())
    else:
        print(ip)


def prettify_filecontents(path_file):
    if os.path.exists(path_file) is True:
        os.chdir(Path)
        name_of_the_file = input(
            'Enter Text File Name without .txt extension:')
        f = open(f'{name_of_the_file}.txt', 'r')
        x = []
        for line in f:
            words = line.split(' ')
            for word in words:
                if(word == 'this' or word == 'that'):
                    continue
                else:
                    word = word.title()
                x.append(word)
        f.close()
        f = open(f'{name_of_the_file}.txt', 'w')
        t = ' '.join(x)
        f.write(t)
        f.close()
        print('File Prettified')
    else:
        print(ip)


def prettify_filejpg(path_file):
    if os.path.exists(path_file) is True:
        os.chdir(Path)
        i = 1
        for file in os.listdir(path_file):
            if file.endswith('.jpg') is True:
                src = file
                new_src = f"{i}"+".jpeg"
                os.rename(src, new_src)
                i += 1
        print('.jpg Files Prettified')
    else:
        print(ip)


print('Soldier: Enter Path Of Your Folder You Want To Prettify')
Path = input('Typer Here:')
print('\n1.Prettify File Name')
print('2.Prettify File Contents')
print('3.Prettify .jpg files')
ch = int(input('Enter choice-'))
if(ch == 1):
    prettify_filename(Path)
elif(ch == 2):
    prettify_filecontents(Path)
elif(ch == 3):
    prettify_filejpg(Path)
else:
    print('Wrong Choice')
print('\nHit Enter to End.......')
input()
