from random import randrange
def monty_hall(attempts:int=10000):
    count = 0
    for i in range(attempts):
        choise = randrange(1,3)
        door = randrange(1, 3)
        if choise == door:
            count += 1
    return((count/attempts)*100)


