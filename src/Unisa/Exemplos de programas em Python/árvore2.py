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

def printTreeIndented1(tree, level=0):
    if tree == None: return
    printTreeIndented1(tree.left, level+1)
    print '  '*level + str(tree.cargo)
    printTreeIndented1(tree.right, level+1)

def abertura():
    a = input("Digite o valor da raiz da árvore: ")
    b = input("Digite o valor de um nó: ")
    c = input("Digite o valor de um nó: ")
    d = input("Digite o valor de uma das folhas: ")
    e = input("Digite o valor de uma das folhas: ")

    if b > a and c > b > a and d > c > a and e > d > a:
        tree = Tree(a, Tree(b, Tree(c, Tree(d, Tree(e)))))
        #tree = Tree(a, Tree(c), Tree(b))
        printTreeIndented(tree, level=0)

    elif b < a and c < b < a and d < c < a and e < d < a:
        tree = Tree(e, Tree(d, Tree(c, Tree(b, Tree(a)))))
        printTreeIndented1(tree, level=0)

    elif b < a and c < b < a and d < c < e and e > c < b and e > c > d and e > d:
        tree = Tree(a, Tree(b, Tree(c, Tree(d), Tree(e))))
        printTreeIndented(tree, level=0)

    elif b > a and c > b > a and d < c < e and e > c > b and e > c > d and e > d:
        tree = Tree(a, Tree(b, Tree(c, Tree(d), Tree(e))))
        printTreeIndented1(tree, level=0)

    elif a > b > d and b > d and a < c < e and c < e:
        tree = Tree(a, Tree(c, Tree(e)), Tree(b, Tree(d)))
        printTreeIndented1(tree, level=0)

    else:
        print "Os valores devem ser maiores ou menores que a raiz!"
        abertura()
abertura()

