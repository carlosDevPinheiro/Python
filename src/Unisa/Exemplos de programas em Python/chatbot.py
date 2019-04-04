# -*- coding: cp1252 -*-

import sys
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Test')

conv_intro =['Olá!', 'Oi!', 'Fala aí!', 'Pois não?', 'O que você quer saber?']
conv_des = ['De qual filme você gosta?', 'Eu gosto de Star Wars.', 'Algum outro?', 'Também gosto de Star Trek.']
con_nome = ['Qual o seu nome?', 'Meu nome é Robotildo.']
con_prof = ['Qual sua profissão?', 'Eu sou um chatbot.']
con_mora = ['Onde você mora?', 'Em um computador.']


bot.set_trainer(ListTrainer)

bot.train(conv_intro)
bot.train(conv_des)
bot.train(con_nome)
bot.train(con_prof)
bot.train(con_mora)

while True:
    quest = input('Você: ')
    response = bot.get_response(quest)
    print('Bot: ', response)
    
