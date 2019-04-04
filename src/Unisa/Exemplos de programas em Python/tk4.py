# -*- coding: cp1252 -*-

from Tkinter import *
import sqlite3

class Controle_de_Acesso:
    
    def __init__(self,toplevel):
        self.frame1=Frame(toplevel)
        self.frame1.pack()
        self.frame2=Frame(toplevel)
        self.frame2.pack()
        self.frame3=Frame(toplevel)
        self.frame3.pack()
        self.frame4=Frame(toplevel, pady=10)
        self.frame4.pack()
        Label(self.frame1,text='Controle de Acesso', fg='black', font=('Times New Roman', '14', 'bold'), height=3).pack()
        fonte1=('Times New Roman','10', 'bold')
        Label(self.frame3, text='Senha: ', font=fonte1, width=8).pack(side=LEFT)
        self.senha=Entry(self.frame3, width=10, show='*', font=fonte1) # show mostra asteriscos ao invés do caracter digitado
        self.senha.focus_force() # Para o foco começar neste campo
        self.senha.pack(side=LEFT)
        self.confere=Button(self.frame4, font=fonte1, text='Verificar', bg='gray', command=self.conferir)
        self.confere.pack()
        self.msg=Label(self.frame4, font=fonte1, height=3, text='No aguardo...')
        self.msg.pack()

    def conferir(self):
        conn=sqlite3.connect('acesso.db')
        cursor=conn.cursor()
        cursor = conn.execute("SELECT password from SENHA")
        SENHA=self.senha.get()
        # Gravando o resultado da consulta em uma lista
        for row in cursor:
            row[0]
        if row[0]==SENHA:
            self.msg['text']='Acesso liberado'
            self.msg['fg']='darkgreen'
        else:
            self.msg['text']='Acesso negado'
            self.msg['fg']='red'
            self.senha.focus_force()
        conn.close()

root=Tk()
Controle_de_Acesso(root)
root.mainloop()