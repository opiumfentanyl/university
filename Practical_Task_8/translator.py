import pymorphy3

from translate import Translator

def get_words():
    text=[]
    with open("aaa.txt",mode='r',encoding='utf-8') as file:
        for i in file.readlines():
            words = i.replace('.','').replace(',','').replace('?','').replace('!','').replace('(','').replace(')','').replace('\n','')
            for j in words.split():
                text.append(j.lower())
    return text

def normal(text):
    normal_text=[]
    for i in text:
        morph=pymorphy3.MorphAnalyzer()
        normal_text.append(morph.parse(i)[0].normal_form)
    return normal_text

def countt(normal_text):
    dict = {}
    for i in range(len(normal_text)):
        if not normal_text[i] in dict:
            dict[normal_text[i]] = 1
        else:
            dict[normal_text[i]] += 1
    return dict

def sortt(dict):
    sorted_dict = sorted(dict.items(),key=lambda i:i[1])
    sorted_dict.reverse()
    return sorted_dict

def translatee(words):
    translator = Translator(from_lang="ru", to_lang="en")
    with open('translation.txt', mode='w', encoding = 'utf-8') as file:
        for i in range(len(words)):
            translation = translator.translate(words[i][0])
            file.write(f"{words[i][0]}|{translation}|{words[i][1]}\n")
            print(f"Переведено слов: {i + 1}")




