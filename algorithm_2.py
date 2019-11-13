#Problem 2
#Sum fibonacii (max value 4mln)

def fibonaci(n):
    liczba_1 = 0
    liczba_2 = 1
    i=0
    suma=0
    while(i<n):
        print(liczba_2)
        liczba_2 += liczba_1
        liczba_1 = liczba_2 - liczba_1
        i+=1
        if(liczba_2%2==0):
            suma+= liczba_2
            print("Suma {}".format(suma))
        if(liczba_2>4000000):
            break

fibonaci(50)