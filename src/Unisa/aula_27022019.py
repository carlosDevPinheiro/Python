

sal = float(input("Digite o salario base de um especialista nessa função: "))
fundo = sal * 0.08
dec_terceiro = sal
parcela_de_fer = sal / 3

sal_base = sal + fundo + (dec_terceiro / 12) + parcela_de_fer
sal_base1 = sal_base / 160
valor_hora = sal_base1 + (sal_base1 * 0.75)
print("O preço da hora de trabalho é: R$ {:5.2f}  ".format(valor_hora))

horas_previstas = float(input("Digite quantas horas são prevista para conclusão do projeto: "))
preco = valor_hora * horas_previstas
print("Valor do Projeto: R$ {:5.2f}".format(preco))