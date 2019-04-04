a = raw_input("Digite uma string ASCII: ")
b = bin(reduce(lambda x, y: 256*x+y, (ord(c) for c in a), 0))
c = b.split('0b')
print ('String digitada em ASCII: '), c[1]