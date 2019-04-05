 import sys

def metodo1(param1):
    print("O metodo 1 recebeu o parametro '{0}'".format(param1))

def metodo2(param1, param2):
    print("O metodo 2 recebeu os parametros '{0}' e '{1}'".format(param1, param2))

qual_metodo_usar = sys.argv[1]

if qual_metodo_usar == "metodo1":
    parametro1 = sys.argv[2]
    metodo1(parametro1)
elif qual_metodo_usar == "metodo2":
    parametro1 = sys.argv[2]
    parametro2 = sys.argv[3]
    metodo2(parametro1, parametro2)
else:
    print("Metodo desconhecido")