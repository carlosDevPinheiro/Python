# -*- coding: cp1252 -*-

from Tkinter import *

root = Tk()

barra = Scrollbar(root)
texto = Text(root, height=4, width=37)
barra.pack(side=RIGHT, fill=Y)
texto.pack(side=LEFT, fill=Y)
barra.config(command=texto.yview)
texto.config(yscrollcommand=barra.set)

quote = """As armas e os Bar�es assinalados
Que da Ocidental praia Lusitana
Por mares nunca de antes navegados 
Passaram ainda al�m da Taprobana, 
Em perigos e guerras esfor�ados 
Mais do que prometia a for�a humana, 
E entre gente remota edificaram 
Novo Reino, que tanto sublimaram; """

texto.insert(END, quote)

mainloop(  )

