# Let's now see how we can read a file using python
from os.path import isfile

file_path = 'titanic/test.csv'
if isfile(file_path):
    my_file = open(file_path)
    for index, line in enumerate(my_file.readlines()):
        stripped_line = line.strip()
        print(f'The file line {index} has the content "{stripped_line}"')
else:
    print('Please provide a valid file!')
