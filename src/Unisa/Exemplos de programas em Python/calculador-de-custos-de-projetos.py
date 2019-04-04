# -*- coding: cp1252 -*-

sal = float(input("Digite o salário base de um especialista nessa função: "))
fundo = sal + (sal * 1.08)
dec_terceiro = sal
parcela_de_fer = sal/3

sal_base = sal + fundo + (dec_terceiro/12) + parcela_de_fer
sal_base_1 = sal_base/160
valor_hora = sal_base_1 + (sal_base_1*0.75)
print("O preço da hora de trabalho é: ", valor_hora)

horas_previstas = float(input("Digite quantas horas são previstas para conclusão do projeto: "))
preço = valor_hora * horas_previstas
print ("Valor do projeto: ", preço)
