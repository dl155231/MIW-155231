# dwa wektory sa:
# niezależne liniowo - z jednego nie da sie zrobic drugiego mnożeniem przez dowolną stałą
# prostopadle - iloczyn skalarny = 0
# A = [v1, v2, ..., vn] -> Q = [e1, e2, ..., en]
# projekcja
# v1 -> u1 -> e1
# z dwoch wektorow v1,v2 zrobic wektory u1 i u2 prostopadłe i niezależne
# wybierz sobie jeden i znajdz drugi prostopadly
# u1 = v1
# u2 = v2 - projekcja_v1(u1)
# un = vn - suma od n=1 do n-1 (projekcja_ui(vi))
# wzor na projekcje
# proj_u(v) = (<v,u>/<u,u>) * u
# <> - iloczyn skalarny
# ei = ui/norma(ui) - wyskalowanie wektora do 1
# norma - dlugosc

macierz_A = [
    [1, 1, 0],
    [0, 1, 1],
]
# licznik = [0, 1, 1] * [1, 1, 0] = 1
# mianownik = [1, 1, 0] * [1, 1, 0] = 2
# projv2(u1) = [1/2, 1/2, 0]
# u2 = [0, 1, 1] - [1/2, 1/2, 0] = [-1/2, 1/2, 1]
# e2 = u2/norma(u2)
# norma u2 = sqrt(6)/2
# e2 = [-1/2, 1/2, 1] * 2/sqrt(6)
# e2 = [-sqrt(6)^(-1), sqrt(6)^(-1), 2*sqrt(6)^(-1)]
