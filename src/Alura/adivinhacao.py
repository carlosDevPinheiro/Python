import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************",end="\n")

numero_secreto = random.randrange(1,101)
rodada = 1
tentativas = 42

# Usando FOR  
# Obs. if,elif,while não precisa utilizar o parenteses 
 
for rodada in range(1, tentativas + 1):
    print(numero_secreto)
    print("Tentativa {} de {}".format(rodada, tentativas))
    chute_str = input("Digite seu Número: ")
    print("Você digitou: ",chute_str)
    chute = int(chute_str)

    if chute < 1 or chute > 100:
        print('Voce deve digitar um número entre 1 e 100.')
        continue  # pula a interação

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto    

    if acertou :
        print('Voce acertou !')
        break
    else:
        if menor:
            print('Voce errou ! Seu chute foi menor que o numero secreto.')
        elif maior:
            print('Voce errou ! Seu chute foi maior que o numero secreto.')

print("Fim do Jogo")


# Parei na Aula:  Nível e Pontuação > Adicionando níveis ao jogo
# Python proxima aula
# https://cursos.alura.com.br/course/python-3-introducao-a-nova-versao-da-linguagem/task/22811


# Usando WHILE
# while(rodada <= tentativas):    
#     #print('Tentativa: ', rodada," de ",tentativas)
#     print("Tentativa {} de {}".format(rodada, tentativas))
#     chute_str = input("Digite seu Número: ")
#     print("Você digitou: ",chute_str)
#     chute = int(chute_str)

#     acertou = chute == numero_secreto
#     maior   = chute > numero_secreto
#     menor   = chute < numero_secreto

#     if acertou :
#         print('Voce acertou !')
#     else:
#         if menor:
#             print('Voce errou ! Seu chute foi menor que o numero secreto.')
#         elif maior:
#             print('Voce errou ! Seu chute foi maior que o numero secreto.')
#     rodada = rodada + 1
       
  
