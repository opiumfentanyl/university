import os
from pdf2docx import *
from docx2pdf import *
from PIL import Image



def current_catalog():
    '''Функция показывает текущий каталог'''
    return os.getcwd()

def change_catalog(swap):
    '''Функция проверяет существование каталога, и меняет его на нужный пользователю'''
    if os.path.isdir(swap):
        os.chdir(swap)
        print(f"Текущий каталог: {current_catalog()}")

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



def pdf_to_docx(file:str):
    '''Функция онвертирует path (путь к файлу) из формата pdf в docx'''

    file_pdf = file
    file_docx=str(file_pdf)+'.docx'
    conv = Converter(file_pdf)
    conv.convert(file_docx)
    conv.close()

def all_pdf_to_docx(path:all_pdf()):
    '''Функция конвертирует в path (путь к файлу) все файлы фаормата pdf в docx'''
    for files_pdf in path:
        pdf_to_docx(files_pdf)

def docx_to_pdf(file_docx:str):
    '''Функция онвертирует path (путь к файлу) из формата docx в pdf'''
    convert(file_docx, file_docx.replace(".docx","") + ".pdf")


def all_docx_to_pdf():
    path = list(os.getcwd())
    '''Функция конвертирует в path (путь к файлу) все файлы фаормата docx в pdf'''
    for files_docx in path:
        pdf_to_docx(files_docx)

def compress(file_img,qlty):
    '''Функция сжимает изображение из файла path на указанное число процентов'''
    image_file = Image.open(file_img)
    image_file.save(file_img, quality=qlty)

def compres_all(path):
    '''Функция сжимает все изображения из файла path на указанное число процентов'''
    for files_img in path:
        compress(files_img)



def delete_start():
    path = os.getcwd()
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

def delete_end():
    path = os.getcwd()
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


def delete_inside():
    path = os.getcwd()
    Str = str(input("Введите номер подстроки: "))
    files = []
    for file in os.listdir(path):
        if Str in file.rsplit(".", 1)[0]:
            files.append(file)
    if len(files) == 0:
        print("Нет файлов для удаления!")
    else:
        for file in files:
            os.remove(file)
            print("Файлы успешно удалены!")

def delete_extension():
    path = os.getcwd()
    Str = str(input("Введите ресширение: "))
    files = []
    for file in os.listdir(path):
        if Str in file.rsplit(".", 1)[1]:
            files.append(file)
    if len(files) == 0:
        print("Нет файлов для удаления!")
    else:
        for file in files:
            os.remove(file)
            print("Файлы успешно удалены!")

def just_delete(file):
    current_repository = os.getcwd()

