#01) Escriba un programa que pida un año y que muestre en pantalla si es
#bisiesto o no. Condiciones para determinar cuándo un año es bisiesto.
#1. Debe ser divisible entre 4.
#2. No debe ser divisible entre 100.
#3. Debe ser divisible entre 400.
#Observación:
#a) Si se cumple la condición 1 y 2 se puede afirmar que el año es bisiesto.
#b) Si se cumple la condición 1, no se cumple la condición 2 y se cumple la
#condición 3 entonces se puede afirmar que el año es bisiesto.
#Se evaluara:
# Definición de una función anho_bisiesto. 2P
# Uso de las estructuras condicionales. 1P

print("Introduce el Año")
año=int(input("Año "))
if año%4==0:
    if año%100 !=0 or año%400==0:
        print("Bisiesto")
    else:
        print("No es Bisiesto")
else:
    print("No Bisiesto")


