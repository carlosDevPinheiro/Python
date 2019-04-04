import media_unisa_lib
nota1 = float(input("Digite a nota da AVC: "))
nota2 = float(input("Digite a nota da AVG: "))
media = media_unisa_lib.media_unisa(nota1, nota2)
print ("Resultado = ", media)
if media >= 6:
    print("Aprovado!")
elif media <=5.999 and media >=5.75:
    print("Aprovado com arredondamento!")
elif media <=5.749 and media >=3:
    print("Prova substitutiva")
    exame = float(input("Digite a nota da substitutiva: "))
    nota_exame = (exame + media) / 2
    if nota_exame > 5:
        print("Aprovado!")
    else:
        print("Reprovado!")
else:
    print("Reprovado!")
