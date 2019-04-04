a = raw_input("Digite um caracter ASCII em binario: ")
b=hex(int(a,2))
c = b.split('0x')
d = c[1]
e = d.decode('hex')
print e