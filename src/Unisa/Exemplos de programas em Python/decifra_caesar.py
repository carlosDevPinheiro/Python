def decifra_caesar():
    abc = []
    for i in bcd:
      if i == unichr(100):
         abc.append(unichr(97))
      elif i == unichr(101):
         abc.append(unichr(98))
      elif i == unichr(102):
         abc.append(unichr(99))
      elif i == unichr(103):
         abc.append(unichr(100))
      elif i == unichr(104):
         abc.append(unichr(101))
      elif i == unichr(105):
         abc.append(unichr(102))
      elif i == unichr(106):
         abc.append(unichr(103))
      elif i == unichr(107):
         abc.append(unichr(104))
      elif i == unichr(108):
         abc.append(unichr(105))
      elif i == unichr(109):
         abc.append(unichr(106))
      elif i == unichr(110):
         abc.append(unichr(107))
      elif i == unichr(111):
         abc.append(unichr(108))
      elif i == unichr(112):
         abc.append(unichr(109))
      elif i == unichr(113):
         abc.append(unichr(110))
      elif i == unichr(114):
         abc.append(unichr(111))
      elif i == unichr(115):
         abc.append(unichr(112))
      elif i == unichr(116):
         abc.append(unichr(113))
      elif i == unichr(117):
         abc.append(unichr(114))
      elif i == unichr(118):
         abc.append(unichr(115))
      elif i == unichr(119):
         abc.append(unichr(116))   
      elif i == unichr(120):
         abc.append(unichr(117))
      elif i == unichr(121):
         abc.append(unichr(118))
      elif i == unichr(122):
         abc.append(unichr(119))
      elif i == unichr(97):
         abc.append(unichr(120))
      elif i == unichr(98):
         abc.append(unichr(121))
      elif i == unichr(99):
         abc.append(unichr(122)) 
      else:
         print "Escreva letras em caixa baixa!"   

    cdf = "".join(str(x) for x in abc)
    print "Mensagem decodificada: ", cdf

bcd = raw_input("Digite a mensagem a ser decodificada: ")
decifra_caesar()