# -*- coding: cp1252 -*-
a = float(input("Digite o peso da moeda A: "))
b = float(input("Digite o peso da moeda B: "))
c = float(input("Digite o peso da moeda C: "))
d = float(input("Digite o peso da moeda D: "))
e = float(input("Digite o peso da moeda E: "))
f = float(input("Digite o peso da moeda F: "))
g = float(input("Digite o peso da moeda G: "))
h = float(input("Digite o peso da moeda H: "))

comp1 = a+b+c
comp2 = d+e+f
comp3 = a+d
comp4 = b+e

if comp1 > comp2:
    if comp3 > comp4:
        if a > b:
            print("A moeda A � a com peso diferente e � mais pesada")
        elif a == b:
            print("A moeda E � a com peso diferente e � mais leve")
    elif comp3 == comp4:
        if c > a:
            print("A moeda C � a com peso diferente e � mais pesada")
        elif c == a:
            print("A moeda F � a com peso diferente e � mais leve")
    elif comp3 < comp4:
        if b > a:
            print("A moeda B � a com peso diferente e � mais pesada")
        elif b == a:
            print("A moeda D � a com peso diferente e � mais leve")
elif comp1 == comp2:
    if g > h:
        if g > a:
            print("A moeda G � a com peso diferente e � mais pesada")
        elif g == a:
            print("A moeda H � a com peso diferente e � mais leve")  
    elif g < h:
        if h > a:
            print("A moeda H � a com peso diferente e � mais pesada")
        elif h == a:
            print("A moeda G � a com peso diferente e � mais leve")
elif comp1 < comp2:
    if comp3 > comp4:
        if a > b:
            print("A moeda B � a com peso diferente e � mais leve")
        elif a == b:
            print("A moeda D � a com peso diferente e � mais pesada")
    elif comp3 == comp4:
        if a > c:
            print("A moeda C � a com peso diferente e � mais leve")
        elif a == c:
            print("A moeda F � a com peso diferente e � mais pesada")
    elif comp3 < comp4:
        if b > a:
            print("A moeda A � a com peso diferente e � mais leve")
        elif b == a:
            print("A moeda E � a com peso diferente e � mais pesada")


    