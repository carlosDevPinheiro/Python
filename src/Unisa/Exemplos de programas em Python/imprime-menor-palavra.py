# -*- coding: cp1252 -*-

# Campina Grande, 23/05/2008.
# Diógenes da Silva Sousa.

# Programa que lê duas palavras da entrada e, na saída, imprime a menor palavra".

################################################################################################################


def quantidade_de_letras (palavra) :
    quantidade = len (palavra)
    return quantidade


a = raw_input ('Digite uma palavra...     ')
b = raw_input ('Digite outra palavra...     ')


if quantidade_de_letras (a) > quantidade_de_letras (b):
    print 'A menor palavra e ', b
elif quantidade_de_letras (a) == quantidade_de_letras (b):
    print 'As duas palavras tem a mesma quantidade de letras'
else:
    print 'A menor palavra e ', a


###############################################################################################################

    
sair = raw_input ('Tecle <ENTER> para encerrar...')

