# Condicional IF
print("Programa de evaluación de notas de alumnos")

notaAlumno=input("Introduce la nota del alumno: ") #Cualquier cosa introducida mediante input es considerada como str

#Función que recibe una nota y evalúa si está aprobado o no
def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspenso"
    return valoracion

print(evaluacion(int(notaAlumno))) #mediante el método int() convertimos el str en int