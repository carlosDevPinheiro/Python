def fatorar(x):          
    A=[]                
    for y in range(2,x): 
        while x%y==0:    
            x=x/y        
            A.append(y)  
    if sum(A)==0:        
        A.append(x)     
    return A 

R=raw_input("Digite Sair para sair, ou qualquer outra coisa para continuar: ").lower()
while R!="sair":
    n=input("Quantos numeros? ")
    N=list(range(n))
    for i in range(n):
        N[i]=input("Proximo Numero: ")
    C=N
    N=map(fatorar,(N))
    mdc=1
    mmc=1
    num=2
    for z in range(n):
        if N[z][-1]>num:
            num=N[z][-1]
    for i in range(2,num+1):
        cont=N[0].count(i)
        for j in range(n):
            if N[j].count(i)>0:
                if N[j].count(i)<cont:
                    cont=N[j].count(i)
            else:
                cont=0
        if i**cont>1:
            mdc*= i**cont
    X=1
    for u in range(len(C)):
        mmc*=C[u]
    for x in range(2,num+1):
        cont=1 
        for y in range(n):
            if N[y].count(x)==0:
                cont=0
        if cont==1:
            X*=x
    mmc=mmc/X
    print "M.D.C = %d e  M.M.C = %d."%(mdc,mmc)
    R=raw_input("Digite Sair para sair, ou qualquer outra coisa para recomecar o programa: ").lower()