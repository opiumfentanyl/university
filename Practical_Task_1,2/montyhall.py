from random import randrange
def montyhall(attempts:int=10000):
    count = 0
    for i in range(attempts):
        choise = randrange(1,3)
        door = randrange(1, 3)
        if choise == door:
            count += 1
    return((count/attempts)*100)

def main():
    print(montyhall(),'%')
if __name__ == '__main__':
    main()