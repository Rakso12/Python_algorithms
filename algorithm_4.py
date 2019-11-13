#Problem 4
#Find palindrome

palindrome = lambda x:x == x[::-1]
max =0
for liczba_1 in range(100,1000):
    for liczba_2 in range(100,1000):
        wynik = liczba_1 * liczba_2
        wynik = str(wynik)
        if(palindrome(wynik) == True):
            print("{} * {} = {}".format(liczba_1,liczba_2,wynik))
            wynik = int(wynik)
            if(wynik>max):
                max = wynik
print(max)