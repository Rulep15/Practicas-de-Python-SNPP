#Escribir un programa que simule una calculadora y que contenga las siguientes
#funciones.
#1º) Muestre un menú con 5 opciones:
# 1. Sumar dos números. ( Función Suma)
# 2. Restar dos números. (Función Resta)
# 3. Multiplicar dos números. (Función Multiplicación)
# 4. Dividir dos números.(Función División)
# 5. Salir.
#2º) Pida por teclado la opción deseada (dato carácter). Deberá ser introducida, mientras
#que, no sea mayor o igual que '1' y menor o igual que '5'.
#3º) Ejecute la opción seleccionada del menú.
#4º) Repita los pasos 1º, 2º y 3º, mientras que, el usuario no seleccione la opción 5 (Salir)
#del menú.
con="SI"
while con=="SI":
 num1=float(input("Ingrese el primer numero "))
 num2=float(input("Ingrese el segundo numero "))

 print("Que desea ejecutar")
 print("Opcion 1 - Suma/ Opcion 2 - Resta / Opcion 3 - Multiplicación / Opcion 4 - División ")

 opc=int(input("Ingrese la opcion: "))

 if opc==1:
    suma=num1+num2
    print("Las suma es",suma)
 elif opc==2:
    resta=num1-num2
    print("La resta es: ",resta)
 elif opc==3:
    multiplica=num1*num2
    print("La multiplicación es: ",multiplica)
 elif opc==4:
    division=num1/num2
    print("La division es: ",division)

 con=input("¿Deseas continuar?: ").upper()