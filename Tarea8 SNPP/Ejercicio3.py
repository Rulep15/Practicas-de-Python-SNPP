#Escribir una función que calcule el factorial de un número. Por ejemplo, 5! =
#5*4*3*2*1 = 120


factorial = (int(input("Ingrese un numero:")))
resultado = factorial * (factorial-1)

for i in range(factorial -2, 0, -1):
    resultado = resultado * i
print("El Factorial es:",resultado)