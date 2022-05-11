import numpy
import numpy as np
import math

np.set_printoptions(suppress=True)

def rozklad_qr(macierz):
    macierz_t = np.transpose(macierz)  # aby mogło to iterować po kolumnach
    e_dict = {}
    projekcje = []
    u_dict = {}
    for i in range(len(macierz_t)):
        if i == 0:
            v_n = macierz_t[i]
            u_n = v_n
            u_dict[i] = u_n
            u_n_len = math.sqrt(sum(i ** 2 for i in u_n))  # długość wektora u
            e_n = u_n / u_n_len
            e_dict[i] = e_n
        else:
            v_n = macierz_t[i]
            u_n_minus_1 = u_dict[i-1]
            projekcja_n = ((np.transpose(v_n) @ u_n_minus_1) / (np.transpose(u_n_minus_1) @ u_n_minus_1)) * u_n_minus_1
            projekcje.append(projekcja_n)
            u_n = v_n.astype(np.float64)
            # print(u_n)
            for q in projekcje:
                u_n = np.subtract(u_n.astype(np.float64, copy=False), q.astype(np.float64, copy=False))
                print(u_n)  # tu jest zle bo te gowno nie potrafi odejmowac, do chuja pana.. KURWAAAAAAAAAA!!!!!!!!

            u_dict[i] = u_n
            u_n_len = math.sqrt(sum(i ** 2 for i in u_n))  # długość wektora u
            e_n = u_n / u_n_len
            e_dict[i] = e_n
    q = []
    for e in e_dict.values():
        q.append(e)
    q = np.transpose(q)
    r = np.transpose(q) @ macierz
    return q, r


A = np.array([
    [1, 1, 1],
    [1, 0, 0],
    [1, 0, 1],
], dtype=np.float)
# A = np.array([
#     [1,0],
#     [1,1],
#     [0,1],
# ])

Q, R = rozklad_qr(A)
print('QR', Q @ R)