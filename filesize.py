import os

target_dir = input('Введите директорию файла в формате D:\\dir\\file.exe: ')
size = os.path.getsize(target_dir)

size_in_kb = size/1024
size_in_mb = size_in_kb/1024
size_in_gb = size_in_mb/1024

print('\nРазмер файла в байтах:     ', size,'Б')
print('\nРазмер файла в килобайтах: ', size_in_kb,'КБ','\n')
print('Размер файла в мегабайтах: ', size_in_mb,'МБ','\n')
print('Размер файла в гигабайтах: ', size_in_gb,'ГБ','\n')


