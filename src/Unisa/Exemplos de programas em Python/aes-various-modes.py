from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import random
import Padding

val=raw_input("Digite o texto para cifrar: ")
password=raw_input("Digite a chave: ")
#ival = 100
ival=random.randint(1,10000)

plaintext=val

def encrypt(plaintext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.decrypt(ciphertext))

def encrypt2(plaintext,key, mode,iv):
	encobj = AES.new(key,mode,iv)
	return(encobj.encrypt(plaintext))

def decrypt2(ciphertext,key, mode,iv):
	encobj = AES.new(key,mode,iv)
	return(encobj.decrypt(ciphertext))

key = hashlib.sha256(password).digest()

iv= hex(ival)[2:8].zfill(16)

print "IV: "+iv	

plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode=0)
print "Input data (CMS): "+binascii.hexlify(bytearray(plaintext))

ciphertext = encrypt(plaintext,key,AES.MODE_ECB)
print "Cipher (ECB): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,mode=0)
print "Decrypt: "+plaintext

plaintext=val
plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode=0)

ciphertext = encrypt2(plaintext,key,AES.MODE_CBC,iv)
print "Cipher (CBC): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt2(ciphertext,key,AES.MODE_CBC,iv)
plaintext = Padding.removePadding(plaintext,mode=0)
print "Decrypt: "+plaintext

plaintext=val
plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode=0)

ciphertext = encrypt2(plaintext,key,AES.MODE_CFB,iv)
print "Cipher (CFB): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt2(ciphertext,key,AES.MODE_CFB,iv)
plaintext = Padding.removePadding(plaintext,mode=0)
print "Decrypt: "+plaintext

plaintext=val
plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode=0)

ciphertext = encrypt2(plaintext,key,AES.MODE_OFB,iv)
print "Cipher (OFB): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt2(ciphertext,key,AES.MODE_OFB,iv)
plaintext = Padding.removePadding(plaintext,mode=0)
print "Decrypt: "+plaintext
