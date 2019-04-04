from sympy.crypto.crypto import encipher_hill, decipher_hill
from sympy import Matrix

key = Matrix([[1, 2], [3, 5]])
a = raw_input("Write the pure text: ")
b = encipher_hill(a, key)
c = decipher_hill(b, key)
print b
print c

