L1=input('Insira o lado 1 do triangulo: ')
L2=input('Insira o lado 2 do triangulo: ')
L3=input('Insira o lado 3 do triangulo: ')

if (L1==L2) and (L1==L3) and (L3==L2):
      print('Triangulo equilatero')
elif (L1<>L2) and (L1<>L3) and (L2<>L3):
      print('Triangulo escaleno')
elif (L1==L2) and (L1<>L3) and (L2<>L3):
      print('Triangulo isosceles')
elif (L2==L3) and (L1<>L3) and (L2<>L1): 
      print('Triangulo isosceles')
elif (L3==L1) and (L3<>L2) and (L1<>L2):
      print('Triangulo isosceles')
else:
      print('Nao triangulo')