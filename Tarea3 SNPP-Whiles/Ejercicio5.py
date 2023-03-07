#Escribir un programa que visualice en pantalla los números pares entre 1 y 25.

x=1
while x<=25:
    if x % 2 == 0:
        print("El numero ",x," es par")
    x=x+1
