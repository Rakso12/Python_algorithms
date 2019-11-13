import math
liczba = 600851475143
dzielnik = 2
for i in range(2,liczba):
    while(liczba%dzielnik==0):
        print(liczba)
        print(dzielnik)
        liczba = liczba/dzielnik
    dzielnik += 1
print(liczba)