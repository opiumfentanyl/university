import os
def current_catalog():
    '''Функция показывает текущий каталог'''
    return os.getcwd()

def change_catalog():
    '''Функция проверяет существование каталога, и меняет его на нужный пользователю'''
    swap=input('Укажите корректный путь к рабочему каталогу: ')
    if os.path.isdir(swap):
        os.chdir(swap)
        print(f"Текущий каталог: {current_catalog()}")
    else:
        print('Такого каталога нет!')
        change_catalog()

def all_pdf():
    '''Функция находит все файлы с расширением .pdf в директории'''
    print('Список файлов с расширением .pdf в данном каталоге:\n')
    list_pdf = [i for i in os.listdir(path='.') if i[-4:] == '.pdf']
    return list_pdf

def all_docx():
    '''Функция находит все файлы с расширением .docx в директории'''
    print('Список файлов с расширением .docx в данном каталоге:\n')
    list_docx = [i for i in os.listdir(path='.') if i[-5:] == '.docx']
    return list_docx

def all_img():
    '''Функция находит все изображения в директории'''
    print('Список изображений в данном каталоге:\n')
    list_img = [i for i in os.listdir(path='.') if i[-5:] == '.jpeg' or i[-4:] == '.jpg' or i[-4:] == '.gif' or i[-4:] == '.png']
    return list_img

