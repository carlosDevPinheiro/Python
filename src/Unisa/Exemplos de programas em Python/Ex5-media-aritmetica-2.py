

scorenumber = input("Com quantos numeros voce quer fazer a media? ") 
counter = 0.0 

tempnumber1 = 0.0 

tempnumber2 = 0.0  


while counter < scorenumber: 
    
  counter = counter + 1 
    
  tempnumber1 = input("Digite um dos numeros componentes da media: ") 
    
  tempnumber2 = tempnumber1 + tempnumber2 
    
  print tempnumber2 
  
scoresum = tempnumber2 

print "A soma dos numeros: " + str(scoresum) 

 


average = scoresum / scorenumber 
print "A media: " + str(average)