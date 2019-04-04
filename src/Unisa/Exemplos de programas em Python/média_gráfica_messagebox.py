# -*- coding: cp1252 -*-

import tkinter
from tkinter import messagebox
      
janela = tkinter.Tk()

janela.title("Sistema Acadêmico")

rotulo_nome = tkinter.Label(janela, text="Nome do aluno:")
rotulo_nome.pack()

nome = tkinter.Entry(janela)
nome.pack()

rotulo_disciplina = tkinter.Label(janela , text="Disciplina:")
rotulo_disciplina.pack()

disciplina = tkinter.Entry(janela)
disciplina.pack()

rotulo_nota1 = tkinter.Label(janela, text="Nota 1:")
rotulo_nota1.pack()

nota1 = tkinter.Entry(janela)
nota1.pack()

rotulo_nota2 = tkinter.Label(janela, text="Nota 2:")
rotulo_nota2.pack()

nota2 = tkinter.Entry(janela)
nota2.pack()

rotulo_nota3 = tkinter.Label(janela, text="Nota 3:")
rotulo_nota3.pack()

nota3 = tkinter.Entry(janela)
nota3.pack()



def calculaMedia():
    alfabeto= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
               "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    
    
    valida1 = nota1.get()
    valida2 = nota2.get()
    valida3 = nota3.get()
    
    if  valida1 in alfabeto or valida2 in alfabeto or valida3 in alfabeto:
        tkinter.messagebox.showinfo("Erro" , "Digite apenas números")

    

    else:
        media = (float(nota1.get()) + float(nota2.get()) + float(nota3.get())) / 3

        if media >= 7:
            tkinter.messagebox.showinfo("Aprovado!" , "O aluno " + nome.get() + " está aprovado na disciplina " + disciplina.get())

        else:
            tkinter.messagebox.showinfo("Reprovado!" , "O aluno " + nome.get() + " está reprovado na disciplina " + disciplina.get())

botao = tkinter.Button(janela , text="Checar", command = calculaMedia)
botao.pack()

janela.mainloop()

        
        
