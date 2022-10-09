#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import json
import shutil


class Main():
    def __init__(self):
        with open(r'C:\Users\nikal\settings.json', 'r') as file_dir:
            self.settings = json.load(file_dir)
            
    def command_list(self):
        print('Список команд:        \n1) Просмотреть содержимое папки        \n2) Создать папку        \n3) Удалить папку        \n4) Зайти в папку        \n5) Перейти на уровень вверх        \n6) Создать новый файл        \n7) Записать текст в файл        \n8) Просмотреть содержимое файла        \n9) Удалить файл        \n10) Копировать файл        \n11) Переместить файл        \n12) Переименовать файл')

    def folder_content(self): #1
        print('Содержимое папки:'+'\n'+'\n'.join(os.listdir()))
        
    def create_folder(self): #2
        try:
            name = input('Введите имя папки, которую хотите создать: ')
            os.mkdir(name)
            print('Папка создана')
        except:
            print('Ошибка')

    def delite_folder(self): #3
        try:
            name = input('Введите имя папки, которую хотите удалить: ')
            os.rmdir(name)
            print('Папка удалена')
        except:
            print('Ошибка')
            
    def get_down(self): #4
        try:
            name = input('Введите имя папки, в которую вы хотите перейти: ')
            os.chdir(name)
            print(f'Вы находитесь в папке {name}')
        except:
            print('Ошибка')
            
    def return_to(self): #5
        try:
            assert len(os.getcwd()) > len(self.settings["directory"])
            os.chdir(os.pardir)
            print(f'Вы вернулись в папку {os.path.split(os.getcwd())[-1]}')
        except:
            print('Ошибка') 
            
    def create_file(self): #6
        try:
            name = input('Введите имя файла, который хотите создать: ')+'.txt'
            with open(f'{name}', 'w') as file:
                print('Файл создан')
        except:
            print('Ошибка')
            
    def write_text(self): #7
        try:
            name = input('Введите имя файла, в который хотите записать текст: ')+'.txt'
            text = input('Введите текст: ')
            with open(name, 'a') as file:
                file.write(text)
            print('Текст записан')
        except:
            print('Ошибка')   
            
    def open_file(self): #8
        try:
            name = input('Введите имя файла, который хотите прочитать: ')+'.txt'
            with open(name, 'r') as file:
                for line in file:
                    print(line)
        except:
            print('Ошибка')

    def delite_file(self): #9
        try:
            name = input('Введите имя файла (с расширением), который хотите удалить: ')
            os.remove(name)
            print('Файл удален')
        except:
            print('Ошибка')
            
    def copy_file(self): #10
        try:
            name = input('Введите имя файла (c расширением), который хотите скопировать: ')
            path_from = input('Введите путь папки, из которой хотите скопировать файл: ')
            path_to = input('Введите путь папки, в которую хотите скопировать файл: ')
            shutil.copyfile(f'{self.settings["directory"]}\\{path_from}\\{name}', 
                            f'{self.settings["directory"]}\\{path_to}\\{name}')
            print('Файл скопирован')
        except:
            print('Ошибка')
            
    def move_file(self): #11
        try:
            name = input('Введите имя файла (c расширением), который хотите переместить: ')
            path_from = input('Введите путь папки, из которой хотите переместить файл: ')
            path_to = input('Введите путь папки, в которую хотите переместить файл: ')
            shutil.move(f'{self.settings["directory"]}\\{path_from}\\{name}', 
                        f'{self.settings["directory"]}\\{path_to}\\{name}')
            print('Файл перемещен')
        except:
            print('Ошибка')

    def rename(self): #12
        try:
            name = input('Введите имя файла (c расширением), который хотите переименовать: ')
            new = input('Введите новое имя файла: ')+'.'+name.split('.')[-1]
            os.rename(name, new)
            print('Файл переименован')
        except:
            print('Ошибка')
    
    def func_list(self, a):
        return {0: 'command_list', 1:'folder_content', 2:'create_folder', 3:'delite_folder', 4:'get_down', 5:'return_to', 
                6: 'create_file', 7: 'write_text', 8:'open_file', 9:'delite_file', 10:'copy_file', 11:'move_file', 12:'rename'}.get(a)
    
f_manager = Main()
os.chdir(f_manager.settings['directory'])
print('Введите 0, если хотите увидеть список команд')
while True:
    try:
        mes = int(input('\n'))
        if mes in [i for i in list(range(0,13))]:
            func = f_manager.func_list(mes)
            eval(f'f_manager.{func}()')
    except ValueError:
        print('Ошибка')

