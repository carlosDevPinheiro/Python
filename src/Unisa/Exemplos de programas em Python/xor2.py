print "Ao preencher o valor binario, coloque '0b' antes do valor digitado"
a = input("Digite o valor binario: ")
b = input("Digite o outro valor binario: ")
c = (a ^ b)
d = '{:b}'.format(c)
print d