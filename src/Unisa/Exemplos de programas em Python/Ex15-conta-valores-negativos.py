vet=[0]*6
contador = 0
for i in range(6):
    vet[i]=input('Digite um valor para armazenar no vetor: ')
    if vet[i] < 0:
       contador += 1
print vet
print 'Foram digitados', contador, 'valores negativos'