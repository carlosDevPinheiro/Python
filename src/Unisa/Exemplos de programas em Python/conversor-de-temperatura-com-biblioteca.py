# -*- coding: cp1252 -*-
import sys
import conversor

def menu():
    print ("Conversor de temperatura")
    print (" ")
    print ("Digite a opção desejada: ")
    print (" ")
    print ("1 para temperatura em Celsius")
    print ("2 para temperatura em Kelvin")
    print ("3 para temperatura em Réamur")
    print ("4 para temperatura em Fahrenheit")
    print ("0 para sair") 
    print (" ")

    c = raw_input("Digite a opção desejada: ")
    d = float(raw_input("Digite o valor da temperatura: "))

    if c == '1':
        print("Temperatura em Fahreiheit: ", conversor.celsius2fahrenheit(d))
        print("Temperatura em Réamur: ", conversor.celsius2reamur(d))
        print("Temperatura em Celsius: ", conversor.celsius2kelvin(d))

    elif c == '2':
        print("Temperatura em Fahreiheit: ", conversor.kelvin2fahrenheit(d))
        print("Temperatura em Réamur: ", conversor.kelvin2reamur(d))
        print("Temperatura em Celsius: ", conversor.kelvin2celsius(d))

    elif c == '3':
        print("Temperatura em Fahreiheit: ", conversor.reamur2fahrenheit(d))
        print("Temperatura em Celsius: ", conversor.reamur2celsius(d))
        print("Temperatura em Kelvin: ", conversor.reamur2kelvin(d))

    elif c =='4':
        print("Temperatura em Celsius: ", conversor.fahrenheit2celsius(d))
        print("Temperatura em Réamur: ", conversor.fahrenheit2reamur(d))
        print("Temperatura em Kelvin: ", conversor.fahrenheit2kelvin(d))

    elif c == '0':
        sys.exit()

    else:
        print("Digite a opção certa!")
        menu()
    menu()
menu()
        
