d1=input('Digite o primeiro digito: ')
d2=input('Digite o segundo digito: ')
d3=input('Digite o terceiro digito: ')
d4=input('Digite o quarto digito: ')
d5=input('Digite o quinto digito: ')
d6=input('Digite o sexto digito: ')
d7=input('Digite o setimo digito: ')
d8=input('Digite o oitavo digito: ')
d9=input('Digite o nono digito: ')

soma=d1*10+d2*9+d3*8+d4*7+d5*6+d6*5+d7*4+d8*3+d9*2
soma=soma*10
resto=soma %11
if resto==10:
   d10==0
else:
   d10=soma %11

soma1=d1*11+d2*10+d3*9+d4*8+d5*7+d6*6+d7*5+d8*4+d9*3+d10*2
soma1=soma1*10
resto2=soma1 %11
if resto2==10:
   d11==0
else:
   d11=soma1 %11
   
print('Digito verificador: ')
print(str(d10)+str(d11))

