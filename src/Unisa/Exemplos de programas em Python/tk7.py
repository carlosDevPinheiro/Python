# -*- coding: UTF-8 -*-

from Tkinter import *
import sqlite3

class Agenda:
    def __init__(self, toplevel):
        self.frame1=Frame(toplevel)
        self.frame1.pack()
        self.frame2=Frame(toplevel)
        self.frame2.pack(padx=45)
        self.frame3=Frame(toplevel)
        self.frame3.pack()
        self.frame4=Frame(toplevel)
        self.frame4.pack()
        self.frame5=Frame(toplevel)
        self.frame5.pack()
        self.frame6=Frame(toplevel)
        self.frame6.pack()
        
        fonte1=('Times New Roman','10', 'bold')
        Label(self.frame1, text='Agenda', fg='black', font=('Times New Roman', '14', 'bold'), height=3).pack()
        Label(self.frame2, text='Nome', fg='black', font=('Times New Roman', '12', 'bold'), height=3).pack(side=LEFT)
        self.entra_nome=Entry(self.frame2, width=40, font=fonte1)
        self.entra_nome.pack(side=RIGHT)
        Label(self.frame3, text='Email', fg='black', font=('Times New Roman', '12', 'bold'), height=3).pack(side=LEFT)
        self.entra_email=Entry(self.frame3, width=40, font=fonte1)
        self.entra_email.pack(side=RIGHT)
        self.botao1=Button(self.frame4, font=fonte1, text='Inserir', bg='gray', command=self.botao1)
        self.botao1.pack(side=LEFT)
        self.botao2=Button(self.frame4, font=fonte1, text='Excluir', bg='gray', command=self.botao2)
        self.botao2.pack(side=RIGHT)
        self.botao3=Button(self.frame4, font=fonte1, text='Alterar', bg='gray', command=self.botao3)
        self.botao3.pack(side=RIGHT)
        self.botao4=Button(self.frame4, font=fonte1, text='Pesquisar', bg='gray', command=self.botao4)
        self.botao4.pack(side=RIGHT)
        self.msg=Label(self.frame5, font=fonte1, height=3, text='Nome:')
        self.msg.pack()
        self.msg1=Label(self.frame6, font=fonte1, height=3, text='E-mail:')
        self.msg1.pack()

    def botao1(self):
        for row in self.entra_nome:
            row[0]
        for row in self.entra_email:
            row[1]
        conn=sqlite3.connect('agenda.db')
        cursor=conn.cursor()
        cursor.execute("INSERT INTO Contatos(Nome, Email) VALUES('?','?');", (row[0], row[1]))
        conn.commit()
        conn=conn.close()
        
    def botao2(self):
        conn=sqlite3.connect('agenda.db')
        cursor=conn.cursor()
        cursor.execute("DELETE FROM Contatos WHERE Nome = ?;", (self.entra_nome))
        conn.commit()
        conn=conn.close()

    def botao3(self):
        conn=sqlite3.connect('agenda.db')
        cursor=conn.cursor()
        cursor.execute("UPDATE Contatos SET Nome = ?, Email = ? WHERE Nome = ?;", (self.entra_nome, self.entra_email, self.entra_nome))
        conn.commit()
        conn=conn.close()

    def botao4(self):
        conn=sqlite3.connect('agenda.db')
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM Contatos;")
        for row in cursor:
            row[0], row[1]
        self.msg['text']=row[0]
        self.msg1['text']=row[1]
        conn.commit()
        conn=conn.close()
        
root=Tk()
Agenda(root)
root.mainloop()
