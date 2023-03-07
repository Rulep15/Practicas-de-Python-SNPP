#Escribir un programa que pregunte al usuario los números ganadores de un sorteo, los
#almacene en una lista y los muestre por pantalla ordenados de menor a
#mayor.
my_list=[]
for i in range (6):
    my_list.append(int(input("Introduce un número ganador ")))
my_list.sort()
print("Los números ganadores son "+str(my_list))



