lista = [1, 2, 3, 4, 5]
def somalista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + somalista(lista[1:])    
print('Resultado de somalista:', somalista(lista))
print('Resultado esperado:', sum(lista))