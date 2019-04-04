#Fonte: http://www.owenstephens.co.uk/blog/2009/10/21/aes-using-ecb-demo-using-python.html

import Image
import sys
import os
from Crypto.Cipher import AES

IV_SIZE = 16
block_size = 16

def check_args():
    try:
        if (len(sys.argv) != 4):
            raise Exception()
        elif (not os.path.isfile(sys.argv[1])):
            raise Exception("Input file must exist")
        elif (not sys.argv[3] in ['CBC', 'ECB']):
            raise Exception("Block cipher mode should be ECB or CBC")
        return (sys.argv[1], sys.argv[2], sys.argv[3])
    except Exception, ex:
        print "Usage:", sys.argv[0], \
          "full_path_to_input_image full_path_to_output_image ECB|CBC"
        if len(ex.args) > 0:
            print "--" + str(ex)
        sys.exit(1)

def encrypt(input_filename, output_filename, cipher_mode):
    #Cifra um arquivo de imagem e escreve a saida como PNG.

    input_image = Image.open(input_filename)

    # Chave deve ser multiplo de 16/24/32 bytes em tamanho.
    key = "0123456789ABCDEF"
    mode = AES.MODE_CBC if cipher_mode == 'CBC' else AES.MODE_ECB
    iv = '2e39234ab3e59652'
    #iv = os.urandom(IV_SIZE)

    aes = AES.new(key, mode, iv)

    image_string = input_image.tostring()
    
    # A string de entrada deve ser preenchida de acordo com o tamanho do bloco de entrada.
    image_padding_length = block_size - len(image_string) % block_size
    image_string += image_padding_length * "~"

    # Gerando a sequencia de imagem criptografada
    encrypted = aes.encrypt(image_string)

    # Criar uma imagem a partir da sequencia criptografada
    encrypted_img = Image.frombuffer("RGB", input_image.size, encrypted, 'raw', "RGB", 0, 1)

    # Criando e salvando a imagem de saida
    encrypted_img.save(output_filename, 'PNG')

    print("Encrypted using AES in " + cipher_mode + " mode and saved to \"" + output_filename + "\"!")

if __name__ == "__main__":
    args = check_args()
    encrypt(*args)
