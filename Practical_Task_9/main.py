from catalogs import*
from converter import*
from delete import*


def pick_zero():
    '''Выбор пользователем нулевого пункта'''
    change_catalog()

def pick_one(path):
    '''Выбор пользователем первого пункта'''
    pdf=all_pdf()
    for i in range(len(pdf)):
        print(f"{i + 1}. {pdf[i]}")
        print()
    choise = input("Введите номер файла для преобразования (чтобы преобразовать все файлы из каталога, введите 0):").strip()
    if choise == '0':
        all_pdf_to_docx(path)
    else:
        pdf_to_docx(pdf[int(choise) - 1])
        print(f'Преобразование файла {pdf[int(choise) - 1]} из PDF в Docx прошло успешно!')

def pick_two(path):
    '''Выбор пользователем второго пункта'''
    docx=all_docx()
    for i in range(len(docx)):
        print(f"{i + 1}. {docx[i]}")
        print()
    choise=input("Введите номер файла для преобразования (чтобы преобразовать все файлы из каталога, введите 0):").strip()
    if choise == '0':
        all_docx_to_pdf(path)
    else:
        docx_to_pdf(docx[int(choise) - 1])
        print(f'Преобразование файла из PDF в Docx прошло успешно!')

def pick_three(path):
    '''Выбор пользователем третьего пункта'''
    img=all_img()
    for i in range(len(img)):
        print(f"{i + 1}. {img[i]}")
        print()
    choise=input("Введите номер файла для преобразования (чтобы преобразовать все файлы из каталога, введите 0):").strip()
    if choise == '0':
        compres_all(path)
    else:
        compress(img[int(choise) - 1])
        print(f'Изображение {img[int(choise) - 1]} успешно сжато!')

def pick_four(path):
    '''Выбор пользователем четвертого пункта'''
    delete(path)



