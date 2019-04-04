import numpy as np

a = input("Digite o valor (1, 1) da matriz 1: ")
b = input("Digite o valor (1, 2) da matriz 1: ")
c = input("Digite o valor (2, 1) da matriz 1: ")
d = input("Digite o valor (2, 2) da matriz 1: ")
e = input("Digite o valor (1, 1) da matriz 2: ")
f = input("Digite o valor (1, 2) da matriz 2: ")
g = input("Digite o valor (2, 1) da matriz 2: ")
h = input("Digite o valor (2, 2) da matriz 2: ")
i = np.array([[a, b], [c, d]])
j = np.array([[e, f], [g, h]])

k = i * j

print k
