num = input("Write a integer number: ")
contador = 1
while contador <= num:
    if num%2 == 1:
        contador = contador + 1
        print num, "is prime"
        break
    else:
        print num, "is not prime"
        break