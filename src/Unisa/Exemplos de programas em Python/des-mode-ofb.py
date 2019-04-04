from Crypto.Cipher import DES
from Crypto import Random

iv = Random.get_random_bytes(8)
des1 = DES.new('01234567', DES.MODE_OFB, iv)
des2 = DES.new('01234567', DES.MODE_OFB, iv)
#text = 'abcdefghijklmnop'
text = raw_input('Digite o texto sendo multiplo de 8 caracteres: ')
cipher_text = des1.encrypt(text)
print 'Texto cifrado: ', cipher_text

decipher_text = des2.decrypt(cipher_text)
print 'Texto decifrado: ', decipher_text
