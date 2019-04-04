# -*- coding: utf-8 -*-

# Programa que lê duas palavras da entrada e, na saída, imprime a menor palavra".

################################################################################################################


def quantidade_de_letras (palavra) :
    quantidade = len (palavra)
    return quantidade


a = raw_input ('Digite uma palavra: ')
b = raw_input ('Digite outra palavra: ')


if quantidade_de_letras (a) > quantidade_de_letras (b):
    print 'Menor palavra = ', b
elif quantidade_de_letras (a) == quantidade_de_letras (b):
    print 'As duas palavras possuem a mesma quantidade de letras'
else:
    print 'Menor palavra = ', a