import numpy as np
import math

def iloczyn_skalarny(v1,v2):
     suma = 0
     for i in range(len(v1)):
          suma += v1[i]*v2[i]
          print(suma)
     return suma

A = [[2, 0],
     [1, 1],
     [0, 2]]
A = np.asmatrix(A)
v1 = [2, 1, 0]
v2 = [0, 1, 2]
u1 = v1
u1_norma = math.sqrt(np.dot(u1, u1))
e1 = np.multiply(u1, 1/u1_norma)

projekcja_v2 = np.dot(v2, u1)/np.dot(u1, u1)
projekcja_v2 = np.multiply(projekcja_v2, u1)
u2 = np.subtract(v2, projekcja_v2)
u2_norma = np.sqrt(np.dot(u2, u2))
print(iloczyn_skalarny(u2, u2), 'dot')
print(u2, 'u2')

e2 = np.multiply(u2, 1/u2_norma)
print(e2, 'e2')
Q_np_T = np.asmatrix([e1, e2])
R = Q_np_T @ A
QR = np.transpose(Q_np_T) @ R
