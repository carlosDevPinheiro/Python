class Fila(object):
    def __init__(self):
        self.dados = []
    def insere(self, elemento):
        self.dados.append(elemento)
    def retira(self):
        return self.dados.pop(0)
    def vazia(self):
        return len(self.dados) == 0

fila = [10, 20, 30, 40, 50]
fila.append(60)
print fila
fila.pop(0)
print fila
fila.append(70)
print fila
fila.pop(0)
print fila
fila.append(80)
print fila
print len (fila)