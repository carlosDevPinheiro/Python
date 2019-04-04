from Crypto.Cipher import XOR

xor1 = XOR.new('chave')
xor2 = XOR.new('chave')
text = raw_input('Digite o texto: ')
cipher_text = xor1.encrypt(text)
print 'Texto cifrado: ', cipher_text

decipher_text = xor2.decrypt(cipher_text)
print 'Texto decifrado: ', decipher_text
