#Dadas 6 notas, escribir la cantidad de alumnos aprobados y los no aprobados.
#(Aprobados mayores a 1)(No aprobados menor o igual a 1).
num = 6

for i in range(num):
    grade = float(input("Ingrese su nota: "))
    if grade <= 1 :
        print ("Usted reprobo la asignatura :(")
    else:
        print ("Usted aprobo la asignatura :D") 

