from abrakadabra import*

def show():
    strings = (inf('info.csv'))
    word = input('Введите стоку, по которой хотите отсортировать книги: ')
    result_string = get_books(word, strings)
    check=get_totals(result_string)
    if len(check) > 0 :
        print(check)
    else:
        print('Книг не найдено.')

if __name__ =='__main__':
    show()