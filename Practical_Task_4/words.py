def read_file(path='D:\qqq\practice4\data.txt'): #ссылка на расположение файла на домашнем ПК
    with open(path,mode='r',encoding='utf8') as text:
        word = text.read().split()
        l=[]
        for i in word:
            l.append(''.join(filter(str.isalnum,i)).lower())
        words = set(l)
        return sorted(words)

def save_file(path='D:\qqq\practice4\count.txt',words=read_file()): #ссылка на расположение файла на домашнем ПК
    with open(path,mode='w', encoding='utf8') as new:
        new.write('Всего уникальных слов: '+str(len(words))+ '\n===================================================\n')
        for i in range(len(words)):
            new.write(words[i]+'\n')

def main():
    read_file()
    save_file()

if __name__ == '__main__':
    main()
