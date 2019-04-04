# -*- coding: cp1252 -*-

from Tkinter import *

class Alterna_Texto:
    
    def __init__(self, toplevel):
        self.frame=Frame(toplevel)
        # Determinando o tamanho da janela no eixo x
        self.frame["padx"]=24
        # Determinando o tamanho da janela no eixo y 
        self.frame["pady"]=24
        self.frame.pack()
        # Geometria do texto exibido
        self.texto=Label(self.frame, anchor='n', font='Arial 12 normal', text='\n \n Pesquisa de satisfação salarial \n \n Clique em "sim" se achar \n que merece um aumento e em \n "não" se achar que seu salário \n está bom')
        self.texto['width']=24
        self.texto['height']=12
        self.texto.pack()
        # Geometria do botao1
        self.botao1=Button(self.frame, font='Arial 12 normal', text='Sim')
        self.botao1['background']='gray'    
        #Associando o evento "passar o mouse" com a funcao muda_botao
        self.botao1.bind("<Motion>", self.muda_botao)
        self.botao1.pack()
        # Geometria do botao2
        self.botao2=Button(self.frame, font='Arial 12 normal', text='Não')
        self.botao2['background']='gray'    
        #Associando o evento "finaliza"
        self.botao2.bind("<Button-1>", self.finaliza)
        self.botao2.pack()
    
    def muda_botao(self, event):
    # Muda o botao
        if self.botao1['text']=='Sim':
            self.botao1.pack(side=LEFT)
            self.botao1['text']='Ih!'
        elif self.botao1['text']=='Ih!':
            self.botao1.pack(side=RIGHT)
            self.botao1['text']='Olé!'
        elif self.botao1['text']=='Olé!':
            self.botao1.pack(side=LEFT)
            self.botao1['text']='Ih!'            
        self.botao1.pack()

    def finaliza(self, event):
        self.texto['text']='\n \n Sua resposta foi encaminhada \n para o RH. \n \n São pessoas como você que \n engrandecem nossa empresa. \n \n \n Agora volte ao trabalho!'        
        self.botao1.destroy()
        self.botao2.destroy()
        
raiz=Tk()
Alterna_Texto(raiz)
raiz.mainloop()
