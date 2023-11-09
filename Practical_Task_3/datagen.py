def get_words(path=r"D:\practice3\words.txt"): #ввел путь, который на домашнем ПК
    with open(path,encoding='utf8') as text:
        words=text.read().upper().splitlines()
        return words
def get_records(record, path=r"D:\practice3\record.txt"): #ввел путь, который на домашнем ПК
    with open(path,mode='r+', encoding='utf8') as record_file:
        cur_record = record_file.readline()
        cur_record = max(int(cur_record),int(record))
        record_file.seek(0)
        record_file.write(str(cur_record))
        return cur_record