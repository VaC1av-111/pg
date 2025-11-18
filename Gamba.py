import random
import time

if __name__ == "__main__":
    symboly = ["A", "K", "Q", "J", "10", "9", "8", "7"]


    steps = 0
    while True:
        steps += 1
        vysledek = []
        for i in range (3):
            vysledek.append (random.choice(symboly))
        print (vysledek)
        if len(set(vysledek)) == 1:
            print (f"Vyhral jsi po {steps} tazich!")
            break


    print (random.choice(symboly))

if __name__ == "__main__":
    ts = time.time()
    #hraci_automat()

    print (f'Program bezel {time.time() - ts} sekund.')