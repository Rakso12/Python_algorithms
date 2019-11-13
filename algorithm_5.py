import time

start = time.time()
licznik = 0
liczba = 0

for liczba in range(1,240000000):
    for dzielnik in range(1,21):
        if(liczba%dzielnik == 0):
            licznik += 1
        else:
            break
    if(licznik==20):
        print("Wynik: {}".format(liczba))
        break;
    licznik=0

stop = time.time()

print("czas: " + str(stop-start))