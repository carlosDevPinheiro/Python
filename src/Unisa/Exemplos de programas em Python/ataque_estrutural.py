# coding: utf-8
 
import os
import zipfile
 
def ataque_estrutural(img1, img2):
     # Armazena o tamanho das imagens comprimidas;
     tam = []
     
     for img in (img1, img2):
         # Comprime a imagem
         zip = zipfile.ZipFile('imagem.zip', 'w')
         zip.write(img, img, zipfile.ZIP_DEFLATED)
         
         # Obtém o tamanho da imagem comprimida;
         tam.append(float(zip.infolist()[0].compress_size))
         
         # Fecha o arquivo e o remove
         zip.close()
         os.remove('imagem.zip')
         
     # Retorna a proporção entre os tamanhos;
     return tam[1] / tam[0]

img1 = raw_input("Digite o nome da primeira imagem: ")
img2 = raw_input("Digite o nome da segunda imagem: ")

ataque_estrutural(img1, img2)