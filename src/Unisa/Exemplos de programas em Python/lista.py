class Lista(object):
    def __init__(self):
        self.dados = []
    def insere(self, elemento):
        self.dados.append(elemento)
    def retira(self):
        return self.dados.pop(0)
    def vazia(self):
        return len(self.dados) == 0

lista = [10, 20, 30, 40, 50]
lista.append(60)
print lista
lista.pop(0)
print lista
del lista[0]
lista.insert(0,15)
print lista
lista.pop(4)
print lista
lista.append(80)
print lista
lista.insert(2,75)
lista.append(67)
print len (lista)
