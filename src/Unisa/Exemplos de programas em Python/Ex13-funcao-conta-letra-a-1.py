def busca_letra():
    contador = 0
    for letra in palavra:
        if letra == 'a':
            contador += 1
    print 'Na palavra',palavra,'exitem',contador,'ocorrencias da letra a'

palavra = raw_input("Digite a palavra: ")
busca_letra()
