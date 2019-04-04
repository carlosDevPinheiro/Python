# -*- coding: cp1252 -*-

import sys
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Test')

conv_intro =['Ol�!', 'Oi!', 'Fala a�!', 'Pois n�o?', 'O que voc� quer saber?']
conv_des = ['De qual filme voc� gosta?', 'Eu gosto de Star Wars.', 'Algum outro?', 'Tamb�m gosto de Star Trek.']
con_nome = ['Qual o seu nome?', 'Meu nome � Robotildo.']
con_prof = ['Qual sua profiss�o?', 'Eu sou um chatbot.']
con_mora = ['Onde voc� mora?', 'Em um computador.']


bot.set_trainer(ListTrainer)

bot.train(conv_intro)
bot.train(conv_des)
bot.train(con_nome)
bot.train(con_prof)
bot.train(con_mora)

while True:
    quest = input('Voc�: ')
    response = bot.get_response(quest)
    print('Bot: ', response)
    
