import math
import random
from tokenize import group
import numpy as np
import time
from datetime import timedelta


def metryka_euklidesowa(listaA, listaB):
    wynik = 0
    for i in range(len(listaA) - 1):
        wynik += (listaA[i] - listaB[i])**2
    return wynik**0.5


def euklidesowa_wektorki_1(obj_1, obj_2):
    wynik = 0
    for a, b in zip(obj_1, obj_2):
        wynik += (a - b)**2
    return wynik**0.5


def euklidesowa_wektorki_2(lista1, lista2, obcinac=False):
    if obcinac:
        v1 = np.array(lista1[:-1])
        v2 = np.array(lista2[:-1])
    else:
        v1 = np.array(lista1)
        v2 = np.array(lista2)
    d = v1 - v2
    return np.dot(d, d)**0.5


# y = data[0]
# klasy = {}

# for line in data[1:]:
#     if klasy.get(line[-1]) is None:
#         klasy[line[-1]] = [metryka_euklidesowa(line, y)]
#     else:
#         klasy[line[-1]].append(metryka_euklidesowa(line, y))


# usun klasy z australiana -> nowa lista
# podziel losowo na klasy 0 i 1
# (na wszelki wypadek nowa lista z dopisanymi klasami)
# sklej w slownik
# ustal wektor z najmniejsza suma do innych
# przelec nowa lista przez wszystkie wektorki (bez wzgledu na klase)
# jak odlegosc wektorka blizsza do 0 to ustaw klase 0, w przeciwnym wypadku ustaw 1
# jak sie skonczy to skoncz, jak nie to przelec N razy

def group_classes(data):
    
    grouped = dict.fromkeys([0, 1])

    for line in data:
        if grouped.get(line[-1]) is None:
            grouped[line[-1]] = [line]
        else:
            grouped[line[-1]].append(line)
    return grouped


def min(grouped_data):
    class_min = {}
    for key, value in grouped_data.items():
        suma = 0
        min = math.inf
        for obj in value:
            suma = sum(euklidesowa_wektorki_2(obj, line, True) for line in value)
            if suma < min and suma != 0:
                min = suma
                min_v = obj
            elif suma == min:
                pass
        class_min[key] = min_v
    return class_min


def kolorowanie(data, class_min):
    for i in range(10):
        changes_count = 0
        for vector in data:
            d_0 = euklidesowa_wektorki_2(vector, class_min[0])
            d_1 = euklidesowa_wektorki_2(vector, class_min[1])
            decision_class = 0 if d_0 < d_1 else 1
            if vector[-1] != decision_class:
                vector[-1] = decision_class
                changes_count += 1
        class_min = min(group_classes(data))
        print(changes_count)
    print(class_min)
    return data


def assign_random_class(data):
    for line in data:
        line[-1] = random.randint(0, 1)
    return data


def main():
    plik = open('new_australian.dat')
    # plik2 = open('new_australian.dat', 'w')

    data = []
    for line in plik:
        row = line.split()
        data.append(list(map(lambda x: float(x), row)))

    # randomized_data = assign_random_class(data)
    grouped_data = group_classes(data)
    class_min = min(grouped_data)
    final_data = kolorowanie(data, class_min)
    


if __name__ == '__main__':
    main()
    # 28 lutego 1:10 filmiku
    # pierwsza kropka - suma odleglosci od wszystkich innych punktów

    # metoda Monte Carlo
    # 1. określić maksimum funkcji na przedziale
    # 1a. przejść przedział w pewnym kroku
    # 1b. weź największy y*2
    # 2. pole - d1*d2 - całka na pewno nie większa niż pole
    # 3.
    ##

    # metoda prostokątów

    # metoda trapezów
