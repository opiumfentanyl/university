from pdf2docx import *
from docx2pdf import *
from PIL import Image

def pdf_to_docx(path:str):
    '''Функция онвертирует path (путь к файлу) из формата pdf в docx'''
    file_pdf=path
    file_docx=str(file_pdf)+'.docx'
    conv = Converter(file_pdf)
    conv.convert(file_docx)
    conv.close()

def all_pdf_to_docx(path:list):
    '''Функция конвертирует в path (путь к файлу) все файлы фаормата pdf в docx'''
    for files_pdf in path:
        pdf_to_docx(files_pdf)

def docx_to_pdf(file_docx:str):
    '''Функция онвертирует path (путь к файлу) из формата docx в pdf'''
    convert(file_docx, file_docx.replace(".docx","") + ".pdf")


def all_docx_to_pdf(path:list):
    '''Функция конвертирует в path (путь к файлу) все файлы фаормата docx в pdf'''
    for files_docx in path:
        pdf_to_docx(files_docx)

def compress(file_img:str):
    '''Функция сжимает изображение из файла path на указанное число процентов'''
    image_file = Image.open(file_img)
    qlty=int(input("Введите параметры сжатия (от 0 до 100%): "))
    image_file.save(file_img, quality=qlty)

def compres_all(path):
    '''Функция сжимает все изображения из файла path на указанное число процентов'''
    for files_img in path:
        compress(files_img)


