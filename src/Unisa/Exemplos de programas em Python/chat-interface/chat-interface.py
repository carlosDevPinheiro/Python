# -*- coding: cp1252 -*-
import random
import tkinter as tk

root = tk.Tk()
user_input = tk.Entry(root)
user_input.pack()

conv_intro = ['Ol�!', 'Oi!', 'Fala ai!']
conv = ['De qual filme voc� gosta?', 'Eu gosto de Star Wars.']
nome = ['Qual o seu nome?', 'Meu nome � Robotildo.']
con_prof = ['Qual sua profiss�o?', 'Eu sou um chatbot.']
con_mora = ['Onde voc� mora?','Em um computador']
huh = "Eu n�o entendi o que voc� disse"

def cb():
    user_text = user_input.get()
    if user_text in conv_intro:
        bot_text = random.choice(conv_intro)
    elif user_text in conv:
        bot_text = random.choice(conv)
    elif user_text in nome:
        bot_text = random.choice(nome)
    elif user_text in con_prof:
        bot_text = random.choice(con_prof)
    else:
        bot_text = huh
    output.config(text=bot_text)

button = tk.Button(root, text="Chat... Digite uma Pergunta ", command=cb)
button.pack()

output = tk.Label(root, text='')
output.pack()

tk.mainloop()
