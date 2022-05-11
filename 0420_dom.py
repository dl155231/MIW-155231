import copy

import numpy as np
import math


def projekcja(v, u):
    return (np.transpose(v) @ u / (np.transpose(u) @ u)) * u


def e_n(u):
    return u / math.sqrt(np.transpose(u) @ u)


def rozkład(A):
    Q = []
    u_list = []
    e_list = []
    for i in range(A.shape[1]):
        suma_projekcji = 0
        v = np.array(A[:, i]).reshape((A.shape[0], 1))
        for j in range(i):
            suma_projekcji += projekcja(v, u_list[j])
        u = v - suma_projekcji
        u_list.append(u)
        e = e_n(u)
        e_list.append(e)
        Q.append(e[:, 0])
    Q = np.array(np.transpose(Q))
    R = np.transpose(Q) @ A
    return Q, R


def a_k(A, k):
    if A.shape[0] != A.shape[1]:
        raise 'Macierze nie jest kwadratowa.'
    matrix = copy.deepcopy(A)
    for i in range(k):
        Q, R = rozkład(matrix)
        matrix = np.linalg.inv(Q) @ matrix @ Q
    return matrix

np.set_printoptions(suppress=True)
A = np.array([
    [1, 1, 1],
    [1, 0, 0],
    [1, 0, 1],
])
# A = np.array([
#     [1,0],
#     [1,1],
#     [0,1],
# ])

Q, R = rozkład(A)
print(a_k(A, 2))