import os

my_desktop='c:/Users/eduardo/Desktop'

for item in os.listdir(my_desktop):
    if os.path.isfile(f'{my_desktop}/{item}'):
        print(f'{item} is a file')
    elif os.path.isdir(f'{my_desktop}/{item}'):
        print(f'{item} is a dir')
