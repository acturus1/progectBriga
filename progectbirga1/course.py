import randomimport timefrom threading import Thread# dinamic action# if yesornoo == 1:aktioprise = 100def dinamicaction(aktioprise):    while True:        aktioprise = 100        b = random.randint(0, 1)        if b == 0:            aktioprise = aktioprise - random.random()            print(f'Сейчас 1 акция стоит: {aktioprise}', end="\b")            time.sleep(2.5)            print('', end="\r")            return aktioprise        elif b == 1:            aktioprise = aktioprise + random.random()            print(f'Сейчас 1 акция стоит: {aktioprise}', end="\b")            time.sleep(2.5)            print('', end="\r")            return aktioprise    return aktioprisedi1 = Thread(target=dinamicaction)while aktioprise > 0:    yesornoo = int(input('(1/0)'))    if yesornoo == 1:        print(aktioprise)    elif yesornoo == 0:        breakif __name__ == '__main__':    course.py()    di1.start()    di1.join()