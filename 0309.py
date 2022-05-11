from typing import List
import math

plik = open('australian.dat')
lista = []
for line in plik:
    row = line.split()
    lista.append(list(map(lambda x: float(x), row)))

for i in range(5):
    print(lista[-i])


def metryka_euklidesowa(listaA: List[float], listaB: List[float]) -> List[float]:
    wynik = 0
    for i in range(len(listaA) - 1):
        wynik += (listaA[i] - listaB[i])**2
    return math.sqrt(wynik)


print('\n', metryka_euklidesowa(lista[0], lista[1]))

# d(y, x) gdzie x nalezy do listy, ale nie jest on pierwszym elementem
# slownik: klucz - klasa decyzyjna x(ostatnia wartosc), wartosc: lista z odleglosciami
# w skrocie: liczymy odleglosci y do reszty punktow metryka
# jak klasa decyzyjna to dodajemy do wartosci slownika o kluczu klasy
#    
## 2
# funckja - wyznacznik macierzy kwadratowej dowolnego wymiaru