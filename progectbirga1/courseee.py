import random
import time
while True:
    aktioprise = 100
    b = random.randint(0, 1)
    if b == 0:
        aktioprise = aktioprise - random.random()
        print(f'Сейчас 1 акция стоит: {aktioprise}', end="\b")
        time.sleep(2.5)
        print('', end="\r")
    elif b == 1:
        aktioprise = aktioprise + random.random()
        print(f'Сейчас 1 акция стоит: {aktioprise}', end="\b")
        time.sleep(2.5)
        print('', end="\r")
