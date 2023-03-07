#Escriba un programa que pida un número entero mayor que cero y que
#muestre en pantalla sus divisores(agregar los divisores en una lista para luego
#imprimir en pantalla)



my_list=[]
print("Ingrese el Numero ")
x=int(input())

for i in range(1,x+1):
    if x % i==0:
       print("Los divisores son:",[i] )
my_list.sort()

