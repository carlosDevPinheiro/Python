# -*- coding: latin1 -*-

#A lista possui o m�todo pop() que facilita a implementa��o de filas e pilhas:
lista = ['A', 'B', 'C']
print 'lista:', lista

# A lista vazia � avaliada como falsa
while lista:

    # Em filas, o primeiro item � o primeiro a sair
    # pop(0) remove e retorna o primeiro item
    print 'Saiu', lista.pop(0), ', faltam', len(lista)

# Mais itens na lista
lista += ['D', 'E', 'F']
print 'lista:', lista

while lista:

    # Em pilhas, o primeiro item � o �ltimo a sair
    # pop() remove e retorna o �ltimo item
    print 'Saiu', lista.pop(), ', faltam', len(lista)