# -*- coding: cp1252 -*-

def celsius2fahrenheit(a):

    b = (1.8*a)+32.0
    return b

def celsius2kelvin(a):
 
    b = a+273
    return b 

def celsius2reamur(a):

    b = a*0.8
    return b

def fahrenheit2celsius(a):

    b = (a-32)/1.8
    return b

def fahrenheit2kelvin(a):
 
    b = ((a-32)/1.8)+273
    return b 

def fahrenheit2reamur(a):
   
    b = ((a-32)/1.8)*0.8
    return b 

def kelvin2celsius(a):
    
    b = a-273
    return b

def kelvin2fahrenheit(a):
    
    b = ((a-273)*1.8)+32
    return b 

def kelvin2reamur(a):
   
    b = (a-273)*0.8
    return b

def reamur2celsius(a):
    
    b = a/0.8
    return b
    
def reamur2fahrenheit(a):

    b = (a*2.25)+32
    return b

def reamur2kelvin(a):
    
    b = a*(5/4)+273
    return b

        
