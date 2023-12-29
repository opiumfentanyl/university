import PySimpleGUI as sg
from task9allnodules import*

def window():
    sg.theme("LightBlue2")
    layout=[
        [sg.Text(f'Текущая дериктория: {current_catalog()}', key="TEXT_DIRECTORY")],
        [sg.Button('Сменить рабочий каталог', key="switchDirectory")],
        [sg.Button('Преобразовать PDF в Docx', key="pdfToDocx", disabled=True)],
        [sg.Button('Преобразовать Docx в PDF', key="docxToPdf", disabled=True)],
        [sg.Button('Произвести сжатие изображения', key="compressor", disabled=True)],
        [sg.Button('Удалить группу файлов', key="deletes", disabled=True)],
        [sg.Button('Выход')]
    ]
    window = sg.Window("Office Tweaks", layout, finalize=True)
    while True:
        window, event, values = sg.read_all_windows()

        if event == sg.WINDOW_CLOSED or event == 'Выход':
            break

        if event == "switchDirectory":
            direct = sg.popup_get_folder('Выберите папку', title='Диалог выбора папки', default_path=current_catalog())
            change_catalog(direct)
            window["TEXT_DIRECTORY"].update(f'Текущая дериктория: {current_catalog()}')
            current_catalog()


        if event == "pdfToDocx":
            pdf_files = all_pdf()
            layout_conversion = [
                [sg.Text("Выберите файлы для конвертации:")],
                *[[sg.Checkbox(file, key=file)] for file in pdf_files],
                [sg.Button("Конвертировать файл", key=convert), sg.Button("Отмена")]
            ]
            window_conversion = sg.Window("Файлы для конвертации", layout_conversion)

            while True:
                event_conversion, values_conversion = window_conversion.read()
                if event_conversion in (sg.WIN_CLOSED, "Отмена"):
                    break

                elif event_conversion == "convert":
                    selected_files = [file for file in pdf_files if values_conversion[file]]
                    for i in selected_files:
                        pdf_to_docx()
            window_conversion.close()


        if event == "docxToPdf":
            docx_files = all_docx()
            layout_conversion = [
                [sg.Text("Выберите файлы для конвертации:")],
                *[[sg.Checkbox(file, key=file)] for file in docx_files],
                [sg.Button("Конвертировать файл", key=convert), sg.Button("Отмена")]
            ]
            window_conversion = sg.Window("Файлы для конвертации", layout_conversion)

            while True:
                event_conversion, values_conversion = window_conversion.read()
                if event_conversion in (sg.WIN_CLOSED, "Отмена"):
                    break

                elif event_conversion == "convert":
                    selected_files = [file for file in docx_files if values_conversion[file]]
                    for i in selected_files:
                        docx_to_pdf(i)
            window_conversion.close()


        if event == "compressor":
            img_files = all_img()
            layout_conversion = [
                [sg.Text("Выберите изображения для конвертации:")],
                *[[sg.Checkbox(file, key=file)] for file in img_files],
                [sg.Text("Процент сжатия:"), sg.Slider(range=(1, 100), key="compression_slider")],
                [sg.Button("Сжать"), sg.Button("Отмена")]
            ]
            window_conversion = sg.Window("Файлы для конвертации", layout_conversion)

            while True:
                event_conversion, values_conversion = window_conversion.read()
                if event_conversion in (sg.WIN_CLOSED, "Отмена"):
                    break

                elif event_conversion == "Сжать изображения":
                    selected_files = [file for file in img_files if values_conversion[file]]
                    qlty = int(values_conversion["compression_slider"])
                    for i in selected_files:
                        compress(i, qlty)
            window_conversion.close()


        if event == 'deletes':
            layout_del = [
                [sg.Text("Выберите критерий удаления:")],
                [sg.Radio('Удалить все файлы начинающиеся на определенную подстроку',key='f1')],
                [sg.Radio('Удалить все файлы заканчивающиеся на определенную подстроку',key='f2')],
                [sg.Radio('Удалить все файлы содержащие определенную подстроку', key='f3')],
                [sg.Radio('Удалить все файлы по расширению', key='f4')],
                [sg.Text("Введите подстроку:"), sg.InputText(key='substring')],
                [sg.Button('Выбор'), sg.Button('Отмена')]
            ]
            window_del = sg.Window("Методы удаления", layout_del)
            pick = None
            substr = None
            while True:
                event_del, values_del = window_del.read()
                if event_del in (sg.WIN_CLOSED, "Отмена"):
                    break
                elif event_del == "Выбор":
                    pick = int([k for k, v in values_del.items() if v][0][-1])
                    substr = values_del['substr']
                    if not substr:
                        sg.popup_error("Неверный ввод, ведите подстроку.")
                        continue
                    window_del.close()

                    if pick == 1:
                        files = []
                        for file in os.listdir(os.getcwd):
                            if file.startswith(substr):
                                files.append(file)
                    elif pick == 2:
                        files = []
                        for file in os.listdir(os.getcwd):
                            if file.rsplit(".", 1)[0].endswith(substr):
                                files.append(file)
                    elif pick == 3:
                        files = []
                        for file in os.listdir(os.getcwd):
                            if substr in file.rsplit(".", 1)[0]:
                                files.append(file)
                    elif pick == 4:
                        files = []
                        for file in os.listdir(os.getcwd):
                            if substr in file.rsplit(".", 1)[1]:
                                files.append(file)
                    layout_p=[
                        [sg.Text("Выберите файлы для удаления:")],
                        *[[sg.Checkbox(file, key=file)] for file in files],
                        [sg.Button('Удалить'), sg.Button('Отмена')]
                    ]
                    window_files = sg.Window('Выбор файлов для удаления', layout_p)
                    while True:
                        event_files, values_files = window_files.read()
                        if event_files in (sg.WINDOW_CLOSED, 'Отмена'):
                            break
                        elif event_files == 'Удалить':
                            selected_files = [file for file in files if values_files[file]]
                            for i in selected_files:
                                os.remove(i)
                            window_files.close()
            window_del.close()

if __name__ == "__main__":
    window()







