import random

vet=[0]*5
for i in range(5):
    vet[i]=input('Digite um valor para armazenar no vetor: ') 
vet.sort() #ordena a lista
print vet
vet.sort(reverse=True) #inverte a lista
print vet
random.shuffle(vet) #embaralha a lista
print vet