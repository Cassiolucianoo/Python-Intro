import os

root = os.path.join('..', 'food')
for directory, subdir_list, file_list in os.walk(root):
    print('Diretorio :', directory)
    for name in subdir_list:
        print('subdiretório :', name)
    for name in file_list:
        print(' Arquivo :', name)
    print()