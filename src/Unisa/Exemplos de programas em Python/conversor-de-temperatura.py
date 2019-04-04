# -*- coding: cp1252 -*-

import sys

def menu():
    print ("Conversor de temperatura")
    print (" ")
    print ("Digite a opção desejada: ")
    print (" ")
    print ("1 para converter Celsius para Fahrenheit")
    print ("2 para converter Celsius para Kelvin")
    print ("3 para converter Celsius para Réamur")
    print ("4 para converter Fahrenheit para Celsius")
    print ("5 para converter Fahrenheit para Kelvin")
    print ("6 para converter Fanrenheit para Réamur")
    print ("7 para converter Kelvin para Celsius")
    print ("8 para converter Kelvin para Fahrenheit")
    
    print ("9 para converter Kelvin para Réamur")
    print ("10 para converter Réamur para Celsius")
    print ("11 para converter Réamur para Fahrenheit")
    print ("12 para converter Réamur para Kelvin")
    print ("0 para sair") 
    print (" ")

    a = input("Digite a opção desejada: ")

    if a == "1":
        celsius2fahrenheit()
    elif a == "2":
        celsius2kelvin()
    elif a == "3":
        celsius2reamur()
    elif a == "4":
        fahrenheit2celsius()
    elif a == "5":
        fahrenheit2kelvin()
    elif a == "6":
        fahrenheit2reamur()
    elif a == "7":
        kelvin2celsius()
    elif a == "8":
        kelvin2fahrenheit()
    elif a == "9":
        kelvin2reamur()
    elif a == "10":
        reamur2celsius()
    elif a == "11":
        reamur2fahrenheit()
    elif a == "12":
        reamur2kelvin()
    elif a =="0":
        sys.exit()
    else:
        print("Digite uma das opções acima!")
        menu()
    menu()
            
def celsius2fahrenheit():
    a = float(input("Digite a temperatura em graus Celsius: "))
    b = (1.8*a)+32.0
    print("Temperatura em Fahrenheit: ", b)

def celsius2kelvin():
    a = float(input("Digite a temperatura em graus Celsius: "))
    b = a+273
    print("Temperatura em Kelvin: ", b) 

def celsius2reamur():
    a = float(input("Digite a temperatura em graus Celsius: "))
    b = a*0.8
    print("Temperatura em Réamur: ", b) 

def fahrenheit2celsius():
    a = float(input("Digite a temperatura em graus Fahrenheit: "))
    b = (a-32)/1.8
    print("Temperatura em graus Celsius: ", b)

def fahrenheit2kelvin():
    a = float(input("Digite a temperatura em graus Fahrenheit: "))
    b = ((a-32)/1.8)+273
    print("Temperatura em Kelvin: ", b) 

def fahrenheit2reamur():
    a = float(input("Digite a temperatura em graus Fahrenheit: "))
    b = ((a-32)/1.8)*0.8
    print("Temperatura em Réamur: ", b) 

def kelvin2celsius():
    a = float(raw_input("Digite a temperatura em graus Kelvin: "))
    b = a-273
    print("Temperatura em Celsius: ", b)

def kelvin2fahrenheit():
    a = float(raw_input("Digite a temperatura em graus Kelvin: "))
    b = ((a-273)*1.8)+32
    print("Temperatura em Fahrenheit: ", b)

def kelvin2reamur():
    a = float(raw_input("Digite a temperatura em graus Kelvin: "))
    b = (a-273)*0.8
    print("Temperatura em Réamur: ", b)

def reamur2celsius():
    a = float(raw_input("Digite a temperatura em graus Réamur: "))
    b = a/0.8
    print("Temperatura em graus Celsius: ", b)
    
def reamur2fahrenheit():
    a = float(raw_input("Digite a temperatura em graus Réamur: "))
    b = (a*2.25)+32
    print("Temperatura em Fahrenheit: ", b) 

def reamur2kelvin():
    a = float(raw_input("Digite a temperatura em graus Réamur: "))
    b = a*(5/4)+273
    print("Temperatura em Kelvin: ", b)

menu()
