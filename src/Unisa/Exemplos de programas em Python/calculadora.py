#!/usr/bin/python
# -*- coding: cp1252 -*-

"""
Autores:             Vinicius Rodrigues da Cunha Perallis
                     
                     
Data:                19/04/2006
                     20/04/2006
                     22/04/2006
                     23/04/2006
                     24/04/2006
                     25/04/2006
                     26/04/2006
                     28/04/2006
                     29/04/2006
                     01/04/2006
                     
Projeto:             Calculadora Comercial(imita uma fita de impress�o)
Materia:             Linguagens de Programa��o Comerciais
Interpretador:       Python 2.4.1

Sistemas Compativeis:Windows,Linux,Solaris,etc...

Dispon�vel:          http://www.pythonbrasil.com.br

Contato:             perallis@rc.unesp.br
"""


#Importa todas fun��es do modulo Tkinter
from Tkinter import *
#Importa as fun��es seno,cossseno,tangente,sqrt que 
#� usada pela calculadora
from math import *


#Classe Principal que executa o aplicativo Calculadora
class Calculadora:
    
    #m�todo construtor para iniciar a aplica��o      
    def __init__(self,parent):
        
        self.myapp=parent
        self.myapp.title("Calculadora - Phy")
        #cria o menu
        self.menubar = Menu(self.myapp)
        self.myapp.config(menu=self.menubar)
        # adiciona o file ao menu
        file = Menu(self.menubar)
        file.add_command(label='Sair',command=self.sair)
        self.menubar.add_cascade(label='Arquivo', \
                                 underline=0, menu=file)
         

        # Adiciona o help ao menu
        help = Menu(self.menubar)
        help.add_command(label='Autores',command=self.autores)
        help.add_command(label='Licen�a',command=self.licenca)
        help.add_command(label='Como usar?',\
                         command=self.comousar)
        self.menubar.add_cascade(label='Ajuda', underline=0, \
                                 menu=help)
 
        #Cria o frame principal
        self.geral=Frame(self.myapp,bg="gray")
        self.geral.pack()
        
        #Cria os frames nescess�rios para a disposi��o
        #dos widgets
        self.fexibir=Frame(self.geral,bg="gray")
        self.fzero=Frame(self.geral,bg="gray")
        self.fum=Frame(self.geral,bg="gray")
        self.fdois=Frame(self.geral,bg="gray")
        self.ftreis=Frame(self.geral,bg="gray")
        self.fquatro=Frame(self.geral,bg="gray")
        self.fcinco=Frame(self.geral,bg="gray")

        #Caixa de texto, que servir� para mostrar os
        #n�meros
        self.visor=Entry(self.fexibir,width=35,bg="white",\
                         fg="blue",justify="right")
        self.visor.insert(INSERT,"0,") 

        #Este trecho de c�digo � necess�rio para criar
        #os grupos dos bot�es radio
        self.decimais=IntVar()
        self.habilita=IntVar()
        self.decimais=1
        self.habilita=2
        
        #Bot�es de r�dio , para opc�o do n�mero de
        #casas decimais
        self.duascasas=Radiobutton(self.fexibir,\
                                   text="2 casas",\
                                   bg="gray",\
                                   variable=self.decimais, \
                                   command=lambda \
                                   casadec="%.2f": \
                                   self.mudcasadec(casadec))
        self.quatrocasas=Radiobutton(self.fexibir,\
                                     text="4 casas",\
                                     value=3,\
                                     variable=self.decimais, \
                                     bg="gray",command=lambda \
                                           casadec="%.4f": \
                                     self.mudcasadec(casadec))
        self.infinitascasas=Radiobutton(self.fexibir,\
                                        text="... casas ",\
                                                variable=self.decimais,\
                                        value=4,bg="gray",\
                                        command=lambda \
                                                casadec="%f": \
                                        self.mudcasadec(casadec))  

        #Frame Criado para inserir os bot�es de radio
        #habilita/desabilita
        self.festado=Frame(self.geral,bg="gray")
        self.festado.pack(side="bottom")

        #Bot�es de r�dio, para habilitar/desabilitar a
        #fita de impress�o
        self.ativado=Radiobutton(self.festado,text="Ativar",\
                                 bg="gray",\
                                 variable=self.habilita, \
                                 command=lambda : \
                                 self.habilitar(h))
        self.desativado=Radiobutton(self.festado,text="Desativar",\
                                    value=2,\
                                    variable=self.habilita,\
                                    bg="gray",command=lambda h=2: \
                                    self.habilitar(h))

        #Espa�o para melhor posicionar os bot�es habilita/desabilita
        self.espaco=Label(self.festado,text="                        \
                                                          ",bg="gray")
        self.espaco.pack(side="left") 
        
        #Exibe os Bot�es de r�dio , para habilitar ou desabilitar
        #a fita 
        self.ativado.pack(side="left",padx=12,anchor=W)
        self.desativado.pack(side="left",padx=4,anchor=W)
        
        
        # Insere a caixa de Texto que ser� utilizada para
        #fazer a fita de impress�o
        self.ffita=Frame(self.geral)
        self.ffita.pack(side="right",padx=15,pady=5)
        self.sb=Scrollbar(self.ffita)
        self.fita=Text(self.ffita,width=23,height=16,\
                       bg="white",\
                       yscrollcommand=self.sb.set,\
                       relief="ridge")
        self.sb["command"] = self.fita.yview
        self.fita.pack(side="left",padx=0)
        self.sb.pack(side="right",fill=Y)
        
        
        ## WIDGETS NO FRAME ZERO #####################
        #Bot�o para reiniciar a calculadora
        self.c=Button(self.fzero,text="C",fg="red",\
                      width=7,command=self.zera)
        #Bot�o para limpar apenas o que est� no visor 
        self.ce=Button(self.fzero,text="CE",fg="red",\
                       width=7,command=self.zeraprim)
        #Botao Backspace
        self.back=Button(self.fzero,text="Backspace",\
                         fg="red",width=10,\
                         command=self.volta)
        #Label para organizar o programa
        self.v=StringVar()
        self.v.set("         ")
        self.space1=Label(self.fzero,bg="gray",\
                          textvariable=self.v,\
                          relief="groove")
        ##############################################
        

       
        ## WIDGETS NO FRAME UM #######################
        self.mc=Button(self.fum,text="MC",fg="red",\
                       width=4,command=lambda opm='MC': \
                       self.memoria(opm))
        self.sete=Button(self.fum,text="7",width=4,\
                         command=lambda n=7:\
                         self.write_visor(n))
        self.oito=Button(self.fum,text="8",width=4,\
                         command=lambda n=8: \
                         self.write_visor(n))
        self.nove=Button(self.fum,text="9",width=4,\
                         command=lambda n=9: \
                         self.write_visor(n))
        self.div=Button(self.fum,text="/",fg="red",\
                        width=4, command=lambda sin='/': \
                        self.op(sin))
        self.sqrt=Button(self.fum,text="sqrt",width=4,\
                         fg="blue",command=lambda \
                         n='sqrt': self.write_visor(n))
        ##############################################

        ## WIDGETS NO FRAME DOIS #####################
        self.mr=Button(self.fdois,text="MR",fg="red",\
                       width=4,command=lambda opm='MR': \
                       self.memoria(opm))
        self.quatro=Button(self.fdois,text="4",width=4,\
                           command=lambda n=4: \
                           self.write_visor(n))
        self.cinco=Button(self.fdois,text="5",width=4,\
                          command=lambda n=5: \
                          self.write_visor(n))
        self.seis=Button(self.fdois,text="6",width=4,\
                         command=lambda n=6: \
                         self.write_visor(n))
        self.mult=Button(self.fdois,text="*",fg="red",\
                         width=4 ,command=lambda sin='*': \
                         self.op(sin))
        self.umx=Button(self.fdois,text="1/x",width=4,\
                        fg="blue",command=lambda n='1/x'\
                        : self.write_visor(n))
        ###############################################

        ## WIDGETS NO FRAME TREIS ######################
        self.ms=Button(self.ftreis,text="MS",fg="red",\
                       width=4,command=lambda opm='MS': \
                       self.memoria(opm))
        self.um=Button(self.ftreis,text="1",width=4,\
                       command=lambda n=1:\
                       self.write_visor(n) )
        self.dois=Button(self.ftreis,text="2",\
                         width=4,command=lambda n=2: \
                         self.write_visor(n))
        self.tres=Button(self.ftreis,text="3",width=4,\
                         command=lambda n=3: self.write_visor(n))
        self.menos=Button(self.ftreis,text="-",fg="red",\
                          width=4, command=lambda sin='-': \
                          self.op(sin) )
        self.porcentagem=Button(self.ftreis,text="%",\
                                width=4,fg="blue",\
                                command=lambda n='%': \
                                self.write_visor(n))
        #################################################

        ## WIDGETS NO FRAME QUATRO#########################
        self.mmais=Button(self.fquatro,text="M+",fg="red",
                          width=4,command=lambda opm='M+': \
                          self.memoria(opm))
        self.zero=Button(self.fquatro,text="0",width=4,\
                         command=lambda n=0: \
                         self.write_visor(n))
        self.virg=Button(self.fquatro,text=",",width=4,\
                         command=lambda n='.': \
                         self.write_visor(n))
        self.maismenos=Button(self.fquatro,fg="blue",text="+/-",\
                              width=4, command=lambda n=-1: \
                              self.write_visor(n))
        self.mais=Button(self.fquatro,fg="red",text="+",width=4, \
                         command=lambda sin='+': self.op(sin))
        self.igual=Button(self.fquatro,text="=",fg="red",width=4,\
                          command=lambda sin="=": self.op(sin))
        ####################################################

        ## WIDGETS NO FRAME CINCO#########################
        self.mmenos=Button(self.fcinco,text="M-",fg="red",
                          width=4,command=lambda opm='M-': \
                          self.memoria(opm))
        self.centena=Button(self.fcinco,fg="brown",text="00",\
                            width=4, command=lambda n=100: \
                            self.write_visor(n))
        self.milhares=Button(self.fcinco,fg="brown",text="000",\
                             width=4, command=lambda n=1000: \
                             self.write_visor(n))
        self.mmenos=Button(self.fcinco,text="M-",fg="red",
                          width=4,command=lambda opm='M-': \
                          self.memoria(opm))
        self.seno=Button(self.fcinco,text="sen",fg="brown",
                          width=4,command=lambda n='sen': \
                          self.write_visor(n))
        self.cosseno=Button(self.fcinco,text="cos",fg="brown",
                          width=4,command=lambda n='cos': \
                          self.write_visor(n))
        self.tangente=Button(self.fcinco,text="tan",fg="brown",
                          width=4,command=lambda n='tan': \
                          self.write_visor(n))
        ####################################################
        
         
        #Frame fexibir   
        self.fexibir.pack(padx=10,pady=10)
       
        self.visor.pack(ipadx="3")
        self.duascasas.pack(side="left",padx=12,anchor=W)
        self.quatrocasas.pack(side="left",padx=4,anchor=W)
        self.infinitascasas.pack(side="left",padx=4,anchor=W)
   
        #Frame fzero  
        self.fzero.pack()
        
        self.space1.pack(side="left",padx="5")
        self.c.pack(side="left",pady="5",padx="3")
        self.ce.pack(side="left",pady="5",padx="3")
        self.back.pack(side="left",pady="5",padx="3")
        

        #Frame fum   
        self.fum.pack(padx=2)
        
        self.mc.pack(side="left",padx=4,pady=2)
        self.sete.pack(side="left",padx=2,pady=2)
        self.oito.pack(side="left",padx=2,pady=2)
        self.nove.pack(side="left",padx=2,pady=2)
        self.div.pack(side="left",padx=2,pady=2)
        self.sqrt.pack(side="left",padx=2,pady=2)
        
        #Frame fdois   
        self.fdois.pack(padx=2)

        self.mr.pack(side="left",padx=4,pady=2)
        self.quatro.pack(side="left",padx=2,pady=2)
        self.cinco.pack(side="left",padx=2,pady=2)
        self.seis.pack(side="left",padx=2,pady=2)
        self.mult.pack(side="left",padx=2,pady=2)
        self.umx.pack(side="left",padx=2,pady=2)

        #Frame ftreis 
        self.ftreis.pack(padx=2)

        self.ms.pack(side="left",padx=4,pady=2)
        self.um.pack(side="left",padx=2,pady=2)
        self.dois.pack(side="left",padx=2,pady=2)
        self.tres.pack(side="left",padx=2,pady=2)
        self.menos.pack(side="left",padx=2,pady=2)
        self.porcentagem.pack(side="left",padx=2,pady=2)

        #Frame fquatro   
        self.fquatro.pack(padx=2)

        self.mmais.pack(side="left",padx=4,pady=2)
        self.maismenos.pack(side="left",padx=2,pady=2)
        self.zero.pack(side="left",padx=2,pady=2)
        self.virg.pack(side="left",padx=2,pady=2)
        self.mais.pack(side="left",padx=2,pady=2)
        self.igual.pack(side="left",padx=2,pady=2)

        #Frame fcinco   
        self.fcinco.pack(padx=2)

        self.mmenos.pack(side="left",padx=4,pady=2)
        self.centena.pack(side="left",padx=2,pady=2)
        self.milhares.pack(side="left",padx=2,pady=2)
        self.seno.pack(side="left",padx=2,pady=2)
        self.cosseno.pack(side="left",padx=2,pady=2)
        self.tangente.pack(side="left",padx=2,pady=2)
         
        
        #  Variais booleanas da classe 
        self.z=0
        self.w=1
        self.i=0
        self.ty=0
        self.prim=0
        self.h=0
        self.sa=0
        self.sinais=1
        self.i=0
        self.prim_op=0
        
        #Controle do n�mero de vezes que o usu�rio clica
        #na v�rgula
        self.ponto=1        
        
        #Vari�veis usadas para guardar os valores do visor
        self.atual=0
        self.num=0
        self.mem=0


        self.casadec="%.2f"

    #metodo para mudar o numero de casas decimais       
    def mudcasadec(self,casadec):
        self.casadec=casadec
   

    #-#--------------- Fun��o aritm�tica op -------------#-#        
    def op(self,sin):
        if (self.w==0) and self.prim_op==1:
            self.num=float(self.visor.get())
            self.atual=float(self.visor.get())
            self.fita.insert(INSERT,self.num)
            self.sinal=sin
            self.w=1
            self.z=1
            self.i=0 
            self.ty=1
            self.divi=0
            self.sinais=1
            self.prim=1
            self.ponto=1
            if self.prim==0:
                self.ty=1
                
        elif self.prim_op==1:   
            
            if sin=="=" and self.i==1 and self.ty==1: 
                self.sinais=1
                
            if sin!="=" and self.ty==1:
                self.sinal=sin
                self.sinais=0
                self.atual=float(self.visor.get())
                
            if self.ty==0:
                self.atual=float(self.visor.get())
                           
            if self.sa==1 and self.ty==1:
                self.num=float(self.visor.get())
                self.sa=0
                
            if self.sinal=='+' and self.sinais==1:
                self.num=self.num + self.atual
                self.i=0
            elif  self.sinal=='-' and self.sinais==1:
                self.num=self.num - self.atual
            elif  self.sinal=='/' and self.sinais==1 and \
                 self.atual!=0:
                self.i=0
                self.num=self.num / self.atual
            elif  self.sinal=='/' and self.atual==0 and \
                 self.sinais==1:
                self.zera()        
                self.visor.delete(0,END)
                self.visor.insert(INSERT,"Imposivel dividir")
                self.divi=1
                self.sinais=0
            elif  self.sinal=='*' and self.prim==1 and \
                 self.sinais==1:
                self.i=0
                self.num=self.num * self.atual
            
            if self.divi==0:
                self.visor.delete(0,END)
                self.visor.insert(END,self.casadec %self.num)
                self.prim=1
            if (self.divi==0 and self.ty==0) or self.sinais==1:
                
                self.fita.insert(INSERT,"\n"+self.sinal)
                self.fita.insert(INSERT,"\n"+str(self.atual))
                self.fita.insert(INSERT,"\n"+"=")
                self.fita.insert(INSERT,"\n "+\
                                 self.casadec %self.num)

            if sin!="=" and sin!=self.sinal and self.ty==0:
                self.sinais=0
                self.sinal=sin
                self.sinal=sin
                                                    
            self.ty=1
            self.i=0
            self.w=1
            self.z=1
            self.div=0
            self.sinais=1
            self.ponto=1
    #-#--------------  Fim da fun��o aritm�tica op ---------#-#



    #+#------- Fun��o para escrever os numeros no visor ----#+#       
    def write_visor(self,n):
        if (self.z==1) and n!=-1 and n!="1/x" and  n!="sqrt" \
           and  n!="%" and n!='.' and n!=100 and n!=1000 \
           and n!="sen" and n!="cos" \
           and n!="tan":
            if self.i==0: 
                 self.visor.delete(0,END)         
          
            self.visor.insert(INSERT,n)
            self.w=1
            self.z=1
            self.i=1
            self.ty=0
            self.prim=1
            self.i=1
            self.prim_op=1
            
        elif self.z==0 and n!=-1 and n!="1/x" and  n!="sqrt" \
             and  n!="%" and n!='.'and n!=100 and n!=1000 \
             and n!="sen" and n!="cos" \
             and n!="tan":
            if self.i==0:
                self.visor.delete(0,END)         
            self.visor.insert(INSERT,n)
            
            self.w=0
            self.i=1
            self.ty=0
            self.i=1
            self.prim_op=1

        elif  n==-1 and self.prim_op==1:
            self.la=(float(self.visor.get())*(-1))
            self.visor.delete(0,END)
            self.visor.insert(END,self.casadec %self.la)
            if self.ty==1:
                self.fita.insert(INSERT,"\n"+"*(-1)")
                self.fita.insert(INSERT,"\n"+"=")
                self.fita.insert(INSERT,"\n "+\
                                 self.casadec %self.la)
            self.sa=1
            self.i=0
            self.prim_op=1
          

        elif  n=="1/x" and self.prim_op==1:
            try:
                self.la=float(1/float(self.visor.get())) 
                self.visor.delete(0,END)
                self.visor.insert(END,self.casadec %self.la)
                if self.ty==1:
                    self.fita.insert(INSERT,"**(-1)")
                    self.fita.insert(INSERT,"\n"+"=")
                    self.fita.insert(INSERT,"\n "+\
                                     self.casadec %self.la)
                self.sa=1
                self.i=0
            except:
                 self.visor.delete(0,END)
        
        elif  n=="sqrt" and self.prim_op==1:
            try:    
                self.la=sqrt(float(self.visor.get()))
                self.visor.delete(0,END)
                self.visor.insert(END,self.casadec %self.la)
                if self.ty==1:
                    self.fita.insert(INSERT,"\n"+"sqrt")
                    self.fita.insert(INSERT,"\n"+"=")
                    self.fita.insert(INSERT,"\n "+\
                                     self.casadec %self.la)
                    
                self.sa=1
                self.i=0
            except:
                self.zera()
                self.visor.delete(0,END)
                self.visor.insert(END,\
                                  "Valor invalido para fun��o")

        elif  n=="sen" and self.prim_op==1:
            try:    
                self.la=sin((float(self.visor.get())/180)*pi)
                self.visor.delete(0,END)
                self.visor.insert(END,self.casadec %self.la)
                if self.ty==1:
                    self.fita.insert(INSERT,"\n"+"sen")
                    self.fita.insert(INSERT,"\n"+"=")
                    self.fita.insert(INSERT,"\n " \
                                     +self.casadec %self.la)
                self.sa=1
                self.i=0
            except:
                self.zera()
                self.visor.delete(0,END)
                self.visor.insert(END,\
                                  "Valor invalido para fun��o")
                
        elif  n=="cos" and self.prim_op==1:
            try:
               
                self.la=cos((float(self.visor.get())/180)*pi)
                self.visor.delete(0,END)
                self.visor.insert(END,self.casadec %self.la)
                if self.ty==1:
                    self.fita.insert(INSERT,"\n"+"cos")
                    self.fita.insert(INSERT,"\n"+"=")
                    self.fita.insert(INSERT,"\n "\
                                     +self.casadec %self.la)
                self.sa=1
                self.i=0
            except:
                self.zera()
                self.visor.delete(0,END)
                self.visor.insert(END,"Valor invalido para fun��o")
                
        elif  n=="tan" and self.prim_op==1:
            try:    
                self.la=tan((float(self.visor.get())/180)*pi)
                self.visor.delete(0,END)
                self.visor.insert(END,self.casadec %self.la)
                if self.ty==1:
                    self.fita.insert(INSERT,"\n"+"tan")
                    self.fita.insert(INSERT,"\n"+"=")
                    self.fita.insert(INSERT,"\n "\
                                     +self.casadec %self.la)
                self.sa=1
                self.i=0
            except:
                self.zera()
                self.visor.delete(0,END)
        
        elif  n=="%" and self.ty==0 and self.prim_op==1 \
             and self.z==1:
            self.perc=float(self.visor.get())
            self.la=self.num*(float(self.visor.get()))/100
            self.visor.delete(0,END)
            self.visor.insert(END,self.casadec %self.la)
            if self.ty==1:
                self.fita.insert(INSERT,"\n"+"*")
                self.fita.insert(INSERT,"\n"+\
                                 str(self.perc/100))
                self.fita.insert(INSERT,"\n"+"%")
                self.fita.insert(INSERT,"\n"+"=")
                self.fita.insert(INSERT,"\n "+\
                                 self.casadec %self.la)
            self.sa=1
            self.i=1

        elif  n=="%" and self.ty==1 and self.prim_op==1 \
             and self.z==1:
            self.perc=float(self.visor.get())
            self.la=((float(self.visor.get()))*\
                     (float(self.visor.get())))/100
            self.visor.delete(0,END)
            self.visor.insert(END,self.casadec %self.la)
            if self.ty==1:
                self.fita.insert(INSERT,"\n"+"*")
                self.fita.insert(INSERT,"\n"+ \
                                 str(self.perc/100))
                self.fita.insert(INSERT,"\n"+"=")
                self.fita.insert(INSERT,"\n "+\
                                 self.casadec %self.la)
            self.sa=1
            self.i=1

        elif  n=="%" and self.ty==0 and self.prim_op==1 \
             and self.z==0:
            self.perc=float(self.visor.get())
            self.la=((float(self.visor.get()))*(0))/100
            self.visor.delete(0,END)
            self.visor.insert(END,self.casadec %self.la)
            if self.ty==0:
                self.fita.insert(INSERT,"\n"+"*")
                self.fita.insert(INSERT,"\n"+str(0/100))
                self.fita.insert(INSERT,"\n"+"=")
                self.fita.insert(INSERT,"\n "\
                                 +self.casadec %self.la)
            self.sa=1
            self.i=1


        elif n=='.' and self.ponto==1:      
            self.visor.insert(INSERT,n)
            if self.z==0:
                self.fita.insert(INSERT,n)
            self.ponto=0

        
        elif  n==100 and self.prim_op==1:
            try:    
                self.la=(float(self.visor.get()))*n
                self.visor.delete(0,END)
                self.visor.insert(END,self.casadec %self.la)
                if self.ty==1:
                    self.fita.insert(INSERT,"\n"+"*100")
                    self.fita.insert(INSERT,"\n"+"=")
                    self.fita.insert(INSERT,"\n "\
                                     +self.casadec %self.la)
                self.sa=1
                self.i=1
            except:
                self.zera()
                self.visor.delete(0,END)
                self.visor.insert(END,\
                                  "Valor invalido para fun��o")

        elif  n==1000 and self.prim_op==1:
            try:    
                self.la=(float(self.visor.get()))*n
                self.visor.delete(0,END)
                self.visor.insert(END,self.casadec %self.la)
                if self.ty==1:
                    self.fita.insert(INSERT,"\n"+"*1000")
                    self.fita.insert(INSERT,"\n"+"=")
                    self.fita.insert(INSERT,"\n "\
                                     +self.casadec %self.la)
                self.sa=1
                self.i=1
            except:
                self.zera()
                self.visor.delete(0,END)
                self.visor.insert(END,"Valor invalido para fun��o")
    #-#--------- Fim da fun��o write_visor ------------#-#


    
    #+#-------Fun��o para manipular a mem�ria----------#+#

    def memoria(self,opm):
        if opm=="MC":
            self.mem=0
            self.v.set("         ")
            
        elif opm=="MR":
             self.visor.delete(0,END)         
             self.visor.insert(INSERT,str(self.mem))
             self.i=0
             self.ty=0
        elif opm=="MS":
            self.mem=float(self.visor.get())
            self.v.set("   M   ")
            self.i=0
        elif opm=="M+":
            self.mem=self.mem + float(self.visor.get())
            self.v.set("   M   ")
            self.i=0
        elif opm=="M-":
            self.mem=self.mem - float(self.visor.get())
            self.v.set("   M   ")
            self.i=0
    #-#------------------- Fim Memoria ---- -------------#-#


    #+#------- Fun��o para reiniciar a calculadora ------#+#     
    def zera(self):
        self.z=0
        self.w=1
        self.atual=0
        self.i=0
        self.ty=0
        self.num=0
        self.prim=0
        self.h=0
        self.sa=0
        self.sinais=1
        self.i=0
        self.prim_op=0
        self.ponto=1
        self.visor.delete(0,END)
        self.visor.insert(INSERT,0)
        self.fita.delete('1.0','90.0')
    #-#----------------- Fim da fun��o zera -------------#-#


    #+#-------------------- Fun��o CE -------------------#+#    
    def zeraprim(self):
        if  self.ty==0:
            self.visor.delete(0,END)
            self.visor.insert(INSERT,0)
            self.i=0
            
        else:
            self.zera()
    #-#----------------- Fim da fun��o CE ----------------#-#
        
        
    #+#-------------- Fun��o volta(Backspace) ------------#+#    
    def volta(self):
        if self.ty==0 and self.prim_op==1:
            tam = len(self.visor.get())
            self.visor.delete(tam-1,tam)                
    #-#----------------- Fim da fun��o volta--------------#-#


    #+#------------------- Fun��o Habilita ---------------#+#    
    def habilitar(self,h):
        if h==2:
            self.fita["state"]="disabled"
        if h==1:
            self.fita["state"]="normal"
    #-#---------------- Fim da fun��o Habilita-------------#-#


    #+#-----------------Janela Sobre(Autores)--------------#+#
    def autores(self):
                s = """
Autores:
Vin�cius Rodrigues da Cunha Perallis
UNESP, Rio Claro
Instituto de Geoci�ncias e Ci�ncias Exatas IGCE 
Email: perallis@rc.unesp.br
                """
                message_box = Toplevel()
                message_box.title("Autores:")
                message_box_fr = Frame(message_box)
                message_box_fr.pack(expand=0, fill=BOTH)
                message_lb = Label(message_box_fr, text = s,\
                                   justify="left")
                message_lb.grid(row=0, column=0)
                quitbutton = Button(message_box_fr,\
                                    text = 'Fechar', \
                                    command=message_box.destroy,\
                                    borderwidth=1)
                quitbutton.grid(row=1, column=0)
    #-#----------------Fim de Janela Sobre(Autores)----------#-#


    #+#------------------Janela Sobre(Licenca)---------------#+#
    def licenca(self):
                s = """
Licen�a: O uso deste programa � gratuito.
              Seu c�digo pode ser melhorado, ou alterado
              conforme a nescessidade do usu�rio

                    Email: perallis@rc.unesp.br
                """
                message_box = Toplevel()
                message_box.title("Licen�a:")
                message_box_fr = Frame(message_box)
                message_box_fr.pack(expand=0, fill=BOTH)
                message_lb = Label(message_box_fr, text = s,\
                                  justify="left")
                message_lb.grid(row=0, column=0)
                quitbutton = Button(message_box_fr,\
                                    text = 'Fechar', \
                                    command=message_box.destroy,\
                                    borderwidth=1)
                quitbutton.grid(row=1, column=0)
    #-#-----------Fim de Janela Licenca(Autores)-------------#-#


    #+#------------------Janela ComoUsar(Licenca)------------#+#
    def comousar(self):
                s = """
Como Usar: Esta � uma calculadora que opera como qualquer
                  outra calculadora(semelhante a do windows).
                  A unica diferen�a,� que ela imita uma fita
                  de impress�o, como uma calculadora comercial

                       Email: perallis@rc.unesp.br
                  """
                message_box = Toplevel()
                message_box.title("Como usar?")
                message_box_fr = Frame(message_box)
                message_box_fr.pack(expand=0, fill=BOTH)
                message_lb = Label(message_box_fr, text = s,\
                                   justify="left")
                message_lb.grid(row=0, column=0)
                quitbutton = Button(message_box_fr, \
                                    text = 'Fechar', \
                                    command=message_box.destroy,\
                                    borderwidth=1)
                quitbutton.grid(row=1, column=0)
    #-#----------------Fim de Janela ComoUsar(Autores)-------#-#


    #+#-------------- Fun��o para sair do programa ----------#+#
    def sair(self):
        root.destroy()
    #-#--------------------- Fim Fn��o sair -----------------#-#

            
# root Intacia-se pela classe Tk() e inicia a aplica��o       
root=Tk()
aplicativo=Calculadora(root)
root.mainloop()