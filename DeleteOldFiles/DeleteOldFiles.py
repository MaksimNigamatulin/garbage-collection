# coding: utf-8-sig
# -----------------------------------#
#       Maksim Nigamatulin           #
#           19/09/2020               #
#  Скрипт для удаления из указанной  #
#  папки файлов старше определеного  #
#  количества дней.                  #
# -----------------------------------#

# импортируем необходимые модули
import os
import time

# указываем путь к папке с файлами. можно расширить список на несколько путей.
my_path = [input(r'Укажите путь каталога для очистки: '), ]

# указываем возраст файлов и каталогов в днях
days = int(input('Укажите возраст файлов и папок в днях: '))

# текущую дату переводим в секунды
seconds = time.time() - (days * 24 * 60 * 60)

# добавляем параметры статистики
common_del_size = 0
common_del_file = 0
common_del_dir = 0

# функция для поиска и удаления файлов
def del_old_files(folder):
    global common_del_size
    global common_del_file
    # проверяем, что указанный путь существует
    if os.path.exists(folder):
        # получаем генератор с файлами и папками в рабочем каталоге
        for root, dirs, files in os.walk(folder):
            # получаем перечень файлов в рабочем каталоге
            for file in files:
                # получаем путь к каждому файлу в рабочем каталоге
                file_path = os.path.join(root, file)
                # получаем время изменения каждого файла и сравниваем с текущим временем
                if seconds > os.path.getmtime(file_path):
                    # получаем размер удаляемого файла, конвертируем в мегабайты
                    common_del_size += os.path.getsize(file_path)/1024/1024
                    # начинаем подсчет удаленных файлов
                    common_del_file += 1
                    # если файл был изменен раньше текущего времени, файл удаляется
                    os.remove(file_path)
                    print(f'Файл {file} удален')
    else:
        print('Файл или каталог по указанному пути не найден')

# функция для удаления каталогов
def del_old_folders(folder):
    global common_del_dir
    # определяем переменную для повторного обхода каталогов
    run_func = 0
    for root, dirs, files in os.walk(folder):
        # определяем наличие файлов и вложенных каталогов
        if not dirs and not files:
            # начинаем подсчет удаленных каталогов
            common_del_dir += 1
            # начинаем подсчитывать сколько каталогов обошел код на данной итерации
            run_func+=1
            # пустые каталоги удаляются
            os.rmdir(root)
            print(f'Каталог {root} удален')
            # если каталогов для обхода не осталось - завершить выполнение функции
            if run_func > 1:    # если нужно удалить и корневой каталог, тогда run_func > 0
                del_old_folders(folder)

# основной цикл скрипта
for folder in my_path:
    del_old_files(folder)
    del_old_folders(folder)

# вывод статистики
print('\n==========Результат очистки каталога==========')
print(f'Очищено памяти: {int(common_del_size)} MB')
print(f'Удалено файлов: {common_del_file}')
print(f'Удалено каталогов: {common_del_dir}')
print('==============================================')

input()