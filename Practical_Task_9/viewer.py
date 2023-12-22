from catalogs import*
from converter import*
from delete import*
from main import*
import os

def show():
    '''Функция позволяет взаимодействовать со всеми функциями пакета'''
    while True:
        path = os.getcwd()
        print(f"Текущий каталог: {current_catalog()}\n\n")
        print(f"Выберите действие:\n\n"
              f"0. Сменить рабочий каталог\n1. Преобразовать PDF в Docx\n"
              f"2. Преобразовать Docx в PDF\n3. Произвести сжатие изображений\n"
              f"4. Удалить группу файлов\n5. Выход\n\n")

        pick=input("Ваш выбор: ")
        if pick == "0":
            pick_zero()
        elif pick == "1":
            pick_one(path)
            print()
        elif pick == "2":
            pick_two(path)
        elif pick == "3":
            pick_three(path)
        elif pick == "4":
            pick_four(path)
        elif pick == "5":
            break
        else:
            print("Введено неправильное значение!")

if __name__ == "__main__":
    show()






