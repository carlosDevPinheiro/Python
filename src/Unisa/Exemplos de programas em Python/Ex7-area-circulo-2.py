import math

raio = input("Digite o valor do raio do circulo: ")
area = math.pi*raio**2
if raio > 0:
  print "Area = ", area
else:
  print "O raio nao pode ser negativo!!!"