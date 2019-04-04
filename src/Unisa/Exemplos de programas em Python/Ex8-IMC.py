print ("Vejamos se voce esta baleia...")
peso=float(input("Digite o peso: "))
altura=float(input("Digite a altura: "))
imc=peso/(altura*altura)
print("IMC= ", imc)
if imc < 16:
   print ("Magreza severa")
elif imc > 16 and imc <= 17:
   print ("Magreza moderada!")
elif imc > 17 and  imc <= 18.5:
   print ("Magreza leve")
elif imc > 18.5 and imc <= 25:
   print ("Peso normal")
elif imc > 25 and imc <= 30:
   print ("Sobrepeso")
elif imc > 30 and imc <= 35:
   print ("Obesidade grau I")
elif imc > 35 and imc <= 40:
   print ("Obesidade grau II")
else:
 
   print ("Obesidade grau III")
