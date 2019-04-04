from Crypto.Cipher import DES

des1 = DES.new('01234567', DES.MODE_ECB)
des2 = DES.new('01234567', DES.MODE_ECB)
text = raw_input('Digite o texto com multiplos de 8 caracteres: ')
cipher_text = des1.encrypt(text)
print 'Texto cifrado: ', cipher_text

decipher_text = des2.decrypt(cipher_text)
print 'Texto decifrado: ', decipher_text
