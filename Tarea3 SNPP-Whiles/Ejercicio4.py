#Pedir por teclado 10 números. Indicar cuántos de ellos son números positivos, cuantos
#son números negativos y la cantidad de ceros.

x=1
a=0
b=0
c=0
while x <=10:
    n=int(input(f"Ingresa el numero {x} "))
    if n==0:
      a=a+1   
    else:

     if n<0:
         b=b+1
     else:
         c=c+1
    x+=1
print(f"{a} cantidad de ceros")
print(f"{b} numeros son negativos")    
print(f"{c} numeros son positivos")
    
