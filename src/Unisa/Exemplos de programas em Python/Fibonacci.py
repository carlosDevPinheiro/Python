def fibonacci(n):
   a=0
   b=1
   for i in range(0,n):
       temp=a
       a=b
       b=temp+b
   return a

c=input('Coloque o valor maximo: ')
for c in range(0,c):
   print fibonacci(c)