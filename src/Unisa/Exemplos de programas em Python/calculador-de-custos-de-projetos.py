# -*- coding: cp1252 -*-

sal = float(input("Digite o sal�rio base de um especialista nessa fun��o: "))
fundo = sal + (sal * 1.08)
dec_terceiro = sal
parcela_de_fer = sal/3

sal_base = sal + fundo + (dec_terceiro/12) + parcela_de_fer
sal_base_1 = sal_base/160
valor_hora = sal_base_1 + (sal_base_1*0.75)
print("O pre�o da hora de trabalho �: ", valor_hora)

horas_previstas = float(input("Digite quantas horas s�o previstas para conclus�o do projeto: "))
pre�o = valor_hora * horas_previstas
print ("Valor do projeto: ", pre�o)
