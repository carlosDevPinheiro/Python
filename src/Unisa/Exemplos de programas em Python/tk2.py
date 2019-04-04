from Tkinter import *

class Alterna_Texto:
    
    def __init__(self, toplevel):
        self.frame=Frame(toplevel)
        # Determinando o tamanho da janela no eixo x
        self.frame["padx"]=46
        # Determinando o tamanho da janela no eixo y 
        self.frame["pady"]=5
        self.frame.pack()
        # Geometria do texto exibido
        self.texto=Label(self.frame, text='Clique para mudar o texto')
        self.texto['width']=46
        self.texto['height']=3
        self.texto.pack()
        # Geometria do botao
        self.botao=Button(self.frame,text='Clique')
        self.botao['background']='gray'
        # Associando evento ao botao
        self.botao.bind("<Button-1>", self.muda_texto)
        self.botao.pack()
    
    def muda_texto(self, event):
    # Muda o texto!
        if self.texto['text']=='Clique para mudar o texto':
            self.texto['text']='O texto mudou! Clique para voltar ao texto anterior'
        elif self.texto['text']=='O texto mudou! Clique para voltar ao texto anterior':
            self.texto['text']='Clique para mudar o texto'
        else:
            self.texto['text']=='Clique para mudar o texto'

raiz=Tk()
Alterna_Texto(raiz)
raiz.mainloop()
