def inf(info):
    with open (info, mode='r',encoding='utf-8') as text:
        words = text.read().splitlines()
    strings =[i.split('|') for i in words]
    return strings

def get_books(word,strings):
    result_string=[]
    for string in strings:
        for choose in string:
            if word in choose:
                result_string.append(string)
    return result_string

def get_totals(list):
    result_str=[]
    for element in list:
        if (int(element[3])*float(element[4]))<500:
            result_str.append((element[0], int(element[3]) * float(element[4]) + float(100)))
        else:
            result_str.append((element[0], int(element[3]) *float(element[4])))
    return result_str

