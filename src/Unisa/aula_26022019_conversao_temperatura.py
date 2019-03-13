
# temperatura = float(input("Digite uma temperatura em ºC: "))
# cf = (temperatura * 9/5) + 32   # (0 °C × 9/5) + 32 = 32 °F
# ck = temperatura + 273.15       # 0 °C + 273,15 = 273,15 K
# cr =  temperatura * 4/5         # °Ré = °C × 4/5

# print("a temperatura {:03.1f} °C em Fahrenheit é {:03.1f}°F .".format(temperatura, cf))
# print("a temperatura {:03.1f} °C em Kelvin é {:03.1f}°K .".format(temperatura, ck))
# print("a temperatura {:03.1f} °C em Réaumur é {:03.1f}°Re .".format(temperatura, cr))

# fc = ((cf - 32) / 1.8)  # ((F -32) / 1.8)
# fk = ((cf - 32)/ 1.8) + 273
# fr = (cf - 32) * 4/9    # ([°F] − 32) × 4⁄9

# print("a temperatura {:03.1f} °F em  °C  é {:03.1f}°C .".format(cf, fc))
# print("a temperatura {:03.1f} °F em  °K é {:03.1f}°K .".format(cf, fk))
# print("a temperatura {:03.1f} °F em  °Re é {:03.1f}°Re .".format(cf, fr))

# kc = ck - 273
# kf = ck * 1.8 - 459.7  # (K * 1.8 - 459.7)

# print("a temperatura {:03.1f} °K em  °C é {:03.1f}°C .".format(ck, kc))
# print("a temperatura {:03.1f} °K em  °F é {:03.1f}°F .".format(ck, kf))


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

    c = input("Digite a opção desejada: ")
    d = float(input("Digite o valor da temperatura: "))

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

    else:
        print("Digite a opção certa!")
        menu()
menu()
        
