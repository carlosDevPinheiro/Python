palavra = raw_input("Digite a palavra: ")
contador = 0
for letra in palavra:
    if letra == 'a':
        contador += 1

print 'Na palavra',palavra,'existem',contador,'ocorrencias da letra a'
