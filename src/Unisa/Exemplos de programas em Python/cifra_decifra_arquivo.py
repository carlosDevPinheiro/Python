# -*- coding: cp1252 -*-

import os
import hashlib
import base64
import struct
from Crypto.Cipher import AES
from Crypto import Random

chunksize = 64 * 1024
BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[:-ord(s[len(s)-1:])]

class AESCipher:

    def __init__( self, key ):
        keydigest = hashlib.sha1(key).digest()
        self.key = keydigest[:16]

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) )

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] ))

    def encrypt_file( self, in_filename, out_filename ):
        iv = Random.new().read( AES.block_size )
        encryptor = AES.new(self.key, AES.MODE_CBC, iv)
        filesize = os.path.getsize(in_filename)
        with open( in_filename, 'rb' ) as infile:
            with open( out_filename, 'wb' ) as outfile:
                outfile.write( struct.pack('<Q', filesize) )
                outfile.write(iv)
                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % BS != 0:
                        chunk += ' ' * (BS - len(chunk) % BS)
                    outfile.write(encryptor.encrypt(chunk))

    def decrypt_file( self, in_filename, out_filename ):
        with open(in_filename, 'rb') as infile:
            origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
            iv = infile.read(16)
            decryptor = AES.new(self.key, AES.MODE_CBC, iv)
            with open(out_filename, 'wb') as outfile:
                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    outfile.write(decryptor.decrypt(chunk))
                outfile.truncate(origsize)


# Definindo uma chave
chave = raw_input("Digite uma chave: ")

# Cria uma instância do Objeto De/Cifrador AES
aes = AESCipher(chave)

def codifica():
    a = raw_input("Digite o nome do arquivo a ser cifrado: ")
    a1 = raw_input("Digite o nome escolhido para o arquivo cifrado seguido da extensão .bin: ")
    aes.encrypt_file(a, a1)

def decodifica():
    b = raw_input("Digite o nome do arquivo a ser decifrado: ")
    b1 = raw_input("Digite o novo nome do arquivo decifrado: ")
    aes.decrypt_file(b, b1)

def menu():
    menu = raw_input("Digite 1 para codificar e 2 para decodificar: ")
    if menu == '1':
        codifica()
    elif menu == '2':
        decodifica()
    else:
        print "Digite o valor certo, jumento!"
        menu()

menu()

# Testando cifragem de dados/texto
#cifrado = aes.encrypt( "Eu sou uma mensagem super secreta." )
#decifrado = aes.decrypt( cifrado )

#print cifrado
#print decifrado
