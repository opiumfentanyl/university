import random

def pole():
    record = 0
    with open('record.txt',encoding="utf-8") as r:
        rec=int(str(r.read()))
    t=1 #Проверка на значение(если вводил число !=1,2,3, выдавал ошибку.
    while t == 1:
        lvl = input('Уровни сложности:\n1.Легкий - Вам дается 7 жизней.\n2.Средний - Вам дается 5 жизней.\n3.Сложный - Вам дается 3 жизни.\nВведите желаемый номер уровня сложности: ')
        if lvl == '1':
            starthealth = 7
            t=0
        elif lvl == '2':
            starthealth = 5
            t=0
        elif lvl == '3':
            starthealth = 3
            t=0
        else:
            print('Вы ввели недопустимое значение!')
            t=1


    with open('words.txt',encoding="utf-8") as text:
        words = text.read().splitlines()
    play = 1

    while play == 1:
        end = 1
        health = starthealth
        word = random.choice(words).upper()
        words.remove(word.lower())
        hide = ['*'] * len(word)
        while end == 1:
            letter=input('Назовите букву или слово целиком: ').upper()
            if len(letter) == 1 and letter in word and not(letter) in hide:
                for i in range(len(word)):
                    if letter == word[i]:
                        hide[i] = letter
                print('Вы угадали букву!\n' + str(hide) +'  Количество жизней: '+ str(health))
                if hide == word:
                    record += 1
                    print('Вы выиграли! Приз в студию!\nВаш рекорд: ' + str(max(record,rec)))
                    end = 0

            elif letter in hide :
                print('Такая буква уже есть! Попробуйте другую букву\n' + str(hide) + ' Количество жизней: ' + str(health))

            elif letter == word:
                record += 1
                print('Вы выиграли! Приз в студию!\nВаш рекорд: ' + str(max(record,rec)))
                end = 0

            else:
                health -= 1
                print('Неправильно. Вы теряете жизнь.\n' + str(hide) + 'Количество жизней: ' + str(health))
                if health == 0:
                    print('Жизни закончились. Вы проиграли! Загаданное слово:'+ str(word)+'\nВаш рекорд:'+ str(max(record,rec)))
                    end = 0


        if len(words)!=0:
            b = 1 #проверка на значение
            while b == 1:
                contunue = input('Желаете продолжить игру? Если да, введите: Да. Если нет, введите: Нет\n').lower()
                if contunue == 'да':
                    t = 1  # Проверка на значение(если вводил число !=1,2,3, выдавал ошибку.
                    while t == 1:
                        lvl = input(
                            'Уровни сложности:\n1.Легкий - Вам дается 7 жизней.\n2.Средний - Вам дается 5 жизней.\n3.Сложный - Вам дается 3 жизни.\nВведите желаемый номер уровня сложности: ')
                        if lvl == '1':
                            starthealth = 7
                            t = 0
                            play = 1
                        elif lvl == '2':
                            starthealth = 5
                            t = 0
                            play = 1
                        elif lvl == '3':
                            starthealth = 3
                            t = 0
                            play = 1
                        else:
                            print('Вы ввели недопустимое значение!')
                            t = 1
                    b = 0
                elif contunue == 'нет':
                    print('Ждем Вас снова! Ваш рекорд за все время: '+ str(max(record,rec)))
                    play = 0
                    b = 0
                else:
                    print('Вы ввели недопустимое значение')
                    b = 1
        else:
            play = 0
            print('Слова в списке закончились!')
    with open('record.txt', mode='w', encoding="utf-8") as k:
        k.write(str(max(record,rec)))

def main():
    print(pole())

if __name__ == '__main__':
    main()
