from random import randrange

def birthday(attempts: int = 1000 , peoples: int = 23):
    count = 0
    for i in range (attempts):
        dates=[]
        for l in range(peoples):
            dates.append(randrange(1,337))
        for a in range(len(dates)-1):
            for j in range(a+1,len(dates)):
                if dates[a] == dates[j]:
                    count+=1
                    break
    return ((count/attempts)*100)


