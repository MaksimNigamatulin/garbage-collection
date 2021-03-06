
# -----------------------------------#
#       Maksim Nigamatulin           #
#           29/09/2020               #
# Скрипт для распаковки zip-архивов  #
# в заданный каталог.                #
# -----------------------------------#

# импорт модулей
import os
import zipfile

# каталог, в котором будем искать архивы
zip_folder_path = input('Укажите путь к каталогу с файлами архива: ')
# запрос пути для хранения распакованных данных
unpacked_folder_path = input('Укажите путь к каталогу для распаковки архива: ')

def unzip(folder):
    os.chdir(folder)
    # проверка наличия каталога для хранения распакованных данных
    if not os.path.exists(unpacked_folder_path):
        # если каталог отсутствует - создать его
        os.mkdir(unpacked_folder_path)
    # поиск всех файлов в корневом каталоге
    for files in os.walk(folder):
        # выбор списка файлов
        for file in files:
            # обход всех файлов в списке
            for item in file:
                # выбор файлов по заданному расширению
                if item.lower().endswith('.zip'):
                    with zipfile.ZipFile(item, 'r') as zip_item:
                        zip_item.extractall(unpacked_folder_path)
                        print(f'Архив {item} успешно распакован.')

def rename_folders_and_files(folder):
    os.chdir(folder)
    for dir in os.listdir():
        if dir != dir.encode('cp437').decode('cp866'):
            if os.path.isfile(dir):
                decode_dirs = dir.encode('cp437').decode('cp866')
                os.rename(dir, decode_dirs)
            if os.path.isdir(dir):
                decode_dirs = dir.encode('cp437').decode('cp866')
                os.rename(dir, decode_dirs)
                rename_folders_and_files(folder + '\\' + decode_dirs)
                if not os.path.isdir(decode_dirs):
                    rename_folders_and_files(folder)

unzip(zip_folder_path)
rename_folders_and_files(unpacked_folder_path)