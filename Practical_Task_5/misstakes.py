def misstakes():
    try:
        file=input('Введите полное имя текстового файла с содержимым: ')
        f=open(file)
        count=int(f.readline())
        num=[]
        for i in range(1,count+1):
            num.append(int(f.readline()))
        f.close()
        print(num)
    except FileNotFoundError:
        print('Файл не найден. Попробуйте еще раз')
        return misstakes()
    except:
        print('Произошла непредвиденная ошибка!')

def main():
    misstakes()
if __name__=='__main__':
    main()