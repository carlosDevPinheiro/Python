def conta_letra(letra_esperada, frase):
    contador = 0
    for letra in frase:
        if letra == letra_esperada:
            contador += 1
    print 'Foram encontradas',contador,'ocorrencias da letra',letra_esperada

conta_letra(raw_input('Digite a letra: '), raw_input('Digite a frase: '))
