
# -*- encoding: utf-8 -*-

import os       # usar comando do sistema operacional, exemplo 'cls' do cmd
import sys      # usar o sys do python, progrmas da lib
import string   # usar caracteres maiusculos
import sqlite3  # banco de dados SQLite


def EscolhaUsuario():
    os.system("cls") # usando comando para limpar tela do cmd 

    print ("===================================")
    print ("======= Agenda de Contatos ========")
    print ("===================================")
    print ("Escolha a alternativa desejada: ")
    print ("1 - Criar banco de dados")
    print ("2 - Cadastrar")
    print ("3 - Alterar")
    print ("4 - Consultar")
    print ("5 - Excluir")
    print ("6 - Mostrar Todos")
    print ("7 - Sair")

    escolha = input("digite sua escolha: ")
    if escolha == '1':
        criar_banco()
    elif escolha == '2':
        cadastrar()
    elif escolha == '3':
        alterar()
    elif escolha == '4':
        consultar()
    elif escolha == '5':
        excluir()
    elif escolha == '6':
        mostrar_todos()
    elif escolha == '7':
        sys.exit()
    else:
        print("Escolha uma das alternativas acima: ")
        EscolhaUsuario()

def criar_banco():   
    conn = sqlite3.connect('agenda.carlos.db')
    ponteiro = conn.cursor()   
    ponteiro.execute(""" CREATE TABLE IF NOT EXISTS Contatos(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome VARCHAR NOT NULL, telefone VARCHAR NOT NULL)""")
    conn.close()
    EscolhaUsuario()

def cadastrar():
    n = input("digite nome do contato: ")
    t = input("digite telefone do contato: ")
    
    conn = sqlite3.connect('agenda.carlos.db')
    ponteiro = conn.cursor()   
    ponteiro.execute("""INSERT INTO Contatos(nome, telefone) VALUES(?, ?) """, (n, t))
    conn.commit()
    c = input("Digite 8 para finalizar o cadastro e voltar ao menu pressione qualquer tecla para encerrar: ")
    if c == '8':
        conn.close()
        EscolhaUsuario()
    else:
        conn.close()
        sys.exit()


def mostrar_todos():
    conn = sqlite3.connect('agenda.carlos.db')
    ponteiro = conn.cursor()
    ponteiro.execute("""SELECT * FROM Contatos""")
    
    for linha in ponteiro.fetchall():
        print("id: ",linha[0])
        print("Nome: ",linha[1])
        print("Telefone: ",linha[2])
    
    c = input("Digite 8 para finalizar o cadastro e voltar ao menu pressione qualquer tecla para encerrar: ")
    if c == '8':
        conn.close()
        EscolhaUsuario()
    else:
        conn.close()
        sys.exit() 

def alterar():
    id = int( input("Digite o id do contato: "))
    novo_telefone = input("Digite novo numero de telefone: ")
    conn = sqlite3.connect('agenda.carlos.db')
    ponteiro = conn.cursor()
    ponteiro.execute("""UPDATE Contatos SET telefone= ? WHERE id = ? """,(novo_telefone, id))
    conn.commit()
    c = input("Digite 8 para finalizar o cadastro e voltar ao menu pressione qualquer tecla para encerrar: ")
    if c == '8':
        conn.close()
        EscolhaUsuario()
    else:
        conn.close()
        sys.exit() 

def consultar():
    id = input("Digite o id a ser consultado: ")   
    conn = sqlite3.connect('agenda.carlos.db')
    ponteiro = conn.cursor()
    ponteiro.execute("""SELECT * FROM Contatos WHERE id = ?""",(id))
    for linha in ponteiro.fetchall():
        print("ID: ", linha[0])
        print("Nome: ", linha[1])
        print("Telefone: ", linha[2])
    c = input("Digite 8 para encerrar a consulta e voltar ao menu ou qualquer coisa para encerrar o programa: ")
    if c == '8':
        conn.close()
        EscolhaUsuario()
    else:
        conn.close()
        sys.exit() 

def excluir():
    id = input("Digite o id a ser consultado: ")   
    conn = sqlite3.connect('agenda.carlos.db')
    ponteiro = conn.cursor()
    ponteiro.execute("""DELETE FROM Contatos WHERE id = ?""",(id))
    conn.commit()
    c = input("Digite 8 para encerrar a consulta e voltar ao menu ou qualquer coisa para encerrar o programa: ")
    if c == '8':
        conn.close()
        EscolhaUsuario()
    else:
        conn.close()
        sys.exit() 

# Executa esse metodo ao iniciar
if __name__ == "__main__":
    EscolhaUsuario()
