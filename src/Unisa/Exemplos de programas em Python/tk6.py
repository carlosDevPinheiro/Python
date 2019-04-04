# -*- coding: cp1252 -*-

from Tkinter import *

root = Tk()

image1 = Text(root, height=20, width=30)
photo=PhotoImage(file='urubu1.gif')
image1.insert(END,'\n')
image1.image_create(END, image=photo)

image1.pack(side=LEFT)

texto = Text(root, height=20, width=50)
scroll = Scrollbar(root, command=texto.yview)
texto.configure(yscrollcommand=scroll.set)
texto.tag_configure('big', font=('Tempus Sans ITC', 20, 'bold'))
texto.tag_configure('color', foreground='black', font=('Tempus Sans ITC', 12, 'bold'))

texto.insert(END,'\nUrubu\n', 'big')
quote = """
Nome cient�fico: Coragyps atratus
Reino: Animalia 
Filo: Chordata 
Classe: Aves 
Ordem: Ciconiiformes 
Fam�lia: Cathartidae 
G�nero: Sarcorhamphus

� uma das aves mais comuns do Brasil,
sendo encontrado tamb�m na regi�o
central dos Estados Unidos e em
praticamente toda a Am�rica do Sul.
Exceto por uma linha mais clara no
final das asas, adultos e jovens s�o
totalmente negros. Costuma planar com
as asas esticadas.
"""
texto.insert(END, quote, 'color')
texto.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)

root.mainloop()
