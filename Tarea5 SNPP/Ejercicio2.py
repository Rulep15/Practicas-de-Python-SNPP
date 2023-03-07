#Escribir un programa que almacene las asignaturas de un curso (por ejemplo
#Matemáticas, Física, Química, Historia y Lengua, Castellano, Geología, Educación Física,
#etc.) en una lista.
#- Las materias deben insertarse por el método append o insert mediante un input.
#- Demostrar el método pop() o remove() eliminando un elemento de la lista.
#- Recorrer la lista y mostrar en pantalla todos los elementos de la lista
#(“Asignatura:”,listaAsignatura[i]) por cada asignatura de la lista.
#Resultado ejemplo:
#Asignatura: Matemáticas
#Asignatura: Física
#Asignatura: Química
#Asignatura: Historia y Lengua….

materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for i in range(len(materias)-1, -1, -1):
    pts = float(input("¿Qué nota has sacado en " + materias[i] + "?"))
    if pts >= 5:
        materias.pop(i)
print("Tienes que repetir " + str(materias))







