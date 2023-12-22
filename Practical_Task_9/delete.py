import os

def delete(path:str):
    '''Функция удаляет указанные пользователем файлы в файле path'''
    print(f"Выберите действие:\n\n1. Удалить все файлы начинающиеся на определенную подстроку\n"
          f"2. Удалить все файлы заканчивающиеся на определенную подстроку\n"
          f"3. Удалить все файлы содержащие определенную подстроку\n"
          f"4. Удалить все файлы по расширению\n")
    pick = input("Введите номер действия: ")
    if pick == "1":
        Str = str(input("Введите номер подстроки: "))
        files = []
        for file in os.listdir(path):
            if file.startswith(Str):
                files.append(file)
        if len(files) == 0:
            print("Нет файлов для удаления!")
        else:
            for file in files:
                os.remove(file)
                print("Файлы успешно удалёны!")
                files.clear()

    elif pick == "2":
        Str = str(input("Введите номер подстроки: "))
        files = []
        for file in os.listdir(path):
            if file.rsplit(".",1)[0].endswith(Str):
                files.append(file)
        if len(files) == 0:
            print("Нет файлов для удаления!")
        else:
            for file in files:
                os.remove(file)
                print("Файлы успешно удалены!")
                files.clear()

    elif pick == "3":
        Str = str(input("Введите номер подстроки: "))
        files=[]
        for file in os.listdir(path):
            if Str in file.rsplit(".",1)[0]:
                files.append(file)
        if len(files)==0:
            print("Нет файлов для удаления!")
        else:
            for file in files:
                os.remove(file)
                print("Файлы успешно удалены!")
                files.clear()

    elif pick == "4":
        Str= str(input("Введите ресширение: "))
        files=[]
        for file in os.listdir(path):
            if Str in file.rsplit(".",1)[1]:
                files.append(file)
        if len(files)==0:
            print("Нет файлов для удаления!")
        else:
            for file in files:
                os.remove(file)
                print("Файлы успешно удалены!")
                files.clear()