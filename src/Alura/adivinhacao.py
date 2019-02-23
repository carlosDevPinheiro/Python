print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************",end="\n")

numero_secreto = 42
chute = input('Digite o seu numero: ')
print('Voce digitou o numero: ',chute)

if numero_secreto == int(chute):
    print('Voce acertou !')
else:
    print('voce errou :( ')


print("Fim do Jogo")
