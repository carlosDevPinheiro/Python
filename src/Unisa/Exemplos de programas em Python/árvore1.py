# -*- coding: cp1252 -*-

class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left  = left
        self.right = right

def printTreeIndented(tree, level=0):
    if tree == None: return
    printTreeIndented(tree.right, level+1)
    print '  '*level + str(tree.cargo)
    printTreeIndented(tree.left, level+1)

def abertura():
    a = input("Digite o valor da raiz da árvore: ")
    b = input("Digite o valor de uma das folhas: ")
    c = input("Digite o valor da outra folha: ")

    if b > a and c < a:
        tree = Tree(a, Tree(c), Tree(b))
        printTreeIndented(tree, level=0)
    elif b < a and c > a:
        tree = Tree(a, Tree(b), Tree(c))
        printTreeIndented(tree, level=0)
    else:
        print "Os valores devem ser maiores ou menores que a raiz!"
        abertura()
abertura()
