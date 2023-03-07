#Leer un número y mostrar su cuadrado, repetir el proceso hasta que se introduzca un
#número negativo

while True:
    numero=int(input("Introduce un numero: "))
    
    
    if numero<0:
        break
    print(numero**2)