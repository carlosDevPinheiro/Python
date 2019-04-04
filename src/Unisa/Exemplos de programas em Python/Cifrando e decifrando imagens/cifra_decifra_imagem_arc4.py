import Image
from Crypto.Cipher import ARC4

def cifra():
    a = raw_input("Digite a imagem a ser cifrada: ")
    b = raw_input("Digite a chave: ")
    c = raw_input("Digite o nome da nova imagem cifrada: ")
    ARC4_1 = ARC4.new(b)

    im = Image.open(a)
    image_string = im.tostring()
    cipher_img = ARC4_1.encrypt(image_string)
    new_img = Image.frombuffer("RGB", im.size, cipher_img, 'raw', "RGB", 0, 1)
    new_img.save(c, 'PNG')

def decifra():
    a1 = raw_input("Digite a imagem a ser decifrada: ")
    b1 = raw_input("Digite a chave: ")
    c1 = raw_input("Digite o nome da nova imagem cifrada: ")
    ARC4_2 = ARC4.new(b1)

    im1 = Image.open(a1)
    image_string1 = im1.tostring()
    decipher_img = ARC4_2.decrypt(image_string1)
    new_img1 = Image.frombuffer("RGB", im1.size, decipher_img, 'raw', "RGB", 0, 1)
    new_img1.save(c1, 'PNG') 

def principal():
    a3 = raw_input("Digite 1 para cifrar e 2 para decifrar: ")
    if a3 == '1':
        cifra()
    elif a3 == '2':
        decifra()
    else:
        print "Escolha errada!"
        principal()

principal()

