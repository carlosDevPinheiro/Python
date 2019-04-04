AVG = float(input("Digite a sua nota da AVG: "))
AVC = float(input("Digite sua nota da AVC: "))
media = ((AVG *0.6) +(AVC*0.4))
print(media)
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
