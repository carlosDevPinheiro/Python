
def sub():
    a1 = float(input('Digite sua nota da Substitutiva: '))
    b1 = float(input('Digite sua nota AVG: '))
    media_sub = (a1 + b1) / 2
    if media_sub >= 5:
        print('APROVADO !!')
    else:
        print('Reprovado :( ')
    
    