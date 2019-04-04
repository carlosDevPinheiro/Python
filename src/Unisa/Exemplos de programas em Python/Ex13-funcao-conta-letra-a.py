def busca_letra():
    contador = 0
    for letra in palavra:
        if letra == 'a':
            contador += 1
    print 'Na palavra', palavra, 'existem', contador, 'ocorrencias da letra a'

palavra = 'teste'
busca_letra()
palavra = 'reutilizacao'
busca_letra()
palavra = 'codigo'
busca_letra()  