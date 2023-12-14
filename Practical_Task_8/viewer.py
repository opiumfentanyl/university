from translator import*

def show():
    text = get_words()
    normal_text = normal(text)
    dict = countt(normal_text)
    words = sortt(dict)
    translatee(words)

if __name__ == "__main__":
    show()