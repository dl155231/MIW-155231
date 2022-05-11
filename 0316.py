from collections import defaultdict
import math


def metryka_euklidesowa(listaA, listaB):
    wyniki = 0
    for i in range(len(listaA)-1):
        wyniki += (listaA[i]-listaB[i])**2
    return math.sqrt(wyniki)


def load_file_3(file):
    lista = []
    with open(file, 'r') as file:
        for line in file:
            lista.append(
                list(map(lambda e: float(e), line.replace('\n', '').split())))
    return lista


def foo(x, lista):
    list_0 = []
    for i in range(len(lista)):
        klasa_decyzyjna = (lista[i][len(lista[0]) - 1])
        odleglosc = metryka_euklidesowa(x, lista[i])
        list_0.append((klasa_decyzyjna, odleglosc))
    return list_0


def foo_pogrupowane(x, lista):
    slownik = defaultdict(list)
    for i in range(len(lista)):
        klasa_decyzyjna = (lista[i][len(lista[0])-1])
        odleglosc = metryka_euklidesowa(x, lista[i])
        slownik[klasa_decyzyjna].append(odleglosc)
    return slownik


def KLN(x, lista, k):
    slownik = defaultdict(list)
    for i in range(len(lista)):
        klasa_decyzyjna = (lista[i][len(lista[0])-1])
        odleglosc = metryka_euklidesowa(x, lista[i])
        slownik[klasa_decyzyjna].append(odleglosc)
    for key in slownik:
        suma = 0
        for i in slownik[key]:
            # dodaj sume k elementow ( np 5 elementow ) najmniejszych wartosci i wrzuc do slownika
            # przyklad: {1:6, 0:10}
            pass
    return slownik


def metryka_euklidesowa_wektory(obj_1, obj_2):
    wynik = 0
    for a, b in zip(obj_1, obj_2):
        wynik += (a - b)**2
    return wynik**0.5
# dodaj x najblizszych sasiadow z klasy a (5)
# KNN (KNM?): rozne klasy decyzyjne i z kazdej klasy decyzyjnej wez n sasiadow ktorzy sa najblizej
# suma n najblizszych sasiadow z klas wyznaczala wage klas
# jak ilosc najwiekszych klas jest taka sama - brak decyzji


# odleglosci, posortuj, wez 10 najblizszych, policzyc ile elementow z jakiej klasy
#
print(metryka_euklidesowa_wektory([1, 2, 3], [3, 4, 6]))
arr = load_file_3('australian.dat')
# print(arr)
# print(foo([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], arr))
# print(foo_pogrupowane([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], arr))
print(KLN([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], arr, 5))
